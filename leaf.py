from flask import Flask, render_template, request, jsonify
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load the model
model_path = os.getenv('MODEL_PATH', 'model.h5')  # Use environment variable or default to 'model.h5'
model = load_model(model_path)
print("Model Loaded Successfully")

# Function to predict disease
def pred_tomato_dieas(tomato_plant):
    try:
        test_image = load_img(tomato_plant, target_size=(128, 128))
        test_image = img_to_array(test_image) / 255.0
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        pred = np.argmax(result, axis=1)
        
        # Disease prediction mapping
        disease_map = {
            0: ("Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html'),
            1: ("Tomato - Early Blight Disease", 'Tomato-Early_Blight.html'),
            2: ("Tomato - Healthy and Fresh", 'Tomato-Healthy.html'),
            3: ("Tomato - Late Blight Disease", 'Tomato - Late_Blight.html'),
            4: ("Tomato - Leaf Mold Disease", 'Tomato - Leaf_Mold.html'),
            5: ("Tomato - Septoria Leaf Spot Disease", 'Tomato - Septoria_Leaf_Spot.html'),
            6: ("Tomato - Target Spot Disease", 'Tomato - Target_Spot.html'),
            7: ("Tomato - Tomato Yellow Leaf Curl Virus Disease", 'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'),
            8: ("Tomato - Tomato Mosaic Virus Disease", 'Tomato - Tomato_Mosaic_Virus.html'),
            9: ("Tomato - Two Spotted Spider Mite Disease", 'Tomato - Two_Spotted_Spider_Mite.html')
        }
        
        return disease_map.get(pred[0], ("Unknown Disease", 'error.html'))
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error during prediction", 'error.html'

# Create Flask instance
app = Flask(__name__)

# Ensure the upload directory exists
UPLOAD_FOLDER = 'static/upload'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Render index.html page
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

# Get input image from client, then predict class and render respective .html page for solution
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
            return render_template(output_page, pred_output=pred, user_image=file_path)
        else:
            return render_template('error.html', pred_output="Invalid file format")

# Handle feedback submission
@app.route("/feedback", methods=['POST'])
def feedback():
    user_feedback = request.form['feedback']
    print(f"Feedback received: {user_feedback}")
    return jsonify({"status": "success", "message": "Thank you for your feedback!"})

# Allowed file types function
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False, port=8080)