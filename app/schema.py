# app/schemas.py

from pydantic import BaseModel

class RequestData(BaseModel):
    host: str
    uri: str
    auth: str
    agent: str
    cookie: str
    referer: str
    body: str
