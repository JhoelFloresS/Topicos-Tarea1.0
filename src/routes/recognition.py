from fastapi import APIRouter, UploadFile
from typing_extensions import Annotated

from src.controllers.recognition import RecognitionController

controller = RecognitionController()

router = APIRouter()


from pydantic import BaseModel


class Image(BaseModel):
    url_image: str



@router.post("/recognition/breed", tags=["Breed Recognition"])
async def get_breed(image: Image):
    return await controller.get_breed(image)

@router.post("/recognition/skin_disease", tags=["Skin Disease Recognition"])
async def get_skin_disease(image: UploadFile):
    return await controller.get_skin_disease(image)