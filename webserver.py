from typing import List, Optional, Dict
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config
from finder import word_finder


class BodyModel(BaseModel):
    game_mode: str
    exact: Optional[Dict] = None
    contains: Optional[List] = None


app = FastAPI(title="Wordle Vaajoor Helper",)


@app.get("/")
async def root():
    return {"message": "The webserver working properly"}


@app.post("/find")
async def find(body: BodyModel):
    response = word_finder(body.game_mode, body.exact, body.contains)

    return response


def run_webserver():
    uvicorn.run(app, host=config('HOST'), port=int(config('PORT')))
