from typing import SupportsIndex, SupportsInt

from wpilib import DriverStation, Gamepad
from wpilib._wpilib import GenericHID

from commands3.button import CommandGenericHID
from commands3.event_loop import EventLoop
from commands3.scheduler import Scheduler

Axis = Gamepad.Axis
Button = Gamepad.Button
RumbleType = GenericHID.RumbleType


class CommandGamepad:
    """A version of ``Gamepad`` with ``Trigger`` factories for command-based
    use.

    See ``Gamepad``.
    """

    def __init__(
        self,
        gamepad: Gamepad | SupportsInt | SupportsIndex,
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

        if isinstance(gamepad, Gamepad):
            self._gamepad = gamepad
        elif isinstance(gamepad, SupportsInt | SupportsIndex):
            self._gamepad = DriverStation.get_gamepad(gamepad)
        else:
            raise TypeError("gamepad must be a port or a Gamepad.")

        self._hid = CommandGenericHID(self._gamepad.get_hid(), scheduler=scheduler)

    def get_hid(self) -> CommandGenericHID:
        """Get the underlying ``CommandGenericHID`` object."""
        return self._hid

    @property
    def hid(self) -> CommandGenericHID:
        """The underlying ``CommandGenericHID`` object."""
        return self._hid

    def get_gamepad(self):
        """Get the underlying ``Gamepad`` object."""
        return self._gamepad

    @property
    def gamepad(self) -> Gamepad:
        """The underlying ``Gamepad`` object."""
        return self._gamepad

    def _get_button(
        self, btn: Button, inverted: bool = False, loop: EventLoop | None = None
    ):
        """Build a trigger for a named gamepad button."""
        return self.button(btn, inverted, loop or self._default_loop)

    def back(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Back button's digital signal.

        :param inverted: Whether or not to invert the trigger.
        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :returns: A trigger representing the Back button's digital
            signal.
        """
        return self._get_button(Button.BACK, inverted, loop)

    def guide(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Guide button's digital signal.

        :param inverted: Whether or not to invert the trigger.
        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Guide button's digital
            signal.
        """
        return self._get_button(Button.GUIDE, inverted, loop)

    def start(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Start button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Start button's digital
            signal.
        """
        return self._get_button(Button.START, inverted, loop)

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

    def face_down(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the Face Down button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Down button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.FACE_DOWN, inverted, loop)

    def face_left(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the Face Left button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Left button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.FACE_UP, inverted, loop)

    def face_right(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the Face Right button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Right button's
            digital signal attached to the given loop.
        """
        return self._get_button(Button.FACE_RIGHT, inverted, loop)

    def face_up(
        self, inverted: bool = False, loop: EventLoop | None = None
    ) -> BooleanEvent:
        """Constructs an event instance around the Face Up button's digital
        signal.

        :param loop: the event loop instance to attach the event to.
        :returns: an event instance representing the Face Up button's
            digital signal attached to the given loop.
        """
        self._gamepad.face_up
        return self._get_button(Button.FACE_LEFT, inverted, loop)

    def misc1(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 1 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 1 button's
            digital signal.
        """
        return self._get_button(Button.MISC_1, inverted, loop)

    def right_paddle1(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Right Paddle 1 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Right Paddle 1 button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_PADDLE_1, inverted, loop)

    def left_paddle1(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Left Paddle 1 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Left Paddle 1 button's
            digital signal.
        """
        return self._get_button(Button.LEFT_PADDLE_1, inverted, loop)

    def right_paddle2(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Right Paddle 2 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Right Paddle 2 button's
            digital signal.
        """
        return self._get_button(Button.RIGHT_PADDLE_2, inverted, loop)

    def left_paddle2(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Left Paddle 2 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Left Paddle 2 button's
            digital signal.
        """
        return self._get_button(Button.LEFT_PADDLE_2, inverted, loop)

    def touchpad(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Touchpad button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Touchpad button's digital
            signal.
        """
        return self._get_button(Button.TOUCHPAD, inverted, loop)

    def misc2(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 2 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 2 button's
            digital signal.
        """
        return self._get_button(Button.MISC_2, inverted, loop)

    def misc3(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 3 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 3 button's
            digital signal.
        """
        return self._get_button(Button.MISC_3, inverted, loop)

    def misc4(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 4 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 4 button's
            digital signal.
        """
        return self._get_button(Button.MISC_4, inverted, loop)

    def misc5(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 5 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 5 button's
            digital signal.
        """
        return self._get_button(Button.MISC_5, inverted, loop)

    def misc6(self, inverted: bool = False, loop: EventLoop | None = None):
        """Construct a trigger for the Miscellaneous 6 button's digital signal.

        :param loop: The event loop to attach the trigger to. Defaults
            to this controller's scheduler default event loop.
        :param inverted: Whether or not to invert the trigger.
        :returns: A trigger representing the Miscellaneous 6 button's
            digital signal.
        """
        return self._get_button(Button.MISC_6, inverted, loop)

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

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_x_deadband()`` to change it.
        """
        return self._gamepad.get_left_x()

    @property
    def left_x(self):
        """The X axis value on the left side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_x_deadband()`` to change it.
        """
        return self._gamepad.get_left_x()

    def get_left_y(self):
        """Get the Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_y_deadband()`` to change it.
        """
        return self._gamepad.get_left_y()

    @property
    def left_y(self):
        """Y-axis value on the left side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_y_deadband()`` to change it.
        """
        return self._gamepad.get_left_x()

    def get_right_x(self):
        """Get the X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_x_deadband()`` to change it.
        """
        return self._gamepad.get_right_x()

    @property
    def right_x(self):
        """X-axis value on the right side of the controller.

        Right is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_x_deadband()`` to change it.
        """
        return self._gamepad.get_right_x()

    def get_right_y(self):
        """Get the Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_y_deadband()`` to change it.
        """
        return self._gamepad.get_right_y()

    @property
    def right_y(self):
        """Y-axis value on the right side of the controller.

        Back is positive. A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_y_deadband()`` to change it.
        """
        return self._gamepad.get_right_y()

    def get_left_trigger(self):
        """Get the left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_trigger_deadband()`` to change it.
        """
        return self._gamepad.get_left_trigger()

    @property
    def left_trigger_pos(self):
        """The left trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_left_trigger_deadband()`` to change it.
        """
        return self._gamepad.get_left_trigger()

    def get_right_trigger(self):
        """Get the right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_trigger_deadband()`` to change it.
        """
        return self._gamepad.get_right_trigger()

    @property
    def right_trigger_pos(self):
        """The right trigger value of the controller.

        This axis is in the range [0, 1], rather than the usual [-1, 1].
        A deadband of 0.1 is applied by default. Use
        ``Gamepad.set_right_trigger_deadband()`` to change it.
        """
        return self._gamepad.get_right_trigger()

    def get_button(self, button: Gamepad.Button) -> bool:
        """Get the button value.

        This method returns true if the button is being held down at the
        time that this method is being called.

        :param button: The button
        :returns: The state of the button.
        """
        return self._gamepad.get_button(button)

    def get_button_pressed(self, button: Gamepad.Button) -> bool:
        """Whether the button was pressed since the last check.

        This method returns true if the button went from not pressed to
        held down since the last time this method was called. This is
        useful if you only want to call a function once when you press
        the button.

        :param button: The button
        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(button)

    def get_button_released(self, button: Gamepad.Button) -> bool:
        """Whether the button was released since the last check.

        This method returns true if the button went from held down to
        not pressed since the last time this method was called. This is
        useful if you only want to call a function once when you release
        the button.

        :param button: The button
        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(button)

    def get_back_button(self) -> bool:
        """Read the value of the Back button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.BACK)

    @property
    def back_button_down(self) -> bool:
        """The value of the Back button on the controller."""
        return self._gamepad.get_button(Button.BACK)

    def get_back_button_pressed(self) -> bool:
        """Whether the Back button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.BACK)

    def get_face_down_button(self) -> bool:
        """Read the value of the Face Down button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.FACE_DOWN)

    @property
    def face_down_button_down(self) -> bool:
        """The value of the Face Down button on the controller."""
        return self._gamepad.get_button(Button.FACE_DOWN)

    def get_face_down_button_pressed(self) -> bool:
        """Whether the Face Down button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.FACE_DOWN)

    @property
    def face_down_button_pressed(self) -> bool:
        """Whether the Face Down button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.FACE_DOWN)

    def get_face_down_button_released(self) -> bool:
        """Whether the Face Down button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.FACE_DOWN)

    @property
    def face_down_button_released(self) -> bool:
        """Whether the Face Down button was released since the last check."""
        return self._gamepad.get_button_released(Button.FACE_DOWN)

    def get_face_right_button(self) -> bool:
        """Read the value of the Face Right button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.FACE_RIGHT)

    @property
    def face_right_button_down(self) -> bool:
        """The value of the Face Right button on the controller."""
        return self._gamepad.get_button(Button.FACE_RIGHT)

    def get_face_right_button_pressed(self) -> bool:
        """Whether the Face Right button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.FACE_RIGHT)

    @property
    def face_right_button_pressed(self) -> bool:
        """Whether the Face Right button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.FACE_RIGHT)

    def get_face_right_button_released(self) -> bool:
        """Whether the Face Right button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.FACE_RIGHT)

    @property
    def face_right_button_released(self) -> bool:
        """Whether the Face Right button was released since the last check."""
        return self._gamepad.get_button_released(Button.FACE_RIGHT)

    def get_face_left_button(self) -> bool:
        """Read the value of the Face Left button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.FACE_LEFT)

    @property
    def face_left_button_down(self) -> bool:
        """The value of the Face Left button on the controller."""
        return self._gamepad.get_button(Button.FACE_LEFT)

    def get_face_left_button_pressed(self) -> bool:
        """Whether the Face Left button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.FACE_LEFT)

    @property
    def face_left_button_pressed(self) -> bool:
        """Whether the Face Left button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.FACE_LEFT)

    def get_face_left_button_released(self) -> bool:
        """Whether the Face Left button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.FACE_LEFT)

    @property
    def face_left_button_released(self) -> bool:
        """Whether the Face Left button was released since the last check."""
        return self._gamepad.get_button_released(Button.FACE_LEFT)

    def get_face_up_button(self) -> bool:
        """Read the value of the Face Up button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.FACE_UP)

    @property
    def face_up_button_down(self) -> bool:
        """The value of the Face Up button on the controller."""
        return self._gamepad.get_button(Button.FACE_UP)

    def get_face_up_button_pressed(self) -> bool:
        """Whether the Face Up button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.FACE_UP)

    @property
    def face_up_button_pressed(self) -> bool:
        """Whether the Face Up button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.FACE_UP)

    def get_face_up_button_released(self) -> bool:
        """Whether the Face Up button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.FACE_UP)

    @property
    def face_up_button_released(self) -> bool:
        """Whether the Face Up button was released since the last check."""
        return self._gamepad.get_button_released(Button.FACE_UP)

    def get_guide_button(self) -> bool:
        """Read the value of the Guide button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.GUIDE)

    @property
    def guide_button_down(self) -> bool:
        """The value of the Guide button on the controller."""
        return self._gamepad.get_button(Button.GUIDE)

    def get_guide_button_pressed(self) -> bool:
        """Whether the Guide button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.GUIDE)

    @property
    def guide_button_pressed(self) -> bool:
        """Whether the Guide button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.GUIDE)

    def get_guide_button_released(self) -> bool:
        """Whether the Guide button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.GUIDE)

    @property
    def guide_button_released(self) -> bool:
        """Whether the Guide button was released since the last check."""
        return self._gamepad.get_button_released(Button.GUIDE)

    def get_start_button(self) -> bool:
        """Read the value of the Start button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.START)

    @property
    def start_button_down(self) -> bool:
        """The value of the Start button on the controller."""
        return self._gamepad.get_button(Button.START)

    def get_start_button_pressed(self) -> bool:
        """Whether the Start button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.START)

    @property
    def start_button_pressed(self) -> bool:
        """Whether the Start button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.START)

    def get_start_button_released(self) -> bool:
        """Whether the Start button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.START)

    @property
    def start_button_released(self) -> bool:
        """Whether the Start button was released since the last check."""
        return self._gamepad.get_button_released(Button.START)

    def get_left_stick_button(self) -> bool:
        """Read the value of the Left stick button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.LEFT_STICK)

    @property
    def left_stick_button_down(self) -> bool:
        """The value of the Left stick button on the controller."""
        return self._gamepad.get_button(Button.LEFT_STICK)

    def get_left_stick_button_pressed(self) -> bool:
        """Whether the Left stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.LEFT_STICK)

    @property
    def left_stick_button_pressed(self) -> bool:
        """Whether the Left stick button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.LEFT_STICK)

    def get_left_stick_button_released(self) -> bool:
        """Whether the Left stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.LEFT_STICK)

    @property
    def left_stick_button_released(self) -> bool:
        """Whether the Left stick button was released since the last check."""
        return self._gamepad.get_button_released(Button.LEFT_STICK)

    def get_right_stick_button(self) -> bool:
        """Read the value of the Right stick button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.RIGHT_STICK)

    @property
    def right_stick_button_down(self) -> bool:
        """The value of the Right stick button on the controller."""
        return self._gamepad.get_button(Button.RIGHT_STICK)

    def get_right_stick_button_pressed(self) -> bool:
        """Whether the Right stick button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.RIGHT_STICK)

    @property
    def right_stick_button_pressed(self) -> bool:
        """Whether the Right stick button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.RIGHT_STICK)

    def get_right_stick_button_released(self) -> bool:
        """Whether the Right stick button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.RIGHT_STICK)

    @property
    def right_stick_button_released(self) -> bool:
        """Whether the Right stick button was released since the last check."""
        return self._gamepad.get_button_released(Button.RIGHT_STICK)

    def get_left_bumper_button(self) -> bool:
        """Read the value of the Left bumper button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_down(self) -> bool:
        """The value of the Left bumper button on the controller."""
        return self._gamepad.get_button(Button.LEFT_BUMPER)

    def get_left_bumper_button_pressed(self) -> bool:
        """Whether the Left bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_pressed(self) -> bool:
        """Whether the Left bumper button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.LEFT_BUMPER)

    def get_left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.LEFT_BUMPER)

    @property
    def left_bumper_button_released(self) -> bool:
        """Whether the Left bumper button was released since the last check."""
        return self._gamepad.get_button_released(Button.LEFT_BUMPER)

    def get_right_bumper_button(self) -> bool:
        """Read the value of the Right bumper button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_down(self) -> bool:
        """The value of the Right bumper button on the controller."""
        return self._gamepad.get_button(Button.RIGHT_BUMPER)

    def get_right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_pressed(self) -> bool:
        """Whether the Right bumper button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.RIGHT_BUMPER)

    def get_right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.RIGHT_BUMPER)

    @property
    def right_bumper_button_released(self) -> bool:
        """Whether the Right bumper button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.RIGHT_BUMPER)

    def get_dpad_up_button(self) -> bool:
        """Read the value of the D-pad up button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.DPAD_UP)

    @property
    def dpad_up_button_down(self) -> bool:
        """The value of the D-pad up button on the controller."""
        return self._gamepad.get_button(Button.DPAD_UP)

    def get_dpad_up_button_pressed(self) -> bool:
        """Whether the D-pad up button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.DPAD_UP)

    @property
    def dpad_up_button_pressed(self) -> bool:
        """Whether the D-pad up button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.DPAD_UP)

    def get_dpad_up_button_released(self) -> bool:
        """Whether the D-pad up button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.DPAD_UP)

    @property
    def dpad_up_button_released(self) -> bool:
        """Whether the D-pad up button was released since the last check."""
        return self._gamepad.get_button_released(Button.DPAD_UP)

    def get_dpad_down_button(self) -> bool:
        """Read the value of the D-pad down button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.DPAD_DOWN)

    @property
    def dpad_down_button_down(self) -> bool:
        """The value of the D-pad down button on the controller."""
        return self._gamepad.get_button(Button.DPAD_DOWN)

    def get_dpad_down_button_pressed(self) -> bool:
        """Whether the D-pad down button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.DPAD_DOWN)

    @property
    def dpad_down_button_pressed(self) -> bool:
        """Whether the D-pad down button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.DPAD_DOWN)

    def get_dpad_down_button_released(self) -> bool:
        """Whether the D-pad down button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.DPAD_DOWN)

    @property
    def dpad_down_button_released(self) -> bool:
        """Whether the D-pad down button was released since the last check."""
        return self._gamepad.get_button_released(Button.DPAD_DOWN)

    def get_dpad_left_button(self) -> bool:
        """Read the value of the D-pad left button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.DPAD_LEFT)

    @property
    def dpad_left_button_down(self) -> bool:
        """The value of the D-pad left button on the controller."""
        return self._gamepad.get_button(Button.DPAD_LEFT)

    def get_dpad_left_button_pressed(self) -> bool:
        """Whether the D-pad left button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.DPAD_LEFT)

    @property
    def dpad_left_button_pressed(self) -> bool:
        """Whether the D-pad left button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.DPAD_LEFT)

    def get_dpad_left_button_released(self) -> bool:
        """Whether the D-pad left button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.DPAD_LEFT)

    @property
    def dpad_left_button_released(self) -> bool:
        """Whether the D-pad left button was released since the last check."""
        return self._gamepad.get_button_released(Button.DPAD_LEFT)

    def get_dpad_right_button(self) -> bool:
        """Read the value of the D-pad right button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_down(self) -> bool:
        """The value of the D-pad right button on the controller."""
        return self._gamepad.get_button(Button.DPAD_RIGHT)

    def get_dpad_right_button_pressed(self) -> bool:
        """Whether the D-pad right button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_pressed(self) -> bool:
        """Whether the D-pad right button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.DPAD_RIGHT)

    def get_dpad_right_button_released(self) -> bool:
        """Whether the D-pad right button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.DPAD_RIGHT)

    @property
    def dpad_right_button_released(self) -> bool:
        """Whether the D-pad right button was released since the last check."""
        return self._gamepad.get_button_released(Button.DPAD_RIGHT)

    def get_misc1_button(self) -> bool:
        """Read the value of the Miscellaneous 1 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_1)

    @property
    def misc1_button_down(self) -> bool:
        """The value of the Miscellaneous 1 button on the controller."""
        return self._gamepad.get_button(Button.MISC_1)

    def get_misc1_button_pressed(self) -> bool:
        """Whether the Miscellaneous 1 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_1)

    @property
    def misc1_button_pressed(self) -> bool:
        """Whether the Miscellaneous 1 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_1)

    def get_misc1_button_released(self) -> bool:
        """Whether the Miscellaneous 1 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_1)

    @property
    def misc1_button_released(self) -> bool:
        """Whether the Miscellaneous 1 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_1)

    def get_right_paddle1_button(self) -> bool:
        """Read the value of the Right Paddle 1 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_down(self) -> bool:
        """The value of the Right Paddle 1 button on the controller."""
        return self._gamepad.get_button(Button.RIGHT_PADDLE_1)

    def get_right_paddle1_button_pressed(self) -> bool:
        """Whether the Right Paddle 1 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_pressed(self) -> bool:
        """Whether the Right Paddle 1 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.RIGHT_PADDLE_1)

    def get_right_paddle1_button_released(self) -> bool:
        """Whether the Right Paddle 1 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.RIGHT_PADDLE_1)

    @property
    def right_paddle1_button_released(self) -> bool:
        """Whether the Right Paddle 1 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.RIGHT_PADDLE_1)

    def get_left_paddle1_button(self) -> bool:
        """Read the value of the Left Paddle 1 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_down(self) -> bool:
        """The value of the Left Paddle 1 button on the controller."""
        return self._gamepad.get_button(Button.LEFT_PADDLE_1)

    def get_left_paddle1_button_pressed(self) -> bool:
        """Whether the Left Paddle 1 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_pressed(self) -> bool:
        """Whether the Left Paddle 1 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.LEFT_PADDLE_1)

    def get_left_paddle1_button_released(self) -> bool:
        """Whether the Left Paddle 1 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.LEFT_PADDLE_1)

    @property
    def left_paddle1_button_released(self) -> bool:
        """Whether the Left Paddle 1 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.LEFT_PADDLE_1)

    def get_right_paddle2_button(self) -> bool:
        """Read the value of the Right Paddle 2 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_down(self) -> bool:
        """The value of the Right Paddle 2 button on the controller."""
        return self._gamepad.get_button(Button.RIGHT_PADDLE_2)

    def get_right_paddle2_button_pressed(self) -> bool:
        """Whether the Right Paddle 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_pressed(self) -> bool:
        """Whether the Right Paddle 2 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.RIGHT_PADDLE_2)

    def get_right_paddle2_button_released(self) -> bool:
        """Whether the Right Paddle 2 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.RIGHT_PADDLE_2)

    @property
    def right_paddle2_button_released(self) -> bool:
        """Whether the Right Paddle 2 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.RIGHT_PADDLE_2)

    def get_left_paddle2_button(self) -> bool:
        """Read the value of the Left Paddle 2 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_down(self) -> bool:
        """The value of the Left Paddle 2 button on the controller."""
        return self._gamepad.get_button(Button.LEFT_PADDLE_2)

    def get_left_paddle2_button_pressed(self) -> bool:
        """Whether the Left Paddle 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_pressed(self) -> bool:
        """Whether the Left Paddle 2 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.LEFT_PADDLE_2)

    def get_left_paddle2_button_released(self) -> bool:
        """Whether the Left Paddle 2 button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.LEFT_PADDLE_2)

    @property
    def left_paddle2_button_released(self) -> bool:
        """Whether the Left Paddle 2 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.LEFT_PADDLE_2)

    def get_touchpad_button(self) -> bool:
        """Read the value of the Touchpad button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.TOUCHPAD)

    @property
    def touchpad_button_down(self) -> bool:
        """The value of the Touchpad button on the controller."""
        return self._gamepad.get_button(Button.TOUCHPAD)

    def get_touchpad_button_pressed(self) -> bool:
        """Whether the Touchpad button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.TOUCHPAD)

    @property
    def touchpad_button_pressed(self) -> bool:
        """Whether the Touchpad button was pressed since the last check."""
        return self._gamepad.get_button_pressed(Button.TOUCHPAD)

    def get_touchpad_button_released(self) -> bool:
        """Whether the Touchpad button was released since the last check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.TOUCHPAD)

    @property
    def touchpad_button_released(self) -> bool:
        """Whether the Touchpad button was released since the last check."""
        return self._gamepad.get_button_released(Button.TOUCHPAD)

    def get_misc2_button(self) -> bool:
        """Read the value of the Miscellaneous 2 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_2)

    @property
    def misc2_button_down(self) -> bool:
        """The value of the Miscellaneous 2 button on the controller."""
        return self._gamepad.get_button(Button.MISC_2)

    def get_misc2_button_pressed(self) -> bool:
        """Whether the Miscellaneous 2 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_2)

    @property
    def misc2_button_pressed(self) -> bool:
        """Whether the Miscellaneous 2 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_2)

    def get_misc2_button_released(self) -> bool:
        """Whether the Miscellaneous 2 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_2)

    @property
    def misc2_button_released(self) -> bool:
        """Whether the Miscellaneous 2 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_2)

    def get_misc3_button(self) -> bool:
        """Read the value of the Miscellaneous 3 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_3)

    @property
    def misc3_button_down(self) -> bool:
        """The value of the Miscellaneous 3 button on the controller."""
        return self._gamepad.get_button(Button.MISC_3)

    def get_misc3_button_pressed(self) -> bool:
        """Whether the Miscellaneous 3 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_3)

    @property
    def misc3_button_pressed(self) -> bool:
        """Whether the Miscellaneous 3 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_3)

    def get_misc3_button_released(self) -> bool:
        """Whether the Miscellaneous 3 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_3)

    @property
    def misc3_button_released(self) -> bool:
        """Whether the Miscellaneous 3 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_3)

    def get_misc4_button(self) -> bool:
        """Read the value of the Miscellaneous 4 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_4)

    @property
    def misc4_button_down(self) -> bool:
        """The value of the Miscellaneous 4 button on the controller."""
        return self._gamepad.get_button(Button.MISC_4)

    def get_misc4_button_pressed(self) -> bool:
        """Whether the Miscellaneous 4 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_4)

    @property
    def misc4_button_pressed(self) -> bool:
        """Whether the Miscellaneous 4 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_4)

    def get_misc4_button_released(self) -> bool:
        """Whether the Miscellaneous 4 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_4)

    @property
    def misc4_button_released(self) -> bool:
        """Whether the Miscellaneous 4 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_4)

    def get_misc5_button(self) -> bool:
        """Read the value of the Miscellaneous 5 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_5)

    @property
    def misc5_button_down(self) -> bool:
        """The value of the Miscellaneous 5 button on the controller."""
        return self._gamepad.get_button(Button.MISC_5)

    def get_misc5_button_pressed(self) -> bool:
        """Whether the Miscellaneous 5 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_5)

    @property
    def misc5_button_pressed(self) -> bool:
        """Whether the Miscellaneous 5 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_5)

    def get_misc5_button_released(self) -> bool:
        """Whether the Miscellaneous 5 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_5)

    @property
    def misc5_button_released(self) -> bool:
        """Whether the Miscellaneous 5 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_5)

    def get_misc6_button(self) -> bool:
        """Read the value of the Miscellaneous 6 button on the controller.

        :returns: The state of the button.
        """
        return self._gamepad.get_button(Button.MISC_6)

    @property
    def misc6_button_down(self) -> bool:
        """The value of the Miscellaneous 6 button on the controller."""
        return self._gamepad.get_button(Button.MISC_6)

    def get_misc6_button_pressed(self) -> bool:
        """Whether the Miscellaneous 6 button was pressed since the last check.

        :returns: Whether the button was pressed since the last check.
        """
        return self._gamepad.get_button_pressed(Button.MISC_6)

    @property
    def misc6_button_pressed(self) -> bool:
        """Whether the Miscellaneous 6 button was pressed since the last
        check."""
        return self._gamepad.get_button_pressed(Button.MISC_6)

    def get_misc6_button_released(self) -> bool:
        """Whether the Miscellaneous 6 button was released since the last
        check.

        :returns: Whether the button was released since the last check.
        """
        return self._gamepad.get_button_released(Button.MISC_6)

    @property
    def misc6_button_released(self) -> bool:
        """Whether the Miscellaneous 6 button was released since the last
        check."""
        return self._gamepad.get_button_released(Button.MISC_6)

    def set_left_x_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the left X axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._gamepad.set_left_x_deadband(deadband)

    def set_left_y_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the left Y axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._gamepad.set_left_y_deadband(deadband)

    def set_right_x_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the right X axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._gamepad.set_right_x_deadband(deadband)

    def set_right_y_deadband(self, deadband: SupportsFloat | SupportsIndex):
        """Set the deadband for the right Y axis.

        The deadband is clamped to [0, 1).

        :param deadband: The deadband to apply.
        """
        self._gamepad.set_right_y_deadband(deadband)
