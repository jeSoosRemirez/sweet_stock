"""Entrypoint for app."""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from endpoints.root import root_router
import uvicorn

load_dotenv()
sentry_dsn = os.getenv("SENTRY_DSN")


app = FastAPI()
app.include_router(router=root_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
