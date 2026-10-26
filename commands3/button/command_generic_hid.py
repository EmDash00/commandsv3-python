"""Python port of the Java ``CommandGenericHID`` wrapper.

The wrapper creates cached ``commands2.Trigger`` objects around a
``wpilib.GenericHID`` and uses RobotPy's ``Scheduler`` and event- loop
APIs. POV angles are integers in degrees: up is 0, right is 90, down is
180, left is 270, and center/not pressed is -1.
"""

from __future__ import annotations

from threading import RLock
from typing import SupportsIndex, SupportsInt

from wpilib import DriverStation, GenericHID

from commands3.event_loop import EventLoop
from commands3.scheduler import Scheduler
from commands3.trigger import Trigger

_hids_lock = RLock()
# Hold each scheduler alongside its port map, and compare schedulers by identity.
_instances: dict[int, tuple[Scheduler, dict[int, CommandGenericHID]]] = {}


def get_command_generic_hid(
    port: SupportsInt | SupportsIndex, scheduler: Scheduler | None = None
) -> CommandGenericHID:
    """Get the cached wrapper for a scheduler and Driver Station port.

    :port: Driver Station USB port for the HID. :scheduler: Scheduler to
    associate with the wrapper. Defaults to the     singleton command
    scheduler.

    :returns: The same wrapper for repeated requests with that scheduler
        and port.
    """
    scheduler = scheduler or Scheduler.get_default()
    scheduler_id = id(scheduler)
    port = int(port)
    with _hids_lock:
        cached_scheduler, ports = _instances.get(scheduler_id, (scheduler, {}))

        ports = ports if cached_scheduler is not scheduler else {}
        instance = ports.get(port)

        if instance is None:
            instance = CommandGenericHID(port, scheduler=scheduler)
            ports[port] = instance

        _instances[scheduler_id] = (scheduler, ports)
        return instance


class CommandGenericHID:
    """A ``GenericHID`` wrapper that provides command-based trigger factories.

    Trigger instances are cached by event loop and input parameters, so
    repeated calls with the same arguments return the same trigger
    object.
    """

    def __init__(
        self,
        hid: GenericHID | SupportsInt | SupportsIndex,
        *,
        scheduler: Scheduler | None = None,
    ) -> None:
        """Construct a device wrapper from a port or an existing HID.

        :hid: Driver Station USB port for the HID. Use this or ``hid``.

        :scheduler: Scheduler that polls and schedules commands from
        triggers. Defaults to the singleton command scheduler.
        """
        self._scheduler = scheduler or Scheduler.get_default()
        self._default_loop = self._scheduler.get_default_event_loop()
        self._last_pov_state = -1

        if isinstance(hid, GenericHID):
            self._hid = hid
        elif isinstance(hid, SupportsInt | SupportsIndex):
            self._hid = DriverStation.get_generic_hid(hid)
        else:
            raise ValueError("hid must be a GenericHID or int.")

        self._button_cache: dict[EventLoop, dict[tuple[int, bool], Trigger]] = {}
        self._button_release_cache: dict[EventLoop, dict[int, Trigger]] = {}
        self._button_press_cache: dict[EventLoop, dict[int, Trigger]] = {}
        self._axis_less_than_cache: dict[
            EventLoop, dict[tuple[int, float], Trigger]
        ] = {}
        self._axis_greater_than_cache: dict[
            EventLoop, dict[tuple[int, float], Trigger]
        ] = {}
        self._axis_magnitude_greater_than_cache: dict[
            EventLoop, dict[tuple[int, float], Trigger]
        ] = {}
        self._pov_cache: dict[EventLoop, dict[tuple[int, int], Trigger]] = {}
        self._pov_pressed_cache: dict[EventLoop, dict[tuple[int, int], Trigger]] = {}
        self._pov_released_cache: dict[EventLoop, dict[tuple[int, int], Trigger]] = {}
        self._pov_transition_cache: dict[
            EventLoop, dict[tuple[int, int, int], Trigger]
        ] = {}

    @classmethod
    def get_command_generic_hid(
        cls,
        port: SupportsInt | SupportsIndex,
        scheduler: Scheduler | None = None,
    ) -> CommandGenericHID:
        """Get the cached wrapper for a scheduler and Driver Station port.

        Args:
            port: Driver Station USB port for the HID.
            scheduler: Scheduler to associate with the wrapper.
            Defaults to the         singleton command scheduler.

        Returns:     The same wrapper for repeated requests with that scheduler and
        port.
        """
        return get_command_generic_hid(port, scheduler)

    def get_hid(self) -> GenericHID:
        """Return the wrapped ``GenericHID`` object."""
        return self._hid

    @property
    def hid(self) -> GenericHID:
        return self._hid

    def get_scheduler(self) -> Scheduler:
        """Return the scheduler associated with this wrapper."""
        return self._scheduler

    @property
    def scheduler(self) -> Scheduler:
        return self._scheduler

    def button(
        self, button: int, inverted: bool = False, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger for a raw button.

        :param button: Button index, starting at 1.
        :param inverted: Whether or not to invert the trigger.
        :param loop: Event loop to attach the trigger to. Defaults to
            the scheduler's default button loop.
        :returns: A cached trigger for the button's digital signal.
        """
        loop = loop or self._default_loop
        cache = self._button_cache.setdefault(loop, {})
        if button not in cache:
            cache[(button, inverted)] = Trigger(
                lambda: self._hid.get_raw_button(button) and inverted,
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[(button, inverted)]

    def button_pressed(self, button: int, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for a raw button press.

        :param button: Button index, starting at 1.
        :param loop: Event loop to attach the trigger to. Defaults to
            the scheduler's default button loop.
        :returns: A cached trigger for the button's digital signal.
        """
        loop = loop or self._default_loop
        cache = self._button_press_cache.setdefault(loop, {})
        if button not in cache:
            cache[button] = Trigger(
                lambda: self._hid.get_raw_button_pressed(button),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[button]

    def button_released(self, button: int, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for a raw button release.

        :param button: Button index, starting at 1.
        :param loop: Event loop to attach the trigger to. Defaults to
            the scheduler's default button loop.
        :returns: A cached trigger for the button's digital signal.
        """
        loop = loop or self._default_loop
        cache = self._button_release_cache.setdefault(loop, {})
        if button not in cache:
            cache[button] = Trigger(
                lambda: self._hid.get_raw_button_released(button),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[button]

    def pov(
        self,
        angle: int,
        *,
        pov: int = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Create or retrieve a trigger for a POV angle that triggers as long
        as the POV button holds the specified angle.

        POV angles are measured clockwise from up; use ``-1`` for center/not pressed.
        For example, right is 90 degrees and down is 180 degrees.

        :param angle: POV angle in degrees, or -1 for the center position.
        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the scheduler's
            default button loop.

        Returns:     A cached trigger that is true while the POV matches ``angle``.
        """
        loop = loop or self._default_loop
        key = (pov, angle)
        cache = self._pov_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda: self._hid.get_pov(pov) == angle,
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def check_pov_transition(self, from_angle: int, to_angle: int, pov: int = 0):
        """Check whether or not the POV button has been pressed with
        `to_angle` from releasing `from_angle`.

        :param to_angle: The angle to check that is being pressed.
        :param to_angle: The angle to check that is being released.
        :returns: True if the POV button's state has become `to_angle`
            when its state was `from_angle` the last time it was checked.
        """
        state = self._hid.get_pov(pov)
        ret = (self._last_pov_state == from_angle) and (state == to_angle)
        self._last_pov_state = state
        return ret

    def check_pov_pressed(self, angle: int, pov: int = 0):
        """Check whether or not the POV button has entered the state defined by
        the angle.

        :param angle: The angle to check.
        :param pov: The POV button to check.
        :returns: True if the POV button's state has become the
            specified angle since the last check and False otherwise.
        """
        state = self._hid.get_pov(pov)
        ret = (state != self._last_pov_state) and (state == angle)
        self._last_pov_state = state
        return ret

    def check_pov_released(self, angle: int, pov: int = 0):
        """Check whether or not the POV button has exited the state defined by
        the angle.

        :param angle: The angle to check.
        :param pov: The POV button to check.
        :returns: True if the POV button's state has become the
            specified angle since the last check and False otherwise.
        """
        state = self._hid.get_pov(pov)
        ret = (self._last_pov_state == angle) and (state != angle)
        self._last_pov_state = state
        return ret

    def pov_angle_pressed(
        self,
        angle: int,
        *,
        pov: int = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Create or retrieve a trigger for a POV angle that triggers once when
        the POV button is pressed with the specified angle.

        POV angles are measured clockwise from up; use ``-1`` for
        center/not pressed. For example, right is 90 degrees and down is
        180 degrees.

        :param angle: POV angle in degrees, or -1 for the center
            position.
        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A cached trigger that is True when the POV changes to
            ``angle``.
        """
        loop = loop or self._default_loop
        key = (pov, angle)
        cache = self._pov_pressed_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda: self.check_pov_pressed(angle, pov),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def pov_angle_released(
        self,
        angle: int,
        *,
        pov: int = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Create or retrieve a trigger for a POV angle that triggers once when
        the POV button is released from the specified angle.

        POV angles are measured clockwise from up; use ``-1`` for
        center/not pressed. For example, right is 90 degrees and down is
        180 degrees.

        :param angle: POV angle in degrees, or -1 for the center
            position.
        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A cached trigger that is True when the POV changes to
            ``angle``.
        """
        loop = loop or self._default_loop
        key = (pov, angle)
        cache = self._pov_released_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda: self.check_pov_released(angle, pov),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def pov_angle_transition(
        self,
        from_angle: int,
        to_angle: int,
        *,
        pov: int = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Create or retrieve a trigger for a POV angle that triggers once when
        the POV button transitions from `from_angle` to `to_angle`.

        POV angles are measured clockwise from up; use ``-1`` for
        center/not pressed. For example, right is 90 degrees and down is
        180 degrees.

        :param angle: POV angle in degrees, or -1 for the center
            position.
        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A cached trigger that is True when the POV changes to
            ``angle``.
        """
        loop = loop or self._default_loop
        key = (pov, from_angle, to_angle)
        cache = self._pov_transition_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda: self.check_pov_transition(from_angle, to_angle, pov),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def pov_up(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up direction
        """
        return self.pov(0, pov=pov, loop=loop)

    def pov_up_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up-right
        direction. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's up-right direction
        """
        return self.pov(45, pov=pov, loop=loop)

    def pov_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's right
        direction. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's right direction
        """
        return self.pov(90, pov=pov, loop=loop)

    def pov_down_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down-right
        direction. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's down-right direction
        """
        return self.pov(135, pov=pov, loop=loop)

    def pov_down(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down direction.
        :param pov: POV index to read, if there are multiple. :param loop:
        Event loop for the trigger. Defaults to the scheduler's default button
        loop.

        :returns: A trigger for the specified POV's down direction
        """
        return self.pov(180, pov=pov, loop=loop)

    def pov_down_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down-left
        direction. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's down-left direction
        """
        return self.pov(225, pov=pov, loop=loop)

    def pov_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's left direction.
        :param pov: POV index to read, if there are multiple. :param loop:
        Event loop for the trigger. Defaults to the scheduler's default button
        loop.

        :returns: A trigger for the specified POV's left direction
        """
        return self.pov(270, pov=pov, loop=loop)

    def pov_up_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up-left
        direction. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's up-left direction
        """
        return self.pov(315, pov=pov, loop=loop)

    def pov_center(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's center
        position. :param pov: POV index to read, if there are multiple. :param
        loop: Event loop for the trigger. Defaults to the scheduler's default
        button loop.

        :returns: A trigger for the specified POV's center direction
        """
        return self.pov(-1, pov=pov, loop=loop)

    def axis_less_than(
        self, axis: int, threshold: float, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger true when an axis is below a threshold.

        Args:     axis: Axis index, starting at 0.     threshold: Value below which the
        trigger is true.     loop: Event loop to attach the trigger to. Defaults to the
        scheduler's default button loop.

        Returns:     A cached axis-comparison trigger.
        """
        loop = loop or self._default_loop
        key = (axis, threshold)
        cache = self._axis_less_than_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda axis=axis, threshold=threshold: (
                    self.get_raw_axis(axis) < threshold
                ),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def axis_greater_than(
        self, axis: int, threshold: float, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger true when an axis exceeds a threshold.

        Args:     axis: Axis index, starting at 0.     threshold: Value above which the
        trigger is true.     loop: Event loop to attach the trigger to. Defaults to the
        scheduler's default button loop.

        Returns:     A cached axis-comparison trigger.
        """
        loop = loop or self._default_loop
        key = (axis, threshold)
        cache = self._axis_greater_than_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda axis=axis, threshold=threshold: (
                    self.get_raw_axis(axis) > threshold
                ),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def axis_magnitude_greater_than(
        self, axis: int, threshold: float, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger true when an axis magnitude exceeds a
        threshold.

        Args:     axis: Axis index, starting at 0.     threshold: Magnitude above which
        the trigger is true.     loop: Event loop to attach the trigger to. Defaults to
        the         scheduler's default button loop.

        Returns:     A cached axis-magnitude trigger.
        """
        loop = loop or self._default_loop
        key = (axis, threshold)
        cache = self._axis_magnitude_greater_than_cache.setdefault(loop, {})
        if key not in cache:
            cache[key] = Trigger(
                lambda axis=axis, threshold=threshold: (
                    abs(self.get_raw_axis(axis)) > threshold
                ),
                scheduler=self._scheduler,
                loop=loop,
            )
        return cache[key]

    def get_raw_axis(self, axis: int) -> float:
        """Return the value of the specified axis (axis indices start at 0)."""
        return self._hid.get_raw_axis(axis)

    def set_rumble(self, rumble_type: GenericHID.RumbleType, value: float) -> None:
        """Set HID rumble output to a normalized value from 0 to 1.

        Args:     rumble_type: Rumble motor selection, such as
        ``GenericHID.RumbleType.kLeftRumble`` or ``kRightRumble``.     value: Normalized
        rumble strength from 0 to 1.
        """
        self._hid.set_rumble(rumble_type, value)

    def is_connected(self) -> bool:
        """Return whether the HID is connected to the Driver Station."""
        return self._hid.is_connected()
