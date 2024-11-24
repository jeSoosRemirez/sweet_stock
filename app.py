"""Entrypoint for app."""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from endpoints.root import root_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
sentry_dsn = os.getenv("SENTRY_DSN")


app = FastAPI()
app.include_router(router=root_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
