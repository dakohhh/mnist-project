from datetime import date
import os
import certifi
from fastapi.responses import JSONResponse
import requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request



CERTIFICATE = os.path.join(os.path.dirname(certifi.__file__), "cacert.pem")


app = FastAPI(title="MNIST PROHECT")


origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail, "success": False},
    )


@app.exception_handler(requests.HTTPError)
async def http_exception_handler(request, exc: requests.HTTPError):
    return JSONResponse(
        status_code=exc.response.status_code,
        content={
            "status": exc.response.status_code,
            "message": exc.response.json()["message"],
            "success": False,
        },
    )


@app.get("/")
def home(request: Request):
    return {"version": "0.1", "name": "MNSIT PRPOJECT"}