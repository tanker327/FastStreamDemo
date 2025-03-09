from ..brokers import broker
from ..utils import exchanges

async def publish_order_created(order_id: str):
    msg = f"Order {order_id} created"
    await broker.publish(msg, exchange=exchanges.orders, routing_key="order.created")
    await broker.publish(msg, exchange=exchanges.orders_topic, routing_key="order.created")

async def publish_order_updated(order_id: str):
    msg = f"Order {order_id} updated"
    await broker.publish(msg, exchange=exchanges.orders, routing_key="order.updated")
    await broker.publish(msg, exchange=exchanges.orders_topic, routing_key="order.updated")
