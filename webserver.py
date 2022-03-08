from typing import List, Optional, Dict
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config
from finder import word_finder


class RequestModel(BaseModel):
    game_mode: str
    exact: Optional[Dict] = None
    contains: Optional[List[str]] = None
    not_contains: Optional[List[str]] = None


class ResponseModel(BaseModel):
    message: str
    result: List[str]
    result_count: int


app = FastAPI(title="Wordle Vaajoor Helper")


@app.get("/")
async def root():
    return {"message": "The webserver working properly"}


@app.post("/find", response_model=ResponseModel)
async def find(request: RequestModel):
    response = word_finder(request.game_mode, request.exact, request.contains, request.not_contains)

    return response


def run_webserver():
    uvicorn.run(app, host=config('HOST'), port=int(config('PORT')))
