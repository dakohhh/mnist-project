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


from xhr.exceptions import *
from router.predict import router as predict

app.include_router(predict)
app.add_exception_handler(UserExistException, user_exist_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(ServerErrorException, server_exception_handler)
app.add_exception_handler(NotFoundException, not_found)
app.add_exception_handler(CredentialsException, credentail_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)



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