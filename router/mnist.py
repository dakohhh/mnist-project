import asyncio

from fastapi.responses import HTMLResponse
from xhr.exceptions import BadRequestException
from xhr.response import CustomResponse
from utils.query import PredictQuery
from utils.model import MNISTModel
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates



router = APIRouter(prefix="/mnist", tags=["Main"])

templates = Jinja2Templates(directory="templates")





@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    print(request.base_url)

    return templates.TemplateResponse("index.html", {"request": request})

