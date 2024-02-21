import asyncio
from xhr.exceptions import BadRequestException
from xhr.response import CustomResponse
from utils.query import PredictQuery
from utils.model import MNISTModel
from fastapi import APIRouter, Request, Depends



router = APIRouter(prefix="/predict", tags=["PREDICTION"])




@router.post("/")
async def predict_digit(request: Request, query:PredictQuery):


    model = MNISTModel()

    pred = model.predict_digit(query.data)


    data = {"predicted_value": pred}

    return CustomResponse("predicted successfully", data=data)
