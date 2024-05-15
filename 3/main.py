import asyncio
from fastapi import FastAPI
from uvicorn import Config, Server

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

async def run_server():
    config = Config(app, host="127.0.0.1", port=8080, log_level="info")
    server = Server(config)
    await server.serve()

async def run_producer():
    while True:
        print("Running producer task")
        await asyncio.sleep(5)

async def main():
    # Schedule both the FastAPI server and the producer task
    server_task = asyncio.create_task(run_server())
    producer_task = asyncio.create_task(run_producer())

    # Wait for both tasks to complete (they won't, as they run indefinitely)
    await asyncio.gather(server_task, producer_task)

if __name__ == "__main__":
    asyncio.run(main())
