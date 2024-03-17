from predict import predict_image_object_detection

from dotenv import load_dotenv
import os

# Import the API keys and other invironment variables
load_dotenv()
PROJECT_NUMBER = os.getenv('PROJECT_NUMBER')
LOCATION = os.getenv('LOCATION')
ENDPOINT_ID = os.getenv('ENDPOINT_ID')
API_ENDPOINT = os.getenv('API_ENDPOINT')

print({
    "PROJECT_NUMBER": PROJECT_NUMBER,
    "LOCATION": LOCATION,
    "ENDPOINT_ID": ENDPOINT_ID,
    "API_ENDPOINT": API_ENDPOINT
})

filename="test-images/IMG_20240305_162858.jpg"

predictions = predict_image_object_detection(
    project=PROJECT_NUMBER,
    endpoint_id=ENDPOINT_ID,
    location=LOCATION,
    api_endpoint=API_ENDPOINT,
    filename=filename
)

print(predictions)
