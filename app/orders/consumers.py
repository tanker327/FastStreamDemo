from ..brokers import broker
from ..utils import queues


@broker.subscriber(queue=queues.order_create.queue)
async def handle_order_created(msg: str):
    print(f"Order Created: {msg}")


@broker.subscriber(queue=queues.order_update.queue)
async def handle_order_updated(msg: str):
    print(f"Order Updated: {msg}")


@broker.subscriber(queue=queues.order_all.queue)
async def handle_all_orders(msg: str):
    print(f"All Orders: {msg}")
