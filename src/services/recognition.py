from src.configs.config import env

from src.services.breed_recognition import BreedRecognitionService
from src.services.disease_recognition import DiseaseRecognitionService


class RecognitionService:
    def __init__(self):
        self.breed_recognition_service = BreedRecognitionService()
        self.disease_recognition_service = DiseaseRecognitionService()

    def get_breed(self, url_image: str) -> str:
        data = self.breed_recognition_service.predict(url_image)
        sorted_output = sorted(data["output"], key=lambda x: x["score"], reverse=True)

        # Obtener solo los tres mayores scores
        top_three = sorted_output[:3]

        # Crear el nuevo formato de datos
        result = {"breed": [{"name": item["label"], "score": item["score"]} for item in top_three]}
        return result

    def get_skin_disease(self, image):
        return self.disease_recognition_service.predict(image)