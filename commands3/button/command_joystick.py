from typing import SupportsIndex, SupportsInt

from wpilib import GenericHID, Joystick
from wpilib._wpilib import POVDirection

from commands3.button.command_generic_hid import CommandGenericHID
from commands3.scheduler import EventLoop, Scheduler


class CommandJoystick:
    def __init__(
        self,
        port: GenericHID | SupportsInt | SupportsIndex,
        scheduler: Scheduler | None = None,
    ):
        self._scheduler = scheduler or Scheduler.get_default()
        self._default_loop = self._scheduler.get_default_event_loop()
        self._joystick = Joystick(port)
        self._hid = CommandGenericHID(port)

    def get_hid(self) -> CommandGenericHID:
        """Get the underlying CommandGenericHID object.

        :returns: The underlying CommandGeniericHID object.
        """
        return self._hid

    @property
    def hid(self) -> CommandGenericHID:
        """The underlying CommandGenericHID object."""
        return self._hid

    def get_joystick(self) -> Joystick:
        """Get the underlying CommandGenericHID object.

        :returns: The underlying CommandGeniericHID object.
        """
        return self._joystick

    @property
    def joystick(self) -> Joystick:
        """The underlying CommandGenericHID object."""
        return self._joystick

    def pov(
        self,
        angle: POVDirection,
        pov: SupportsIndex | SupportsInt = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct an event instance around the POV button's direction.

        :param angle: The direction which causes this trigger to be
            invoked.
        :param pov: The POV button index if there are multiple.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.pov(angle.value, pov=int(pov), loop=loop)

    def pov_angle_pressed(
        self,
        angle: POVDirection,
        pov: SupportsIndex | SupportsInt = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance that triggers when the specified the
        POV button is pressed with the specified angle.

        :param angle: The direction which causes this trigger to be
            invoked.
        :param pov: The POV button index if there are multiple.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        self._hid.pov(angle.value, pov=int(pov), loop=loop)

    def pov_angle_released(
        self,
        angle: POVDirection,
        pov: SupportsIndex | SupportsInt = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance that triggers once when the specified
        the POV button is released from the specified angle.

        :param angle: The direction which causes this trigger to be
            invoked.
        :param pov: The POV button index if there are multiple.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        self._hid.pov_angle_released(angle.value, pov=int(pov), loop=loop)

    def pov_angle_transtion(
        self,
        from_angle: POVDirection,
        to_angle: POVDirection,
        pov: SupportsIndex | SupportsInt = 0,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance that triggers once when the specified
        the POV button transitions from `from_angle` to `to_angle`

        :param angle: The direction which causes this trigger to be
            invoked.
        :param pov: The POV button index if there are multiple.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        self._hid.pov_angle_transition(
            from_angle.value, to_angle.value, pov=int(pov), loop=loop
        )

    def pov_up(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up direction
        """
        return self._hid.pov(0, pov=pov, loop=loop)

    def pov_up_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up-right
        direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-right direction
        """
        return self._hid.pov(45, pov=pov, loop=loop)

    def pov_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's right
        direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's right direction
        """
        return self._hid.pov(90, pov=pov, loop=loop)

    def pov_down_right(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down-right
        direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-right direction
        """
        return self._hid.pov(135, pov=pov, loop=loop)

    def pov_down(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down direction.
        :param pov: POV index to read, if there are multiple.

        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down direction
        """
        return self._hid.pov(180, pov=pov, loop=loop)

    def pov_down_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's down-left
        direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-left direction
        """
        return self._hid.pov(225, pov=pov, loop=loop)

    def pov_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's left direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's left direction
        """
        return self._hid.pov(270, pov=pov, loop=loop)

    def pov_up_left(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's up-left
        direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-left direction
        """
        return self._hid.pov(315, pov=pov, loop=loop)

    def pov_center(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger for the specified POV's center
        position.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's center direction
        """
        return self._hid.pov(-1, pov=pov, loop=loop)

    def pov_up_pressed(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the up direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up direction
        """
        return self._hid.pov_angle_pressed(0, pov=pov, loop=loop)

    def pov_up_right_pressed(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the up-right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-right direction
        """
        return self._hid.pov_angle_pressed(45, pov=pov, loop=loop)

    def pov_right_pressed(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's right direction
        """
        return self._hid.pov_angle_pressed(90, pov=pov, loop=loop)

    def pov_down_right_pressed(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the down-right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-right direction
        """
        return self._hid.pov_angle_pressed(135, pov=pov, loop=loop)

    def pov_down_pressed(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the down direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down direction
        """
        return self._hid.pov_angle_pressed(180, pov=pov, loop=loop)

    def pov_down_left_pressed(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's presses the down-left direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-left direction
        """
        return self._hid.pov_angle_pressed(225, pov=pov, loop=loop)

    def pov_left_pressed(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's presses the left direction.


        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's left direction
        """
        return self._hid.pov_angle_pressed(270, pov=pov, loop=loop)

    def pov_up_left_pressed(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's presses the up-left direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-left direction
        """
        return self._hid.pov_angle_pressed(315, pov=pov, loop=loop)

    def pov_center_pressed(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's presses the center direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's center direction
        """
        return self._hid.pov_angle_pressed(-1, pov=pov, loop=loop)

    def pov_up_released(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the up direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up direction
        """
        return self._hid.pov_angle_released(0, pov=pov, loop=loop)

    def pov_up_right_released(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the up-right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-right direction
        """
        return self._hid.pov_angle_released(45, pov=pov, loop=loop)

    def pov_right_released(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's right direction
        """
        return self._hid.pov_angle_released(90, pov=pov, loop=loop)

    def pov_down_right_released(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the down-right direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-right direction
        """
        return self._hid.pov_angle_released(135, pov=pov, loop=loop)

    def pov_down_released(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the down direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down direction
        """
        return self._hid.pov_angle_released(180, pov=pov, loop=loop)

    def pov_down_left_released(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when the specified
        POV's  releases from the down-left direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's down-left direction
        """
        return self._hid.pov_angle_released(225, pov=pov, loop=loop)

    def pov_left_released(self, pov: int = 0, loop: EventLoop | None = None) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's  releases from the left direction.


        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's left direction
        """
        return self._hid.pov_angle_released(270, pov=pov, loop=loop)

    def pov_up_left_released(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's  releases from the up-left direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's up-left direction
        """
        return self._hid.pov_angle_released(315, pov=pov, loop=loop)

    def pov_center_released(
        self, pov: int = 0, loop: EventLoop | None = None
    ) -> Trigger:
        """Create or retrieve a trigger that is invoked once when
        the specified POV's  releases from the center direction.

        :param pov: POV index to read, if there are multiple.
        :param loop: Event loop for the trigger. Defaults to the
            scheduler's default button loop.
        :returns: A trigger for the specified POV's center direction
        """
        return self._hid.pov_angle_released(-1, pov=pov, loop=loop)


    def trigger(self, inverted: bool = False, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the trigger button's digital
        signal.

        :param inverted: Whether or not to invert the trigger.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button(
            Joystick.ButtonType.TRIGGER_BUTTON.value,
            inverted,
            loop or self._default_loop,
        )

    def trigger_pressed(self, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the trigger button being pressed.

        :param inverted: Whether or not to invert the trigger.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button_pressed(
            Joystick.ButtonType.TRIGGER_BUTTON.value,
            loop or self._default_loop,
        )

    def trigger_released(self, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the trigger button being
        released.

        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button_released(
            Joystick.ButtonType.TRIGGER_BUTTON.value,
            loop or self._default_loop,
        )

    def button(
        self,
        button: SupportsInt | SupportsIndex,
        inverted: bool = False,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance around one of the joystick's button's
        digital signal."""
        return self._hid.button(int(button), inverted, loop or self._default_loop)

    def button_pressed(
        self,
        button: SupportsInt | SupportsIndex,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance around one of the joystick's buttons
        being pressed."""
        return self._hid.button_pressed(int(button), loop or self._default_loop)

    def button_released(
        self,
        button: SupportsInt | SupportsIndex,
        loop: EventLoop | None = None,
    ) -> Trigger:
        """Construct and event instance around one of the joystick's buttons
        being released."""
        return self._hid.button_released(int(button), loop or self._default_loop)

    def top(self, inverted: bool = False, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the top button's digital signal.

        :param inverted: Whether or not to invert the trigger.
        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button(
            Joystick.ButtonType.TOP_BUTTON.value, inverted, loop or self._default_loop
        )

    def top_pressed(self, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the top button being pressed..

        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button_pressed(
            Joystick.ButtonType.TOP_BUTTON.value, loop or self._default_loop
        )

    def top_released(self, loop: EventLoop | None = None) -> Trigger:
        """Construct an event instance around the top button being pressed..

        :param loop: The event loop instance to attach the event to. If
            None, uses the default event loop.
        :returns: An event instance representing the top button's
            digital signal attached to the given loop.
        """
        return self._hid.button_released(
            Joystick.ButtonType.TOP_BUTTON.value, loop or self._default_loop
        )

    def set_x_channel(self, channel: SupportsInt | SupportsIndex):
        """Set the channel associated with the X axis.

        :param channel: The channel to set the axis to.
        """
        return self._joystick.set_x_channel(channel)

    def set_y_channel(self, channel: SupportsInt | SupportsIndex):
        """Set the channel associated with the Y axis.

        :param channel: The channel to set the axis to.
        """
        return self._joystick.set_y_channel(channel)

    def set_z_channel(self, channel: SupportsInt | SupportsIndex):
        """Set the channel associated with the Z axis.

        :param channel: The channel to set the axis to.
        """
        return self._joystick.set_z_channel(channel)

    def set_throttle_channel(self, channel: SupportsInt | SupportsIndex):
        """Set the channel associated with the throttle axis.

        :param channel: The channel to set the axis to.
        """
        return self._joystick.set_throttle_channel(channel)

    def set_twist_channel(self, channel: SupportsInt | SupportsIndex):
        """Set the channel associated with the twist axis.

        :param channel: The channel to set the axis to.
        """
        return self._joystick.set_twist_channel(channel)

    def get_x_channel(self) -> float:
        """Get the channel currently associated with the X axis."""
        return self._joystick.get_x_channel()

    @property
    def x_channel(self) -> float:
        """The channel currently associated with the X axis."""
        return self._joystick.get_x_channel()

    def get_y_channel(self) -> float:
        """Get the channel currently associated with the Y axis."""
        return self._joystick.get_y_channel()

    @property
    def y_channel(self) -> float:
        """The channel currently associated with the Y axis."""
        return self._joystick.get_y_channel()

    def get_z_channel(self) -> float:
        """Get the channel currently associated with the Z axis."""
        return self._joystick.get_z_channel()

    @property
    def z_channel(self) -> float:
        """The channel currently associated with the Z axis."""
        return self._joystick.get_z_channel()

    def get_twist_channel(self) -> float:
        """Get the channel currently associated with the twist axis."""
        return self._joystick.get_twist_channel()

    @property
    def twist_channel(self) -> float:
        """The channel currently associated with the twist axis."""
        return self._joystick.get_twist_channel()

    def get_throttle_channel(self) -> float:
        """Get the channel currently associated with the throttle axis."""
        return self._joystick.get_twist_channel()

    @property
    def throttle_channel(self) -> float:
        """The channel currently associated with the throttle axis."""
        return self._joystick.get_throttle_channel()

    def get_x(self) -> float:
        """Get the x value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_x()

    @property
    def x(self) -> float:
        """The x value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_x()

    def get_y(self) -> float:
        """Get the y value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_y()

    @property
    def y(self) -> float:
        """The y value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_y()

    def get_z(self) -> float:
        """Get the z value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_z()

    @property
    def z(self) -> float:
        """The z value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_z()

    def get_twist(self) -> float:
        """Get the twist value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_twist()

    @property
    def twist(self) -> float:
        """The twist value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_twist()

    def get_throttle(self) -> float:
        """Get the throttle value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_throttle()

    @property
    def throttle(self) -> float:
        """The throttle value of the current joystick.

        Depends on the mapping of the joystick connected to the current
        port.
        """
        return self._joystick.get_throttle()

    def get_magnitude(self) -> float:
        """Get the magnitude of the vector formed by the joystick's current
        position relative to the origin."""
        return self._joystick.get_magnitude()

    @property
    def magnitude(self) -> float:
        """The magnitude of the vector formed by the joystick's current."""
        return self._joystick.get_magnitude()

    def get_direction_degrees(self) -> float:
        """Get the direction of the vector formed by the joystick and its
        origin in degrees.

        0 is forward and clockwise is positive. (Straight right is 90.)
        """
        return self._joystick.get_direction_degrees()

    @property
    def direction_degrees(self) -> float:
        """The direction of the vector formed by the joystick and its origin in
        degrees.

        0 is forward and clockwise is positive. (Straight right is 90.)
        """
        return self._joystick.get_direction_degrees()

    def get_direction_radians(self) -> float:
        """Get the direction of the vector formed by the joystick and its
        origin in radians.

        0 is forward and clockwise is positive. (Straight right is π/2.)
        """
        return self._joystick.get_direction_radians()

    @property
    def direction_radians(self) -> float:
        """The direction of the vector formed by the joystick and its origin in
        radians.

        0 is forward and clockwise is positive. (Straight right is π/2.)
        """
        return self._joystick.get_direction_radians()

    @property
    def direction(self) -> float:
        """The direction of the vector formed by the joystick and its origin in
        degrees.

        0 is forward and clockwise is positive. (Straight right is π/2.)
        """
        return self._joystick.get_direction_radians()
