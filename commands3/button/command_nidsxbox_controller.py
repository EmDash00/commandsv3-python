from typing import SupportsIndex, SupportsInt

from wpilib import GenericHID, NiDsXboxController

from commands3.button import CommandGenericHID
from commands3.event_loop import EventLoop
from commands3.scheduler import Scheduler

Axis = NiDsXboxController.Axis
Button = NiDsXboxController.Button
RumbleType = GenericHID.RumbleType


class CommandNiDsXboxController:
    """A version of ``NiDsXboxController`` with ``Trigger`` factories for command-
    based use.

    See ``NiDsXboxController``.
    """

    def __init__(
        self,
        controller: NiDsXboxController | SupportsInt | SupportsIndex,
        *,
        scheduler: Scheduler | None = None,
    ):
        """Construct an instance of NiDsXboxController.

        Commands bound to buttons are scheduled on ``scheduler`` using
        its default event loop if no event loop is provided. If no
        scheduler is provided, the default scheduler is used.

        :param controller: The port index on the Driver Station that the
            controller is plugged into.
        :param scheduler: The scheduler that should execute triggered
            commands. If None, uses the default scheduler.
        """
        scheduler = scheduler if scheduler is not None else Scheduler.get_default()
        self._default_loop = scheduler.get_default_event_loop()

        if isinstance(controller, NiDsXboxController):
            self._controller = controller
        elif isinstance(gamepad, SupportsInt | SupportsIndex):
            self._controller = NiDsXboxController(port)
        else:
            raise TypeError("gamepad must be a port or a NiDsXboxController.")

        self._hid = CommandGenericHID(self._controller.get_hid(), scheduler=scheduler)

    def get_hid(self) -> CommandGenericHID:
        """Get the underlying ``CommandGenericHID`` object."""
        return self._hid

    @property
    def hid(self) -> CommandGenericHID:
        """The underlying ``CommandGenericHID`` object."""
        return self._hid

    def get_controller(self):
        """Get the underlying ``NiDsXboxController`` object."""
        return self._controller

    @property
    def gamepad(self) -> NiDsXboxController:
        """The underlying ``NiDsXboxController`` object."""
        return self._controller

    def _get_button(
        self, btn: int, inverted: bool = False, loop: EventLoop | None = None
    ):
        """Build a trigger for a named gamepad button."""
        return self.button(btn, inverted, loop or self._default_loop)

    def left_stick(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the left stick button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left stick button's digital
            signal.
        """
        return self._get_button(Button.LEFT_STICK, inverted, loop)

    def right_stick(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right stick button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the right stick button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_STICK, inverted, loop)

    def left_bumper(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the left bumper button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left bumper button's
            digital signal.
        """
        return self._get_button(Button.LEFT_BUMPER, inverted, loop)

    def right_bumper(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right bumper button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the right bumper button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_BUMPER, inverted, loop)


    def a(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the A button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Down button's
            digital signal attached to the given loop.
        """
        return self._hid.button(Button.A, inverted, loop)

    def a_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the A button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the A button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.A, loop)

    def a_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the A button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the A button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.A, loop)

    def b(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the B button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button(Button.B, inverted, loop)

    def b_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the B button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.B, loop)

    def b_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the B button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.B, loop)

    def x(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the X button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button(Button.X, inverted, loop)

    def x_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the X button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.X, loop)

    def x_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the X button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.X, loop)

    def y(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the Y button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Up button's
            digital signal attached to the given loop.
        """
        return self._hid.button(Button.Y, inverted, loop)

    def y_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the Y button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Y button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.Y, loop)

    def y_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the Y button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Y button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.Y, loop)

    def axis_greater_than(
        self,
        axis: SupportsInt | SupportsIndex,
        threshold: float,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the selected axis exceeds a
        threshold."""
        if isinstance(axis, SupportsInt | SupportsIndex):
            axis = int(axis)
        else:
            raise TypeError("axis must be Axis, SupportsInt, or SupportsIndex")

        event_loop = loop or self._default_loop
        return self._hid.axis_greater_than(axis, threshold, event_loop)

    def axis_less_than(
        self,
        axis: SupportsInt | SupportsIndex,
        threshold: float,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the selected axis exceeds a
        threshold."""
        if isinstance(axis, SupportsInt | SupportsIndex):
            axis = int(axis)
        else:
            raise TypeError("axis must be Axis, SupportsInt, or SupportsIndex")

        event_loop = loop or self._default_loop
        return self._hid.axis_less_than(axis, threshold, event_loop)

    def button(
        self,
        btn: SupportsInt | SupportsIndex,
        inverted: bool = False,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the button is held down.

        :param btn: The button to check.
        :param inverted: Whether or not to invert the trigger.
        """
        if isinstance(btn, SupportsInt | SupportsIndex):
            btn = int(btn)
        else:
            raise TypeError("axis must be Axis, SupportsInt, or SupportsIndex")

        event_loop = loop or self._default_loop
        return self._hid.button(btn, inverted, event_loop)

    def left_trigger(self, threshold=0.5, loop: EventLoop | None = None):
        """Construct a trigger around the left trigger axis.

        The trigger is true when the axis value is greater than
        ``threshold``. The threshold should be in the range [0, 1],
        where 0 is the unpressed state. By default, the threshold is 0.5
        and the scheduler's default event loop is used.

        :threshold: Minimum axis value for the trigger to be true.

        :loop: Event loop to attach the trigger to.

        :returns: A trigger that is true when the left trigger axis
            exceeds the provided threshold.
        """
        return self.axis_greater_than(Axis.LEFT_TRIGGER, threshold, loop)

    def left_trigger_release(self, threshold=0.5, loop: EventLoop | None = None):
        """Construct a trigger around the left trigger axis.

        The trigger is true when the axis value is less than
        ``threshold``. The threshold should be in the range [0, 1],
        where 0 is the unpressed state. By default, the threshold is 0.5
        and the scheduler's default event loop is used.

        :threshold: Minimum axis value for the trigger to be true.

        :loop: Event loop to attach the trigger to.

        :returns: A trigger that is true when the left trigger axis
            exceeds the provided threshold.
        """
        return self.axis_less_than(Axis.LEFT_TRIGGER, threshold, loop)

    def right_trigger(self, threshold=0.5, loop: EventLoop | None = None):
        """Construct a trigger around the right trigger axis.

        The trigger is true when the axis value is greater than
        ``threshold``. The threshold should be in the range [0, 1],
        where 0 is the unpressed state. By default, the threshold is 0.5
        and the scheduler's default event loop is used.

        :threshold: Maximum axis value for the trigger to be true.
        :loop: Event loop to attach the trigger to.

        :returns: A trigger that is true when the right trigger axis
            exceeds the provided threshold.
        """
        return self.axis_greater_than(Axis.RIGHT_TRIGGER, threshold, loop)

    def right_trigger_release(self, threshold=0.5, loop: EventLoop | None = None):
        """Construct a trigger around the right trigger axis.

        The trigger is true when the axis value is less than
        ``threshold``. The threshold should be in the range [0, 1],
        where 0 is the unpressed state. By default, the threshold is 0.5
        and the scheduler's default event loop is used.

        :threshold: Maximum axis value for the trigger to be true.

        :loop: Event loop to attach the trigger to.

        :returns: A trigger that is true when the left trigger axis
            exceeds the provided threshold.
        """
        return self.axis_less_than(Axis.LEFT_TRIGGER, threshold, loop)

    def get_left_x(self):
        """Get the X axis value on the left side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    @property
    def left_x(self):
        """The X axis value on the left side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_left_y(self):
        """Get the Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_y()

    @property
    def left_y(self):
        """Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_right_x(self):
        """Get the X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    @property
    def right_x(self):
        """X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    def get_right_y(self):
        """Get the Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    @property
    def right_y(self):
        """Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``NiDsXboxController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    def get_a_down(self) -> bool:
        """Get the value of the A button on the controller."""
        return self._controller.get_a_button()

    @property
    def a_down(self) -> bool:
        """The value of the A button on the controller."""
        return self._controller.get_a_button()

    def get_a_button_pressed(self) -> bool:
        """Whether the A button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_a_button_pressed()

    @property
    def is_a_pressed(self) -> bool:
        """Whether the A button was pressed since the last check."""
        return self._controller.get_a_button_pressed()

    def get_a_released(self) -> bool:
        """Whether the A button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_a_button_released()

    @property
    def is_a_released(self) -> bool:
        """Whether the A button was released since the last check."""
        return self._controller.get_a_button_released()

    def get_b_down(self) -> bool:
        """Read the value of the B button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_b_button()

    @property
    def b_down(self) -> bool:
        """The value of the B button on the controller."""
        return self._controller.get_b_button()

    def get_b_pressed(self) -> bool:
        """Whether the B button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_b_button_pressed()

    @property
    def is_b_pressed(self) -> bool:
        """Whether the B button was pressed since the last check."""
        return self._controller.get_b_button_pressed()

    def get_b_released(self) -> bool:
        """Whether the B button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_b_button_released()

    @property
    def is_b_released(self) -> bool:
        """Whether the B button was released since the last check."""
        return self._controller.get_b_button_released()

    def get_x_down(self) -> bool:
        """Get the value of the X button on the controller."""
        return self._controller.get_x_button()

    @property
    def x_down(self) -> bool:
        """The value of the X button on the controller."""
        return self._controller.get_x_button()

    def get_x_pressed(self) -> bool:
        """Whether the X button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_x_button_pressed()

    @property
    def is_x_pressed(self) -> bool:
        """Whether the X button was pressed since the last check."""
        return self._controller.get_x_button_pressed()

    def get_x_released(self) -> bool:
        """Whether the X button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_x_button_released()

    @property
    def is_x_released(self) -> bool:
        """Whether the X button was released since the last check."""
        return self._controller.get_x_button_released()

    def get_y_down(self) -> bool:
        """Read the value of the Y button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_y_button()

    @property
    def y_down(self) -> bool:
        """The value of the Y button on the controller."""
        return self._controller.get_y_button()

    def get_y_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_y_button_pressed()

    @property
    def is_y_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check."""
        return self._controller.get_y_button_pressed()

    def get_y_released(self) -> bool:
        """Whether the Y button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_y_button_released()

    @property
    def is_y_released(self) -> bool:
        """Whether the Y button was released since the last check."""
        return self._controller.get_y_button_released()

    @property
    def left_bumper_button_down(self) -> bool:
        """The value of the Left bumper button on the controller."""
        return self._controller.get_left_bumper_button()

    def get_left_bumper_button_pressed(self) -> bool:
        """Whether the Left bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_left_bumper_button_pressed()

    @property
    def left_bumper_button_pressed(self) -> bool:
        return self._controller.get_left_bumper_button_pressed()

    def get_left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_left_bumper_button_released()

    @property
    def left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check."""
        return self._controller.get_left_bumper_button_released()

    def get_right_bumper_button(self) -> bool:
        """Read the value of the Right bumper button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_right_bumper_button()

    @property
    def right_bumper_button_down(self) -> bool:
        """The value of the Right bumper button on the controller."""
        return self._controller.get_right_bumper_button()

    def get_right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_right_bumper_button_pressed()

    @property
    def right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check."""
        return self._controller.get_right_bumper_button_pressed()

    def get_right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_right_bumper_button_released()

    @property
    def right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last
        check."""
        return self._controller.get_right_bumper_button_released()
