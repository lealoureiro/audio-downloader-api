
from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
import os
import api

app = FastAPI()

app.include_router(api.router)

api.library_dir = os.getenv("LIBRARY_DIR", '.')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True, debug=True)