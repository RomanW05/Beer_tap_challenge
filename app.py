import uvicorn
import uuid
import time
import datetime
import json
import requests
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse, JSONResponse

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, ValidationError, validator


mock_url = "https://stoplight.io/mocks/rviewer/beer-tap-dispenser/90004725"

app = FastAPI()


class new_dispenser_schema(BaseModel):
    flow_volume: float
    id: uuid.UUID


@app.post('/new_dispenser')
def new_dispenser(request: Request, flow_volume:float) -> Response:
    headers = { 'Content-Type': "application/json" }
    payload = {"flow_volume": flow_volume}
    results = requests.post(f"{mock_url}/dispenser", headers=headers, data=json.dumps(payload))
    contents = json.loads(results.text)

    if results.status_code == 200:
        status_code = status.HTTP_200_OK
    if results.status_code != 200:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    
    try:
        new_dispenser_schema(
            flow_volume = contents['flow_volume'],
            id = contents['id']
        )
    except ValidationError as e:
        print(e)

    return JSONResponse(content=contents, status_code=status_code)


@app.put("/open/dispenser/{id}/status")
def open_tap(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "status": "open",
        "updated_at": date_now
    }

    results = requests.put(f"{mock_url}/dispenser/{id}/status", headers=headers, data=json.dumps(payload))

    if results.status_code == 409:
        contents = {"status":"The tap is already opened"}
        status_code = 409

    elif results.status_code == 202:
        contents = {"status": f"Tap with id {id} opened"}
        status_code = 202
    
    elif results.status_code == 500:
        contents = {"status":"Internal server error"}
        status_code = 500
    
    elif results.status_code == 422:
        contents ={"status":"Unprocessable Entity"}
        status_code = 422
    else:
        contents = {"status":"Undefined"}
        status_code = results.status_code


    return JSONResponse(content=contents, status_code=status_code)


@app.put("/close/dispenser/{id}/status")
def close_tap(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "status": "close",
        "updated_at": date_now
    }

    results = requests.put(f"{mock_url}/dispenser/{id}/status", headers=headers, data=json.dumps(payload))

    if results.status_code == 409:
        contents = {"status":"The tap is already closed"}
        status_code = 409

    elif results.status_code == 202:
        contents = {"status": f"Tap with id {id} closed"}
        status_code = 202
    
    elif results.status_code == 500:
        contents = {"status":"Internal server error"}
        status_code = 500
    
    elif results.status_code == 422:
        contents ={"status":"Unprocessable Entity"}
        status_code = 422
    else:
        contents = {"status":"Undefined"}
        status_code = results.status_code


    return JSONResponse(content=contents, status_code=status_code)


@app.get('/dispenser/{id}/spending')
def get_bill(request: Request, id:str) -> Response:
    headers = { 'Content-Type': "application/json" }
    results = requests.get(f"{mock_url}/dispenser/{id}/spending", headers=headers)
    print(results.text)
    contents = json.loads(results.text)

    return JSONResponse(content=contents, status_code=results.status_code)


