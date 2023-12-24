from typing import List
from fastapi import UploadFile
import numpy as np
import cv2 as cv

async def convertToArrayByte(image: UploadFile):
    image_bytes = await image.read()

        # Convertir los bytes de la imagen a un array numpy
    nparr = np.frombuffer(image_bytes, np.uint8)

        # Decodificar la imagen con OpenCV
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)
    return image

async def convertToTupla(images: List[UploadFile]):
    tupleImages = ()
    for image in images:
        tupleImages = tupleImages + (await convertToArrayByte(image),)
    return tupleImages