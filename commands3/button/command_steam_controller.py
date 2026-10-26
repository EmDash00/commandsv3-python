from typing import SupportsIndex, SupportsInt

from wpilib import SteamController
from wpilib._wpilib import GenericHID

from commands3.button import CommandGenericHID
from commands3.event_loop import EventLoop
from commands3.scheduler import Scheduler

Axis = SteamController.Axis
Button = SteamController.Button
RumbleType = GenericHID.RumbleType


class CommandSteamController:
    """A version of ``SteamController`` with ``Trigger`` factories for command-
    based use.

    See ``SteamController``.
    """

    def __init__(
        self,
        controller: GenericHID | SupportsInt | SupportsIndex,
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

        if isinstance(gamepad, GenericHID | SupportsInt | SupportsIndex):
            self._controller = SteamController(controller)
        else:
            raise TypeError("gamepad must be a port or a SteamController.")

        self._hid = CommandGenericHID(self._controller.get_hid(), scheduler=scheduler)

    def get_hid(self) -> CommandGenericHID:
        """Get the underlying ``CommandGenericHID`` object."""
        return self._hid

    @property
    def hid(self) -> CommandGenericHID:
        """The underlying ``CommandGenericHID`` object."""
        return self._hid

    def get_controller(self):
        """Get the underlying ``SteamController`` object."""
        return self._controller

    @property
    def gamepad(self) -> SteamController:
        """The underlying ``SteamController`` object."""
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

    def a(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the A button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad up button's digital
            signal.
        """
        return self._get_button(Button.A, inverted, loop)

    def b(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the B button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad down button's digital
            signal.
        """
        return self._get_button(Button.B, inverted, loop)

    def x(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the X button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad left button's digital
            signal.
        """
        return self._get_button(Button.X, inverted, loop)

    def y(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Y button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the D-pad right button's
            digital signal.
        """
        return self._get_button(Button.Y, inverted, loop)

    def dpad_down(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the dpad down button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the dpad down button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.DPAD_DOWN, inverted, loop)

    def dpad_left(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the dpad left button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the dpad left button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.DPAD_UP, inverted, loop)

    def dpad_right(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the dpad right button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the dpad right button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.DPAD_RIGHT, inverted, loop)

    def dpad_up(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the dpad up button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the dpad up button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.DPAD_LEFT, inverted, loop)

    def left_grip_touch(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the left grip touch button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left grip touch button's
            digital signal.
        """
        return self._get_button(Button.LEFT_GRIP_TOUCH, inverted, loop)

    def right_grip_touch(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right grip touch button's digital
        signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left grip touch button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_GRIP_TOUCH, inverted, loop)

    def right_paddle1(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right Paddle 1 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the right Paddle 1 button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_PADDLE_1, inverted, loop)

    def left_paddle1(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the left Paddle 1 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left Paddle 1 button's
            digital signal.
        """
        return self._get_button(Button.LEFT_PADDLE_1, inverted, loop)

    def right_paddle2(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right Paddle 2 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the right Paddle 2 button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_PADDLE_2, inverted, loop)

    def left_paddle2(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the left Paddle 2 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the left Paddle 2 button's
            digital signal.
        """
        return self._get_button(Button.LEFT_PADDLE_2, inverted, loop)

    def left_touchpad(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Touchpad button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Touchpad button's digital
            signal.
        """
        return self._get_button(Button.LEFT_TOUCHPAD, inverted, loop)

    def right_touchpad(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the right touchpad button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Touchpad button's digital
            signal.
        """
        return self._get_button(Button.RIGHT_TOUCHPAD, inverted, loop)

    def menu(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the menu button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 2 button's
            digital signal.
        """
        return self._get_button(Button.MENU, inverted, loop)

    def view(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 3 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 3 button's
            digital signal.
        """
        return self._get_button(Button.VIEW, inverted, loop)

    def qam(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 4 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 4 button's
            digital signal.
        """
        return self._get_button(Button.QAM, inverted, loop)

    def left_stick_touch(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 5 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 5 button's
            digital signal.
        """
        return self._get_button(Button.LEFT_STICK_TOUCH, inverted, loop)

    def right_stick_touch(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 6 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 6 button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_STICK_TOUCH, inverted, loop)

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

        :threshold: Maximium axis value for the trigger to be true.

        :loop: Event loop to attach the trigger to.

        :returns: A trigger that is true when the left trigger axis
            exceeds the provided threshold.
        """
        return self.axis_less_than(Axis.LEFT_TRIGGER, threshold, loop)

    def get_left_x(self):
        """Get the X axis value on the left side of the controller.

        right is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    @property
    def left_x(self):
        """The X axis value on the left side of the controller.

        right is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_x_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_left_y(self):
        """Get the Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_y()

    @property
    def left_y(self):
        """Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_y_deadband()`` to change it.
        """
        return self._controller.get_left_x()

    def get_right_x(self):
        """Get the X-axis value on the right side of the controller.

        right is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    @property
    def right_x(self):
        """X-axis value on the right side of the controller.

        right is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_x_deadband()`` to change it.
        """
        return self._controller.get_right_x()

    def get_right_y(self):
        """Get the Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    @property
    def right_y(self):
        """Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_y_deadband()`` to change it.
        """
        return self._controller.get_right_y()

    def get_left_trigger(self):
        """Get the left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_trigger_deadband()`` to change it.
        """
        return self._controller.get_left_trigger()

    @property
    def left_trigger_pos(self):
        """The left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``SteamController.set_left_trigger_deadband()`` to change it.
        """
        return self._controller.get_left_trigger()

    def get_right_trigger(self):
        """Get the right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_trigger_deadband()`` to change it.
        """
        return self._controller.get_right_trigger()

    @property
    def right_trigger_pos(self):
        """The right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``SteamController.set_right_trigger_deadband()`` to change it.
        """
        return self._controller.get_right_trigger()

    def get_button(self, button: SteamController.Button) -> bool:
        """Get the button value.

        This method returns true if the button is being held down at the
        time that this method is being called.

        :param button: The button
        :returns: The state of the button.
        """
        return self._controller.get_button(button)

    def get_button_pressed(self, button: SteamController.Button) -> bool:
        """Whether the button was pressed since the last check.

        This method returns true if the button went from not pressed to
        held down since the last time this method was called. This is
        useful if you only want to call a function once when you press
        the button.

        :param button: The button
        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(button)

    def get_button_released(self, button: SteamController.Button) -> bool:
        """Whether the button was released since the last check.

        This method returns true if the button went from held down to
        not pressed since the last time this method was called. This is
        useful if you only want to call a function once when you release
        the button.

        :param button: The button
        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(button)

    def get_down_button(self) -> bool:
        """Read the value of the dpad down button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_DOWN)

    @property
    def a_button_down(self) -> bool:
        """The value of the dpad down button on the controller."""
        return self._controller.get_button(Button.A)

    def get_a_button_pressed(self) -> bool:
        """Whether the A button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.A)

    @property
    def a_button_pressed(self) -> bool:
        """Whether the A button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.A)

    def get_a_button_released(self) -> bool:
        """Whether the A button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.A)

    @property
    def a_button_released(self) -> bool:
        """Whether the A button was released since the last check."""
        return self._controller.get_button_released(Button.A)

    def get_b_button(self) -> bool:
        """Read the value of the B button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.B)

    @property
    def b_button_down(self) -> bool:
        """The value of the B button on the controller."""
        return self._controller.get_button(Button.B)

    def get_b_button_pressed(self) -> bool:
        """Whether the B button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.B)

    @property
    def b_button_pressed(self) -> bool:
        """Whether the B button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.B)

    def get_b_button_released(self) -> bool:
        """Whether the B button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.B)

    @property
    def b_button_released(self) -> bool:
        """Whether the B button was released since the last check."""
        return self._controller.get_button_released(Button.B)

    def get_face_left_button(self) -> bool:
        """Read the value of the dpad left button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.DPAD_LEFT)

    @property
    def x_button_down(self) -> bool:
        """The value of the x button on the controller."""
        return self._controller.get_button(Button.X)

    def get_x_button_pressed(self) -> bool:
        """Whether the x button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.X)

    @property
    def x_button_pressed(self) -> bool:
        """Whether the x button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.X)

    def get_x_button_released(self) -> bool:
        """Whether the x button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.X)

    @property
    def x_button_released(self) -> bool:
        """Whether the x button was released since the last check."""
        return self._controller.get_button_released(Button.X)

    def get_face_up_button(self) -> bool:
        """Read the value of the Y button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.Y)

    @property
    def y_button_down(self) -> bool:
        """The value of the Y button on the controller."""
        return self._controller.get_button(Button.Y)

    def get_y_button_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.Y)

    @property
    def y_button_pressed(self) -> bool:
        """Whether the Y button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.Y)

    def get_y_button_released(self) -> bool:
        """Whether the Y button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.Y)

    @property
    def y_button_released(self) -> bool:
        """Whether the Y button was released since the last check."""
        return self._controller.get_button_released(Button.Y)

    def get_left_stick_button(self) -> bool:
        """Read the value of the left stick button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_STICK)

    @property
    def left_stick_button_down(self) -> bool:
        """The value of the left stick button on the controller."""
        return self._controller.get_button(Button.LEFT_STICK)

    def get_left_stick_button_pressed(self) -> bool:
        """Whether the left stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_STICK)

    @property
    def left_stick_button_pressed(self) -> bool:
        """Whether the left stick button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.LEFT_STICK)

    def get_left_stick_button_released(self) -> bool:
        """Whether the left stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_STICK)

    @property
    def left_stick_button_released(self) -> bool:
        """Whether the left stick button was released since the last check."""
        return self._controller.get_button_released(Button.LEFT_STICK)

    def get_right_stick_button(self) -> bool:
        """Read the value of the right stick button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_STICK)

    @property
    def right_stick_button_down(self) -> bool:
        """The value of the right stick button on the controller."""
        return self._controller.get_button(Button.RIGHT_STICK)

    def get_right_stick_button_pressed(self) -> bool:
        """Whether the right stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_STICK)

    @property
    def right_stick_button_pressed(self) -> bool:
        """Whether the right stick button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.RIGHT_STICK)

    def get_right_stick_button_released(self) -> bool:
        """Whether the right stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_STICK)

    @property
    def right_stick_button_released(self) -> bool:
        """Whether the right stick button was released since the last check."""
        return self._controller.get_button_released(Button.RIGHT_STICK)

    def get_left_bumper_button(self) -> bool:
        """Read the value of the left bumper button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_down(self) -> bool:
        """The value of the left bumper button on the controller."""
        return self._controller.get_button(Button.LEFT_BUMPER)

    def get_left_bumper_button_pressed(self) -> bool:
        """Whether the left bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_pressed(self) -> bool:
        """Whether the left bumper button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.LEFT_BUMPER)

    def get_left_bumper_button_released(self) -> bool:
        """Whether the left bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_released(self) -> bool:
        """Whether the left bumper button was released since the last check."""
        return self._controller.get_button_released(Button.LEFT_BUMPER)

    def get_right_bumper_button(self) -> bool:
        """Read the value of the right bumper button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_down(self) -> bool:
        """The value of the right bumper button on the controller."""
        return self._controller.get_button(Button.RIGHT_BUMPER)

    def get_right_bumper_button_pressed(self) -> bool:
        """Whether the right bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_pressed(self) -> bool:
        """Whether the right bumper button was pressed since the last check."""
        return self._controller.get_button_pressed(Button.RIGHT_BUMPER)

    def get_right_bumper_button_released(self) -> bool:
        """Whether the right bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_released(self) -> bool:
        """Whether the right bumper button was released since the last
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

    def get_left_grip_touch_button(self) -> bool:
        """Read the value of the left grip touch button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_GRIP_TOUCH)

    @property
    def left_grip_touch_button_down(self) -> bool:
        """The value of the left grip touch button on the controller."""
        return self._controller.get_button(Button.LEFT_GRIP_TOUCH)

    def get_left_grip_touch_button_pressed(self) -> bool:
        """Whether the left grip touch button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_GRIP_TOUCH)

    @property
    def left_grip_touch_button_pressed(self) -> bool:
        """Whether the left grip touch button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.LEFT_GRIP_TOUCH)

    def get_left_grip_touch_button_released(self) -> bool:
        """Whether the left grip touch button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_GRIP_TOUCH)

    @property
    def left_grip_touch_button_released(self) -> bool:
        """Whether the left grip touch button was released since the last
        check."""
        return self._controller.get_button_released(Button.LEFT_GRIP_TOUCH)

    @property
    def right_grip_touch_button_down(self) -> bool:
        """The value of the right grip touch button on the controller."""
        return self._controller.get_button(Button.RIGHT_GRIP_TOUCH)

    def get_right_grip_touch_button_pressed(self) -> bool:
        """Whether the right grip touch button was pressed since the last
        check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_GRIP_TOUCH)

    @property
    def right_grip_touch_button_pressed(self) -> bool:
        """Whether the right grip touch button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.RIGHT_GRIP_TOUCH)

    def get_right_grip_touch_button_released(self) -> bool:
        """Whether the right grip touch button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_GRIP_TOUCH)

    @property
    def right_grip_touch_button_released(self) -> bool:
        """Whether the right grip touch button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_GRIP_TOUCH)

    def get_right_paddle1_button(self) -> bool:
        """Read the value of the right Paddle 1 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_down(self) -> bool:
        """The value of the right Paddle 1 button on the controller."""
        return self._controller.get_button(Button.RIGHT_PADDLE_1)

    def get_right_paddle1_button_pressed(self) -> bool:
        """Whether the right Paddle 1 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_pressed(self) -> bool:
        """Whether the right Paddle 1 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.RIGHT_PADDLE_1)

    def get_right_paddle1_button_released(self) -> bool:
        """Whether the right Paddle 1 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_released(self) -> bool:
        """Whether the right Paddle 1 button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_PADDLE_1)

    def get_left_paddle1_button(self) -> bool:
        """Read the value of the left Paddle 1 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_down(self) -> bool:
        """The value of the left Paddle 1 button on the controller."""
        return self._controller.get_button(Button.LEFT_PADDLE_1)

    def get_left_paddle1_button_pressed(self) -> bool:
        """Whether the left Paddle 1 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_pressed(self) -> bool:
        """Whether the left Paddle 1 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.LEFT_PADDLE_1)

    def get_left_paddle1_button_released(self) -> bool:
        """Whether the left Paddle 1 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_released(self) -> bool:
        """Whether the left Paddle 1 button was released since the last
        check."""
        return self._controller.get_button_released(Button.LEFT_PADDLE_1)

    def get_right_paddle2_button(self) -> bool:
        """Read the value of the right Paddle 2 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_down(self) -> bool:
        """The value of the right Paddle 2 button on the controller."""
        return self._controller.get_button(Button.RIGHT_PADDLE_2)

    def get_right_paddle2_button_pressed(self) -> bool:
        """Whether the right Paddle 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_pressed(self) -> bool:
        """Whether the right Paddle 2 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.RIGHT_PADDLE_2)

    def get_right_paddle2_button_released(self) -> bool:
        """Whether the right Paddle 2 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_released(self) -> bool:
        """Whether the right Paddle 2 button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_PADDLE_2)

    def get_left_paddle2_button(self) -> bool:
        """Read the value of the left Paddle 2 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_down(self) -> bool:
        """The value of the left Paddle 2 button on the controller."""
        return self._controller.get_button(Button.LEFT_PADDLE_2)

    def get_left_paddle2_button_pressed(self) -> bool:
        """Whether the left Paddle 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_pressed(self) -> bool:
        """Whether the left Paddle 2 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.LEFT_PADDLE_2)

    def get_left_paddle2_button_released(self) -> bool:
        """Whether the left Paddle 2 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_released(self) -> bool:
        """Whether the left Paddle 2 button was released since the last
        check."""
        return self._controller.get_button_released(Button.LEFT_PADDLE_2)

    def get_left_touchpad_button(self) -> bool:
        """Read the value of the left touchpad button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_TOUCHPAD)

    def get_right_touchpad_button(self) -> bool:
        """Read the value of the left touchpad button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_TOUCHPAD)

    @property
    def left_touchpad_button_down(self) -> bool:
        """The value of the left touchpad button on the controller."""
        return self._controller.get_button(Button.LEFT_TOUCHPAD)

    def get_left_touchpad_button_pressed(self) -> bool:
        """Whether the left touchpad button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_TOUCHPAD)

    @property
    def left_touchpad_button_pressed(self) -> bool:
        """Whether the left touchpad button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.LEFT_TOUCHPAD)

    def get_left_touchpad_button_released(self) -> bool:
        """Whether the left touchpad button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_TOUCHPAD)

    @property
    def left_touchpad_button_released(self) -> bool:
        """Whether the left touchpad button was released since the last
        check."""
        return self._controller.get_button_released(Button.LEFT_TOUCHPAD)

    @property
    def right_touchpad_button_down(self) -> bool:
        """The value of the right touchpad button on the controller."""
        return self._controller.get_button(Button.RIGHT_TOUCHPAD)

    def get_right_touchpad_button_pressed(self) -> bool:
        """Whether the right touchpad button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_TOUCHPAD)

    @property
    def right_touchpad_button_pressed(self) -> bool:
        """Whether the right touchpad button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.RIGHT_TOUCHPAD)

    def get_right_touchpad_button_released(self) -> bool:
        """Whether the right touchpad button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_TOUCHPAD)

    @property
    def right_touchpad_button_released(self) -> bool:
        """Whether the right touchpad button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_TOUCHPAD)

    def get_menu_button(self) -> bool:
        """Read the value of the Miscellaneous 2 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.MENU)

    @property
    def menu_button_down(self) -> bool:
        """The value of the Miscellaneous 2 button on the controller."""
        return self._controller.get_button(Button.MENU)

    def get_menu_button_pressed(self) -> bool:
        """Whether the Miscellaneous 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.MENU)

    @property
    def menu_button_pressed(self) -> bool:
        """Whether the Miscellaneous 2 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.MENU)

    def get_menu_button_released(self) -> bool:
        """Whether the Miscellaneous 2 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.MENU)

    @property
    def menu_button_released(self) -> bool:
        """Whether the Miscellaneous 2 button was released since the last
        check."""
        return self._controller.get_button_released(Button.MENU)

    def get_view_button(self) -> bool:
        """Read the value of the Miscellaneous 3 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.VIEW)

    @property
    def view_button_down(self) -> bool:
        """The value of the Miscellaneous 3 button on the controller."""
        return self._controller.get_button(Button.VIEW)

    def get_view_button_pressed(self) -> bool:
        """Whether the Miscellaneous 3 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.VIEW)

    @property
    def view_button_pressed(self) -> bool:
        """Whether the Miscellaneous 3 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.VIEW)

    def get_view_button_released(self) -> bool:
        """Whether the Miscellaneous 3 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.VIEW)

    @property
    def view_button_released(self) -> bool:
        """Whether the Miscellaneous 3 button was released since the last
        check."""
        return self._controller.get_button_released(Button.VIEW)

    def get_qam_button(self) -> bool:
        """Read the value of the Miscellaneous 4 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.QAM)

    @property
    def qam_button_down(self) -> bool:
        """The value of the Miscellaneous 4 button on the controller."""
        return self._controller.get_button(Button.QAM)

    def get_qam_button_pressed(self) -> bool:
        """Whether the Miscellaneous 4 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.QAM)

    @property
    def qam_button_pressed(self) -> bool:
        """Whether the Miscellaneous 4 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.QAM)

    def get_qam_button_released(self) -> bool:
        """Whether the Miscellaneous 4 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.QAM)

    @property
    def qam_button_released(self) -> bool:
        """Whether the Miscellaneous 4 button was released since the last
        check."""
        return self._controller.get_button_released(Button.QAM)

    def get_left_stick_touch_button(self) -> bool:
        """Read the value of the Miscellaneous 5 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.LEFT_STICK_TOUCH)

    @property
    def left_stick_touch_button_down(self) -> bool:
        """The value of the Miscellaneous 5 button on the controller."""
        return self._controller.get_button(Button.LEFT_STICK_TOUCH)

    def get_left_stick_touch_button_pressed(self) -> bool:
        """Whether the Miscellaneous 5 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.LEFT_STICK_TOUCH)

    @property
    def left_stick_touch_button_pressed(self) -> bool:
        """Whether the Miscellaneous 5 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.LEFT_STICK_TOUCH)

    def get_left_stick_touch_button_released(self) -> bool:
        """Whether the Miscellaneous 5 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.LEFT_STICK_TOUCH)

    @property
    def left_stick_touch_button_released(self) -> bool:
        """Whether the Miscellaneous 5 button was released since the last
        check."""
        return self._controller.get_button_released(Button.LEFT_STICK_TOUCH)

    def get_right_stick_touch_button(self) -> bool:
        """Read the value of the Miscellaneous 6 button on the controller.

        :returns: The state of the button.
        """
        return self._controller.get_button(Button.RIGHT_STICK_TOUCH)

    @property
    def right_stick_touch_button_down(self) -> bool:
        """The value of the Miscellaneous 6 button on the controller."""
        return self._controller.get_button(Button.RIGHT_STICK_TOUCH)

    def get_right_stick_touch_button_pressed(self) -> bool:
        """Whether the Miscellaneous 6 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._controller.get_button_pressed(Button.RIGHT_STICK_TOUCH)

    @property
    def right_stick_touch_button_pressed(self) -> bool:
        """Whether the Miscellaneous 6 button was pressed since the last
        check."""
        return self._controller.get_button_pressed(Button.RIGHT_STICK_TOUCH)

    def get_right_stick_touch_button_released(self) -> bool:
        """Whether the Miscellaneous 6 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._controller.get_button_released(Button.RIGHT_STICK_TOUCH)

    @property
    def right_stick_touch_button_released(self) -> bool:
        """Whether the Miscellaneous 6 button was released since the last
        check."""
        return self._controller.get_button_released(Button.RIGHT_STICK_TOUCH)

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
