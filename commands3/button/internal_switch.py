from commands3 import EventLoop, Trigger


class InternalToggle(Trigger):
    """Defines a virtual toggle switch directly that triggers a Command.

    Programmatically toggle it to invoke the trigger once.
    """

    def __init__(
        self,
        scheduler: Scehduler | None = None,
        loop: EventLoop | None = None,
    ):
        self._last_state = False
        self._state = False

        # Python GIL makes everything atomic, so AtomicBool translates as bool.
        # May need to add a wrapper if we use the GIL.
        super().__init__(lambda: self.is_toggled, scheduler, loop)

    @property
    def is_toggled(self):
        """Checks whether or not the switch has been toggled.

        This occurs when the state of the switch is different from the
        last known state of the switch.
        """
        ret = self._state != self._last_state
        self._last_state = self._state

        return ret

    def toggle(self):
        """Toggle the switch."""
        self._state = not self._state
