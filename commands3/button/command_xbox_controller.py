from typing import SupportsIndex, SupportsInt

from wpilib import GenericHID, XboxController

from commands3.button import CommandGenericHID
from commands3.event_loop import EventLoop
from commands3.scheduler import Scheduler

Axis = XboxController.Axis
Button = XboxController.Button
RumbleType = GenericHID.RumbleType


class CommandXboxController:
    """A version of ``XboxController`` with ``Trigger`` factories for command-
    based use.

    See ``XboxController``.
    """

    def __init__(
        self,
        controller: XboxController | SupportsInt | SupportsIndex,
        *,
        scheduler: Scheduler | None = None,
    ):
        """Construct an instance of XboxController.

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

        if isinstance(controller, XboxController):
            self._controller = controller
        elif isinstance(gamepad, SupportsInt | SupportsIndex):
            self._controller = XboxController(port)
        else:
            raise TypeError("gamepad must be a port or a XboxController.")

        self._hid = CommandGenericHID(self._controller.get_hid(), scheduler=scheduler)

    def get_hid(self) -> CommandGenericHID:
        """Get the underlying ``CommandGenericHID`` object."""
        return self._hid

    @property
    def hid(self) -> CommandGenericHID:
        """The underlying ``CommandGenericHID`` object."""
        return self._hid

    def get_controller(self):
        """Get the underlying ``XboxController`` object."""
        return self._controller

    @property
    def gamepad(self) -> XboxController:
        """The underlying ``XboxController`` object."""
        return self._controller

    def _get_button(
        self, btn: Button, inverted: bool = False, loop: EventLoop | None = None
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

    def dpad_up(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the D-pad up button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad up button's digital
            signal.
        """
        return self._get_button(Button.DPAD_UP, inverted, loop)

    def dpad_down(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the D-pad down button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad down button's digital
            signal.
        """
        return self._get_button(Button.DPAD_DOWN, inverted, loop)

    def dpad_left(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the D-pad left button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad left button's digital
            signal.
        """
        return self._get_button(Button.DPAD_LEFT, inverted, loop)

    def dpad_right(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the D-pad right button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad right button's
            digital signal.
        """
        return self._get_button(Button.DPAD_RIGHT, inverted, loop)

    def a(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the A button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Down button's
            digital signal attached to the given loop.
        """
        return self._hid.button(Button.A.value, inverted, loop)

    def a_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the A button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the A button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.A.value, loop)

    def a_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the A button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the A button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.A.value, loop)

    def b(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the B button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button(Button.B.value, inverted, loop)

    def b_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the B button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.B.value, loop)

    def b_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the B button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the B button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.B.value, loop)

    def x(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the X button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button(Button.X.value, inverted, loop)

    def x_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the X button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.X.value, loop)

    def x_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the X button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the X button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.X.value, loop)

    def y(self, inverted: bool = False, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance around the Y button's digital signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Up button's
            digital signal attached to the given loop.
        """
        return self._hid.button(Button.Y.value, inverted, loop)

    def y_pressed(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the Y button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Y button's digital
            signal attached to the given loop.
        """
        return self._hid.button_pressed(Button.Y.value, loop)

    def y_released(self, loop: EventLoop | None = None) -> BooleanEvent:
        """Constructs an event instance that is invoked once when the Y button
        is pressed.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Y button's digital
            signal attached to the given loop.
        """
        return self._hid.button_released(Button.Y.value, loop)

    def axis_greater_than(
        self,
        axis: Axis | SupportsInt | SupportsIndex,
        threshold: float,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the selected axis exceeds a
        threshold."""
        if isinstance(axis, Axis):
            axis = axis.value
        elif isinstance(axis, SupportsInt | SupportsIndex):
            axis = int(axis)
        else:
            raise TypeError("axis must be Axis, SupportsInt, or SupportsIndex")

        event_loop = loop or self._default_loop
        return self._hid.axis_greater_than(axis, threshold, event_loop)

    def axis_less_than(
        self,
        axis: Axis | SupportsInt | SupportsIndex,
        threshold: float,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the selected axis exceeds a
        threshold."""
        if isinstance(axis, Axis):
            axis = axis.value
        elif isinstance(axis, SupportsInt | SupportsIndex):
            axis = int(axis)
        else:
            raise TypeError("axis must be Axis, SupportsInt, or SupportsIndex")

        event_loop = loop or self._default_loop
        return self._hid.axis_less_than(axis, threshold, event_loop)

    def button(
        self,
        btn: Button | SupportsInt | SupportsIndex,
        inverted: bool = False,
        loop: EventLoop | None = None,
    ):
        """Construct a trigger that is true when the button is held down.

        :param btn: The button to check.
        :param inverted: Whether or not to invert the trigger.
        """
        if isinstance(btn, Button):
            btn = btn.value
        elif isinstance(btn, SupportsInt | SupportsIndex):
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
        ``XboxController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    @property
    def left_x(self):
        """The X axis value on the left side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_left_y(self):
        """Get the Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_y()

    @property
    def left_y(self):
        """Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_right_x(self):
        """Get the X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    @property
    def right_x(self):
        """X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    def get_right_y(self):
        """Get the Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    @property
    def right_y(self):
        """Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    def get_left_trigger(self):
        """Get the left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``XboxController.set_left_trigger_deadband()`` to change it.
        """
        return self._controller.get_left_trigger()

    @property
    def left_trigger_pos(self):
        """The left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``XboxController.set_left_trigger_deadband()`` to change it.
        """
        return self._controller.get_left_trigger()

    def get_right_trigger(self):
        """Get the right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_trigger_deadband()`` to change it.
        """
        return self._controller.get_right_trigger()

    @property
    def right_trigger_pos(self):
        """The right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``XboxController.set_right_trigger_deadband()`` to change it.
        """
        return self._controller.get_right_trigger()

    def is_button_down(self, button: XboxController.Button) -> bool:
        """Get the button value.

        This method returns true if the button is being held down at the
        time that this method is being called.

        :param button: The button
        :returns: The state of the button.
        """
        return self._controller.get_button(button)

    def is_button_pressed(self, button: XboxController.Button) -> bool:
        """Whether the button was pressed since the last check.

        This method returns true if the button went from not pressed to
        held down since the last time this method was called. This is
        useful if you only want to call a function once when you press
        the button.

        :param button: The button
        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(button)

    def is_button_released(self, button: XboxController.Button) -> bool:
        """Whether the button was released since the last check.

        This method returns true if the button went from held down to
        not pressed since the last time this method was called. This is
        useful if you only want to call a function once when you release
        the button.

        :param button: The button
        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(button)

    def get_a_down(self) -> bool:
        """Get the value of the A button on the controller."""
        return self._controller.get_button(Button.A)

    @property
    def a_down(self) -> bool:
        """The value of the A button on the controller."""
        return self._controller.get_button(Button.A)

    def get_a_button_pressed(self) -> bool:
        """Whether the A button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.A)

    @property
    def is_a_pressed(self) -> bool:
        """Whether the A button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.A)

    def get_a_released(self) -> bool:
        """Whether the A button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.A)

    @property
    def is_a_released(self) -> bool:
        """Whether the A button was released since the last check."""
        return self._controller.get_button_released(Button.A)

    def get_b_down(self) -> bool:
        """Read the value of the B button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.B)

    @property
    def b_down(self) -> bool:
        """The value of the B button on the controller."""
        return self._controller.get_button(Button.B)

    def get_b_pressed(self) -> bool:
        """Whether the B button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.B)

    @property
    def is_b_pressed(self) -> bool:
        """Whether the B button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.B)

    def get_b_released(self) -> bool:
        """Whether the B button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.B)

    @property
    def is_b_released(self) -> bool:
        """Whether the B button was released since the last check."""
        return self._controller.get_button_released(Button.B)

    def get_x_down(self) -> bool:
        """Get the value of the X button on the controller."""
        return self._controller.get_button(Button.X)

    @property
    def x_down(self) -> bool:
        """The value of the X button on the controller."""
        return self._controller.get_button(Button.X)

    def get_x_pressed(self) -> bool:
        """Whether the X button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.X)

    @property
    def is_x_pressed(self) -> bool:
        """Whether the X button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.X)

    def get_x_released(self) -> bool:
        """Whether the X button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.X)

    @property
    def is_x_released(self) -> bool:
        """Whether the X button was released since the last check."""
        return self._controller.get_button_released(Button.X)

    def get_y_down(self) -> bool:
        """Read the value of the Y button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.Y)

    @property
    def y_down(self) -> bool:
        """The value of the Y button on the controller."""
        return self._controller.get_button(Button.Y)

    def get_y_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.Y)

    @property
    def is_y_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.Y)

    def get_y_released(self) -> bool:
        """Whether the Y button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.Y)

    @property
    def is_y_released(self) -> bool:
        """Whether the Y button was released since the last check."""
        return self._controller.get_button_released(Button.Y)

    def get_view_button(self) -> bool:
        """Read the value of the view button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.VIEW)

    @property
    def view_button_down(self) -> bool:
        """The value of the view button on the controller."""
        return self._controller.get_button(Button.VIEW)

    def get_view_button_pressed(self) -> bool:
        """Whether the view button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.VIEW)

    @property
    def view_button_pressed(self) -> bool:
        """Whether the view button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.VIEW)

    def get_view_button_released(self) -> bool:
        """Whether the view button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.VIEW)

    @property
    def view_button_released(self) -> bool:
        """Whether the view button was released since the last check."""
        return self._controller.get_button_released(Button.VIEW)

    def get_xbox_button(self) -> bool:
        """Read the value of the xbox button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.XBOX)

    @property
    def xbox_button_down(self) -> bool:
        """The value of the xbox button on the controller."""
        return self._controller.get_button(Button.XBOX)

    def get_xbox_button_pressed(self) -> bool:
        """Whether the xbox button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.XBOX)

    @property
    def xbox_button_pressed(self) -> bool:
        """Whether the xbox button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.XBOX)

    def get_xbox_button_released(self) -> bool:
        """Whether the xbox button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.XBOX)

    @property
    def xbox_button_released(self) -> bool:
        """Whether the xbox button was released since the last check."""
        return self._controller.get_button_released(Button.XBOX)

    def get_left_stick_button(self) -> bool:
        """Read the value of the Left stick button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_STICK)

    @property
    def left_stick_button_down(self) -> bool:
        """The value of the Left stick button on the controller."""
        return self._controller.get_button(Button.LEFT_STICK)

    def get_left_stick_button_pressed(self) -> bool:
        """Whether the Left stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_STICK)

    @property
    def left_stick_button_pressed(self) -> bool:
        """Whether the Left stick button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.LEFT_STICK)

    def get_left_stick_button_released(self) -> bool:
        """Whether the Left stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_STICK)

    @property
    def left_stick_button_released(self) -> bool:
        """Whether the Left stick button was released since the last check."""
        return self._controller.get_button_released(Button.LEFT_STICK)

    def get_right_stick_button(self) -> bool:
        """Read the value of the Right stick button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_STICK)

    @property
    def right_stick_button_down(self) -> bool:
        """The value of the Right stick button on the controller."""
        return self._controller.get_button(Button.RIGHT_STICK)

    def get_right_stick_button_pressed(self) -> bool:
        """Whether the Right stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_STICK)

    @property
    def right_stick_button_pressed(self) -> bool:
        """Whether the Right stick button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.RIGHT_STICK)

    def get_right_stick_button_released(self) -> bool:
        """Whether the Right stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_STICK)

    @property
    def right_stick_button_released(self) -> bool:
        """Whether the Right stick button was released since the last check."""
        return self._controller.get_button_released(Button.RIGHT_STICK)

    def get_left_bumper_button(self) -> bool:
        """Read the value of the Left bumper button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_down(self) -> bool:
        """The value of the Left bumper button on the controller."""
        return self._controller.get_button(Button.LEFT_BUMPER)

    def get_left_bumper_button_pressed(self) -> bool:
        """Whether the Left bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_pressed(self) -> bool:
        """Whether the Left bumper button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.LEFT_BUMPER)

    def get_left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check."""
        return self._controller.get_button_released(Button.LEFT_BUMPER)

    def get_right_bumper_button(self) -> bool:
        """Read the value of the Right bumper button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_down(self) -> bool:
        """The value of the Right bumper button on the controller."""
        return self._controller.get_button(Button.RIGHT_BUMPER)

    def get_right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.RIGHT_BUMPER)

    def get_right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_BUMPER)

    def get_dpad_up_button(self) -> bool:
        """Read the value of the D-pad up button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_UP)

    @property
    def dpad_up_button_down(self) -> bool:
        """The value of the D-pad up button on the controller."""
        return self._controller.get_button(Button.DPAD_UP)

    def get_dpad_up_button_pressed(self) -> bool:
        """Whether the D-pad up button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.DPAD_UP)

    @property
    def dpad_up_button_pressed(self) -> bool:
        """Whether the D-pad up button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.DPAD_UP)

    def get_dpad_up_button_released(self) -> bool:
        """Whether the D-pad up button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.DPAD_UP)

    @property
    def dpad_up_button_released(self) -> bool:
        """Whether the D-pad up button was released since the last check."""
        return self._controller.get_button_released(Button.DPAD_UP)

    def get_dpad_down_button(self) -> bool:
        """Read the value of the D-pad down button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_DOWN)

    @property
    def dpad_down_button_down(self) -> bool:
        """The value of the D-pad down button on the controller."""
        return self._controller.get_button(Button.DPAD_DOWN)

    def get_dpad_down_button_pressed(self) -> bool:
        """Whether the D-pad down button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.DPAD_DOWN)

    @property
    def dpad_down_button_pressed(self) -> bool:
        """Whether the D-pad down button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.DPAD_DOWN)

    def get_dpad_down_button_released(self) -> bool:
        """Whether the D-pad down button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.DPAD_DOWN)

    @property
    def dpad_down_button_released(self) -> bool:
        """Whether the D-pad down button was released since the last check."""
        return self._controller.get_button_released(Button.DPAD_DOWN)

    def get_dpad_left_button(self) -> bool:
        """Read the value of the D-pad left button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_LEFT)

    @property
    def dpad_left_button_down(self) -> bool:
        """The value of the D-pad left button on the controller."""
        return self._controller.get_button(Button.DPAD_LEFT)

    def get_dpad_left_button_pressed(self) -> bool:
        """Whether the D-pad left button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.DPAD_LEFT)

    @property
    def dpad_left_button_pressed(self) -> bool:
        """Whether the D-pad left button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.DPAD_LEFT)

    def get_dpad_left_button_released(self) -> bool:
        """Whether the D-pad left button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.DPAD_LEFT)

    @property
    def dpad_left_button_released(self) -> bool:
        """Whether the D-pad left button was released since the last check."""
        return self._controller.get_button_released(Button.DPAD_LEFT)

    def get_dpad_right_button(self) -> bool:
        """Read the value of the D-pad right button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_down(self) -> bool:
        """The value of the D-pad right button on the controller."""
        return self._controller.get_button(Button.DPAD_RIGHT)

    def get_dpad_right_button_pressed(self) -> bool:
        """Whether the D-pad right button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_pressed(self) -> bool:
        """Whether the D-pad right button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.DPAD_RIGHT)

    def get_dpad_right_button_released(self) -> bool:
        """Whether the D-pad right button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_released(self) -> bool:
        """Whether the D-pad right button was released since the last check."""
        return self._controller.get_button_released(Button.DPAD_RIGHT)

    def set_left_x_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the left X axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._controller.set_left_x_deadband(deadband)

    def set_left_y_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the left Y axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._controller.set_left_y_deadband(deadband)

    def set_right_x_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the right X axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._controller.set_right_x_deadband(deadband)

    def set_right_y_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the right Y axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._controller.set_right_y_deadband(deadband)
