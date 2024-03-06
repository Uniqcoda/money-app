from flask import Flask, request, render_template

from predict import predict_image_object_detection
from helpers import get_total

app = Flask(__name__)

PROJECT_NUMBER = ''
LOCATION = 'europe-west4'
ENDPOINT_ID = ''
API_ENDPOINT = "europe-west4-aiplatform.googleapis.com"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        
        if image_file:

            file_path = "./static/images/" + image_file.filename
            image_file.save(file_path)
        
            # Make a prediction using the model endpoint
            prediction = predict_image_object_detection(
                project=PROJECT_NUMBER,
                endpoint_id=ENDPOINT_ID,
                location=LOCATION,
                api_endpoint=API_ENDPOINT,
                filename=file_path
            )

            # print(prediction)
            
            # Process prediction here
            boxes = prediction['bboxes']
            labels = prediction['displayNames'] 
            scores = prediction['confidences']
            scores = [f"{score:.2f}" for score in scores]
            total_amount = get_total(labels)
            
            img_display_width = 400
            
            # Convert normalized coordinates to pixel coordinates
            boxes_pixels = []
            for box in boxes:
                box_pixels = [] # xMin, xMax, yMin, yMax
                for x in box:
                    box_pixels.append(x * img_display_width)
                boxes_pixels.append(box_pixels)

            # print(boxes_pixels)

            # Zip the boxes, labels, and scores together
            zip_predictions = zip(boxes_pixels, labels, scores)
            
            # Render template with prediction
            return render_template('index.html', predictions=zip_predictions, image_path=file_path, img_width=img_display_width, total_amount=total_amount )
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
