from typing import overload

from ntcore import BooleanSubscriber, BooleanTopic, NetworkTable, NetworkTableInstance

from commands3 import EventLoop, Trigger


class NetworkButton(Trigger):
    """
    A :class:`~commands3.trigger.Trigger` that uses a :class:`~ntcore.NetworkTable`
    field.
    """

    @overload
    def __init__(
        self,
        *,
        sub: BooleanSubscriber,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ): ...

    """Create a NetworkButton that commands be bound to.

    :param sub: The boolean subscriber that provides the value.
    """

    @overload
    def __init__(
        self,
        *,
        topic: BooleanTopic,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ): ...

    """Create a NetworkButton that commands be bound to.

    :param topic: The boolean topic that provides the value.
    """

    @overload
    def __init__(
        self,
        *,
        table: NetworkTable,
        field: str,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ): ...

    """Create a NetworkButton that commands be bound to.

    :param table: The table where the NetworkTable value is located.
    :param field: The field that provides the value.
    """

    @overload
    def __init__(
        self,
        *,
        table: str,
        field: str,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ): ...

    """Create a NetworkButton that commands be bound to.

    :param table: The name of the table where the NetworkTable value is
        located.
    :param field: The field that provides the value.
    """

    @overload
    def __init__(
        self,
        *,
        inst: str,
        table: str,
        field: str,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
    ): ...

    """Create a NetworkButton that commands be bound to.

    :param inst: The :class:`~ntcore.NetworkTableInstance` to use.
    :param table: The name of the table where the NetworkTable value is
        located.
    :param field: The field that provides the value.
    """

    def __init__(
        self,
        scheduler: Scheduler | None = None,
        loop: EventLoop | None = None,
        **kwargs,
    ):
        match kwargs:
            case {"topic": topic} if isinstance(topic, BooleanTopic):
                topic_inst = topic.get_instance()
                sub = topic.subscribe(False)
            case {"sub": sub} if isinstance(sub, BooleanSubscriber):
                topic_inst = sub.get_topic().get_instance()
                sub = sub
            case {"table": table, "field": field} if isinstance(
                table, NetworkTable
            ) and isinstance(field, str):
                topic = table.get_boolean_topic(field)
                topic_inst = topic.get_instance()
                sub = topic.subscribe(False)
            case {"table": table, "field": field} if isinstance(
                table, str
            ) and isinstance(field, str):
                topic = (
                    NetworkTableInstance.get_default()
                    .get_table(table)
                    .get_boolean_topic(field)
                )

                topic_inst = topic.get_instance()
                sub = topic.subscribe(False)
            case {"inst": inst, "table": table, "field": field} if (
                isinstance(inst, NetworkTableInstance)
                and isinstance(table, str)
                and isinstance(field, str)
            ):
                topic = inst.get_table(table).get_boolean_topic(field)
                topic_inst = topic.get_instance()
                sub = topic.subscribe(False)
            case _:
                raise TypeError(
                    f"{args} are not valid arguments to NetworkButton.__init__()"
                )

        super().__init__(
            lambda: topic_inst.is_connected() and sub.get(),
            scheduler,
            loop,
        )
