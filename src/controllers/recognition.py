from fastapi import UploadFile
from src.services.recognition import RecognitionService
from src.utils import convert
from typing import List

from pydantic import BaseModel
import json

class RecognitionController:
    def __init__(self):
        self.recognitionService = RecognitionService()

    async def get_breed(self, image: str):
        print(image)
        try:
            data = self.recognitionService.get_breed(image.url_image)
            return data
        except Exception as error:
            return error, 500

    async def get_skin_disease(self, image: UploadFile):
        try:
            data = self.recognitionService.get_skin_disease(await convert.convertToArrayByte(image))
            return data
        except Exception as error:
            return error