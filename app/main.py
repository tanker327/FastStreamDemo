from faststream import FastStream
from .brokers import broker
from .utils import queues  # Ensure configuration is loaded
import app.orders.consumers
import app.logs.consumers
from app.orders.publishers import publish_order_created, publish_order_updated
from app.logs.publishers import publish_error_log, publish_info_log

app = FastStream(broker)

@app.after_startup
async def test_publish():
    await publish_order_created("12345")
    await publish_order_updated("12345")
    await publish_error_log("Database connection failed")
    await publish_info_log("System started successfully")

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run())
