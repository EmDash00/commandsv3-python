from typing import SupportsIndex

from wpilib import RobotState

from commands3 import Trigger


class OnEnable(Trigger):
    """Returns a trigger that is True when the robot is enabled, regardless of
    mode."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_enabled, scheduler, loop)


class OnDisable(Trigger):
    """Returns a trigger that is `True when the robot is disabled."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_disabled, scheduler, loop)


class OnEStop(Trigger):
    """Returns a trigger that is True when the robot is e-stopped."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_e_stopped, scheduler, loop)


class OnAutonomousEnable(Trigger):
    """Returns a trigger that is True when the robot is enabled in autonomous
    mode."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_autonomous_enabled, scheduler, loop)


class OnTeleopEnable(Trigger):
    """Returns a trigger that is True when the robot is enabled in teleop
    mode."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_teleop_enabled, scheduler, loop)


class OnUtilityEnable(Trigger):
    """Returns a trigger that is True when the robot is enabled in utility
    mode."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_utility_enabled, scheduler, loop)


class OnDSAttached(Trigger):
    """Returns a trigger that is True when the robot is attached to a driver
    station."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_ds_attached, scheduler, loop)


class OnFMSAttached(Trigger):
    """Returns a trigger that is True when the robot is attached to an FMS."""

    def __init__(
        self, scheduler: Scheduler | None = None, loop: EventLoop | None = None
    ) -> None:
        super().__init__(RobotState.is_fms_attached, scheduler, loop)


class OnOpMode(Trigger):
    """Returns a trigger that is True when the robot is in the specified
    :class:`~wpilib.opmodes.OpMode`."""

    def __init__(
        self,
        opmode: str | SupportsInt | SupportsIndex,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ) -> None:
        if isinstance(opmode, str):
            condition = lambda: RobotState.get_opmode() == opmode
        elif isinstance(opmode, SupportsInt | SupportsIndex):
            opmode_id = int(opmode)
            condition = lambda: RobotState.get_opmode_id() == opmode_id
        else:
            raise TypeError(
                "opmode must be a string with the name of the op mode or an "
                "integer that specifies the op mode's ID"
            )
        super().__init__(condition, scheduler, loop)
