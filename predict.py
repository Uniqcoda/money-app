import base64
import io
from  helpers import process_img

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict


def predict_image_object_detection(
    project: str,
    endpoint_id: str,
    filename: str,
    location: str = "europe-west4",
    api_endpoint: str = "europe-west4-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}

    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

    preprocessed_img = process_img(filename, (1024, 1024))


    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    preprocessed_img.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()


    # The format of each instance should conform to the deployed model's prediction input schema.

    # Encode the image bytes
    encoded_content = base64.b64encode(img_byte_arr).decode("utf-8")
    instance = predict.instance.ImageObjectDetectionPredictionInstance(
        content=encoded_content,
    ).to_value()

    instances = [instance]

    parameters = predict.params.ImageObjectDetectionPredictionParams(
        confidence_threshold=0.7,
        # max_predictions=5,
    ).to_value()

    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )

    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )

    predictions = response.predictions
    prediction = predictions[0]


    return dict(prediction)
