# Utils
from typing import *
from pydantic import BaseModel, BaseSettings, Field, validator

# FastAPI
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Routers
from routers.friends import friends

import os
import datetime


app = FastAPI(
    title="test",
    description="test"
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(friends)

templates = Jinja2Templates(directory="templates")


async def get_title():
    return ''.join(str(datetime.datetime.now()).split('.')[:-1])


@app.get("/")
async def root(request: Request, title: str = Depends(get_title)):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": title}
    )


if __name__ == "__main__":
    import uvicorn
    print(os.getenv("RELOAD", 11))
    uvicorn.run(
        "main:app",
        host=str(os.getenv("HOST", "127.0.0.1")),
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
