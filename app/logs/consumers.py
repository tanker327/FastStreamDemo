from ..brokers import broker
from ..utils import queues


@broker.subscriber(queue=queues.error_log.queue)
async def handle_error_log(msg: str):
    print(f"Error Log: {msg}")


@broker.subscriber(queue=queues.info_log.queue)
async def handle_info_log(msg: str):
    print(f"Info Log: {msg}")


@broker.subscriber(queue=queues.all_log.queue)
async def handle_all_logs(msg: str):
    print(f"All Logs: {msg}")
