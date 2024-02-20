import asyncio
from fastapi import APIRouter, Request, Depends



router = APIRouter(prefix="/predict", tags=["PREDICTION"])




@router.post("/")
async def predict_digit(request: Request, ):

    return CustomResponse("Get Vendor Successful", data=result)
