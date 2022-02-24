import uvicorn
from fastapi import FastAPI, Request
from finder import word_finder

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The webserver working properly"}


@app.post("/find")
async def root(request_body: Request):
    try:
        request_body = await request_body.json()
    except:
        return {"message": "Invalid json format"}

    try:
        game_mode = request_body["type"]
    except:
        return {"message": "You must specify the type of the request"}

    exact_dict = request_body.get("exact", {})
    contains_list = request_body.get("contains", [])

    response = word_finder(game_mode, exact_dict, contains_list)

    return response


def run_server():
    # uvicorn.run(app, host=HOST_ADDRESS, port=HOST_PORT)
    uvicorn.run(app)
