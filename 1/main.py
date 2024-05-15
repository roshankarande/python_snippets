import random
import string
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():

    return {
        "Hello": f"World {''.join(random.choices(string.ascii_uppercase + string.digits, k=10))}"}

import threading
import uvicorn

# from app import app  # Assuming the FastAPI app is defined in app.py

def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # Create a thread for the FastAPI app
    fastapi_thread = threading.Thread(target=run_fastapi)
    
    # Set the thread as a daemon thread so it exits when the main thread does
    fastapi_thread.daemon = True
    
    # Start the FastAPI thread
    fastapi_thread.start()

    # # Main thread can do other work here
    # # For demonstration, we'll just wait for the thread to run
    try:
        while True:
            print("Hello world")
            time.sleep(1)
            pass  # Replace with other main thread work if needed
    except KeyboardInterrupt:
        print("Shutting down the server.")
