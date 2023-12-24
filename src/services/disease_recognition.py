from src.configs.config import env
import tensorflow as tf
import cv2 as cv
import numpy as np



classes=['Bacterial', 'Hongos', 'Saludable', 'Hipersensibilidad']


class DiseaseRecognitionService:
    def __init__(self):
        self.model = "./src/models/model_finetuned1_10-0.98.tflite"


    @staticmethod
    def  load_image(filename):
        img = cv.imread(filename)
        new_img = cv.resize(img, (224, 224))
        new_img = new_img.astype(np.float32)
        new_img = new_img / 255

        return new_img

    def predict(self, image):
        interpreter = tf.lite.Interpreter(model_path=self.model)


        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()


        interpreter.allocate_tensors()

        # classes=['Bacterial', 'Hongos', 'Saludable', 'Hipersensibilidad']

        #  fs = FileSystemStorage()
        # filename = fs.save(uploaded_file.name, uploaded_file)

        # input = f"./media/{uploaded_file}"
        new_img = cv.resize(image, (224, 224))
        new_img = new_img.astype(np.float32)
        new_img = new_img / 255

        interpreter.set_tensor(input_details[0]['index'], [new_img])

        # run the inference
        interpreter.invoke()

        # output_details[0]['index'] = the index which provides the input
        output_data = interpreter.get_tensor(output_details[0]['index'])
        class_idx = np.argmax(output_data[0])
        return {
            'prediction': classes[class_idx],
            'accuracy': round(output_data[0][class_idx] * 100)
        }