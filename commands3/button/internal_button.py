from commands3 import EventLoop, Trigger


class InternalButton(Trigger):
    """Defines a virtual button that directly that triggers a Command when
    pressed.

    Programmatically press it to invoke the trigger, or programmatically
    release it to end the trigger.
    """

    def __init__(
        self,
        inverted: bool = False,
        scheduler: Scehduler | None = None,
        loop: EventLoop | None = None,
    ):
        self._state = False
        self._inverted = inverted

        # Python GIL makes everything atomic, so AtomicBool translates as bool.
        # May need to add a wrapper if we use the GIL.
        super().__init__(lambda: self.state, scheduler, loop)

    @property
    def state(self) -> bool:
        """Get the boolean state of the button, accounting for inversion."""
        return self._state != self._inverted

    @property
    def is_pressed(self) -> bool:
        """Get whether or not the button is pressed."""
        return self._state

    @property
    def is_inverted(self) -> bool:
        """Get whether or not the button is inverted."""
        return self._inverted

    def set_inverted(self, inverted: bool):
        """Sets whether to invert the button state.

        :param inverted: Whether button state should be inverted.
        """
        self._inverted = inverted

    def set_pressed(self, pressed: bool):
        """Sets whether or not the button is pressed.

        :param pressed: Whether button is pressed.
        """
        self._state = pressed

    def press(self):
        """Press the button."""
        self._state = True

    def release(self):
        """Release the button."""
        self._state = False
