import uvicorn
import uuid

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


@app.post('/dispenser')
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



@app.put("/dispenser/{id}/status")
def change_dispenser(request: Request, id:int) -> Response:
    pass

@app.get(f'{mock_url}/dispenser/{id}/spending')
def bill(request: Request, id:int) -> Response:
    pass

