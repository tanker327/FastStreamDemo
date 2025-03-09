from ..brokers import broker
from ..utils import exchanges

async def publish_error_log(error_msg: str):
    await broker.publish(error_msg, exchange=exchanges.logs, routing_key="error.critical")

async def publish_info_log(info_msg: str):
    await broker.publish(info_msg, exchange=exchanges.logs, routing_key="info.general")
