import json
from typing import Dict, Protocol
from faststream.rabbit import RabbitExchange, RabbitQueue


class QueueConfigProtocol(Protocol):
    queue: RabbitQueue
    exchange: RabbitExchange
    routing_key: str


class QueueConfig:
    def __init__(self, queue: RabbitQueue, exchange: RabbitExchange, routing_key: str):
        self.queue = queue
        self.exchange = exchange
        self.routing_key = routing_key


def load_queue_config(
    config_file: str = "../messaging_config.json",
) -> tuple[Dict[str, RabbitExchange], Dict[str, QueueConfig]]:
    with open(config_file, "r") as f:
        config = json.load(f)

    exchanges = {
        name: RabbitExchange(name=name, type=conf["type"])
        for name, conf in config["exchanges"].items()
    }

    queues = {
        name: QueueConfig(
            queue=RabbitQueue(name=name),
            exchange=exchanges[conf["exchange"]],
            routing_key=conf["routing_key"],
        )
        for name, conf in config["queues"].items()
    }

    return exchanges, queues


# Load raw configuration
exchanges_raw, queues_raw = load_queue_config()


# generate dynamic classes
def create_dynamic_class(name: str, raw_data: Dict, return_type: type) -> type:
    class DynamicClass:
        def __getattr__(self, attr: str) -> return_type:
            full_name = attr.replace("_", "-")
            if full_name in raw_data:
                return raw_data[full_name]
            available = ", ".join(raw_data.keys())
            raise AttributeError(
                f"'{name}' has no attribute '{full_name}'. Available options: {available}"
            )

        def __dir__(self):
            return [name.replace("-", "_") for name in raw_data.keys()]

    DynamicClass.__name__ = name
    return DynamicClass


# Dynamically generate Exchanges and Queues
exchanges = create_dynamic_class("Exchanges", exchanges_raw, RabbitExchange)()
queues = create_dynamic_class("Queues", queues_raw, QueueConfigProtocol)()
