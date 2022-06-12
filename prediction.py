from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = "https://plantdiseasedetection-prediction.cognitiveservices.azure.com/"
# training_key = "PASTE_YOUR_CUSTOM_VISION_TRAINING_SUBSCRIPTION_KEY_HERE"
prediction_key = "b88d5f31083c4e33bc7f2c6f595354ab"
prediction_resource_id = "/subscriptions/06dd452b-ef1f-4649-9b43-4aebecd9c0c0/resourceGroups/AzureInternshipProject"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# base_image_location = os.path.join (os.path.dirname(__file__), "Images")
publish_iteration_name = "Iteration1"
project_id = "30b4cc24-cf83-42f8-b87f-b36086ec6051"


def predict(image):
    test_data = image
    results = predictor.classify_image(project_id, publish_iteration_name, test_data)
    for prediction in results.predictions:
            if(prediction.tag_name == "Apple_healthy" and prediction.probability > 0.5):
                return "Healthy"
            elif(prediction.tag_name == "Apple_scab" and prediction.probability > 0.5):
                return "Apple scab"
            elif(prediction.tag_name == "Grape_healthy" and prediction.probability > 0.5):
                return "healthy"
            elif(prediction.tag_name == "Grape_blackRot" and prediction.probability > 0.5):
                return "Grape blackRot"
            elif(prediction.tag_name == "Corn_healthy" and prediction.probability > 0.5):
                return "healthy"
            elif(prediction.tag_name == "Corn_commonRust" and prediction.probability > 0.5):
                return "Corn commonRust"