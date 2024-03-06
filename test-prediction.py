from predict import predict_image_object_detection

filename="test-images/IMG_20240305_162858.jpg"

predictions = predict_image_object_detection(
    project="",
    endpoint_id="",
    location="europe-west4",
    api_endpoint="europe-west4-aiplatform.googleapis.com",
    filename=filename
)

print(predictions)