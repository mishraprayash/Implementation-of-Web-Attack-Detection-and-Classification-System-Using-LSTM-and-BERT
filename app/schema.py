# app/schemas.py

from pydantic import BaseModel

class RequestData(BaseModel):
    method:str
    source_ip:str
    host: str
    uri: str
    auth: str
    agent: str
    cookie: str
    referer: str
    body: str
