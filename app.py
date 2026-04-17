from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

app = Flask(__name__)

# ===== LOAD MODELS =====
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 38)

model_next = models.resnet18(weights=None)
model_next.fc = nn.Linear(model_next.fc.in_features, 38)

model.load_state_dict(torch.load("baselines_cnn_model.pth", map_location='cpu'))
model.eval()

model_next.load_state_dict(torch.load("gan_cnn_model.pth", map_location='cpu'))
model_next.eval()

# ===== IMAGE TRANSFORM =====
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ===== CLASSES =====
classes = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy'] 

# ===== ROUTES =====

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        selected_model = request.form.get("model")

        image = Image.open(file).convert("RGB")
        image = transform(image).unsqueeze(0)

        # 🔥 MODEL SELECTION
        if selected_model == "gan":
            chosen_model = model_next
        else:
            chosen_model = model

        with torch.no_grad():
            output = chosen_model(image)

            # DEBUG INFO
            print("Output shape:", output.shape)
            print("Classes length:", len(classes))

            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            confidence, predicted = torch.max(probabilities, 0)

        pred_idx = predicted.item()

        # 🔥 SAFE CHECK
        if pred_idx >= len(classes):
            return jsonify({
                "error": f"Model predicted index {pred_idx} but only {len(classes)} classes exist"
            })

        return jsonify({
            "prediction": classes[pred_idx],
            "confidence": float(confidence.item()) * 100,
            "model_used": selected_model
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == '__main__':
    app.run(debug=True)