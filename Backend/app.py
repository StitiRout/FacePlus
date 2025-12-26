from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import io
from PIL import Image
import random
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Compliment templates
COMPLIMENTS = [
    "You look absolutely amazing today!",
    "Your smile radiates pure joy and warmth!",
    "What a stunning and confident expression!",
    "Your eyes sparkle with genuine kindness!",
    "You have such a beautiful and unique look!",
    "Your facial features are perfectly harmonious!",
    "You exude confidence and positivity!",
    "Your natural beauty shines through!",
    "You have a captivating and charming presence!",
    "Your face tells a story of happiness and grace!",
    "You look radiant and full of life!",
    "Your features create a perfect balance of elegance!",
    "You have an infectious positive energy!",
    "Your smile could light up any room!",
    "You possess a timeless and classic beauty!"
]

def decode_base64_image(image_data):
    """Decode base64 image data to OpenCV format"""
    try:
        # Remove data URL prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        # Decode base64
        image_bytes = base64.b64decode(image_data)
        
        # Convert to PIL Image
        pil_image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if necessary
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        # Convert to numpy array
        img_array = np.array(pil_image)
        
        # Convert RGB to BGR for OpenCV
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        return img_bgr
    except Exception as e:
        print(f"Error decoding image: {e}")
        return None

def analyze_face(image):
    """Analyze face in the image and return features"""
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    if len(faces) == 0:
        return None
    
    # Get the largest face (assuming it's the main subject)
    largest_face = max(faces, key=lambda x: x[2] * x[3])
    x, y, w, h = largest_face
    
    # Extract face region
    face_roi = gray[y:y+h, x:x+w]
    face_color = image[y:y+h, x:x+w]
    
    # Calculate basic features
    face_area = w * h
    image_area = image.shape[0] * image.shape[1]
    face_ratio = face_area / image_area
    
    # Detect if eyes are open (simplified - using brightness variance)
    eye_region = face_roi[int(h*0.2):int(h*0.5), int(w*0.1):int(w*0.9)]
    eye_variance = np.var(eye_region) if eye_region.size > 0 else 0
    
    # Detect smile (using mouth region brightness)
    mouth_region = face_roi[int(h*0.6):int(h*0.9), int(w*0.2):int(w*0.8)]
    mouth_brightness = np.mean(mouth_region) if mouth_region.size > 0 else 0
    
    # Calculate symmetry (simplified)
    left_half = face_roi[:, :w//2]
    right_half = cv2.flip(face_roi[:, w//2:], 1)
    if right_half.shape[1] > left_half.shape[1]:
        right_half = right_half[:, :left_half.shape[1]]
    elif left_half.shape[1] > right_half.shape[1]:
        left_half = left_half[:, :right_half.shape[1]]
    
    symmetry_score = 0
    if left_half.shape == right_half.shape:
        diff = cv2.absdiff(left_half, right_half)
        symmetry_score = 1 - (np.mean(diff) / 255.0)
    
    return {
        'face_detected': True,
        'face_size': face_ratio,
        'eye_openness': min(eye_variance / 100, 1.0),
        'smile_intensity': min(mouth_brightness / 255, 1.0),
        'symmetry': max(0, symmetry_score),
        'face_position': {'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)}
    }

def calculate_score(face_features):
    """Calculate positivity/beauty score based on face features"""
    if not face_features:
        return 0
    
    # Base score from face detection
    base_score = 50
    
    # Face size factor (optimal range)
    face_size_score = 0
    if 0.1 <= face_features['face_size'] <= 0.4:
        face_size_score = 20
    elif 0.05 <= face_features['face_size'] <= 0.5:
        face_size_score = 15
    else:
        face_size_score = 10
    
    # Eye openness (indicates alertness/positivity)
    eye_score = face_features['eye_openness'] * 15
    
    # Smile intensity (major factor for positivity)
    smile_score = face_features['smile_intensity'] * 20
    
    # Symmetry (aesthetic factor)
    symmetry_score = face_features['symmetry'] * 15
    
    # Calculate total score (0-100)
    total_score = base_score + face_size_score + eye_score + smile_score + symmetry_score
    
    # Ensure score is between 0-100
    total_score = max(0, min(100, int(total_score)))
    
    return total_score

def generate_compliment(score, face_features):
    """Generate a personalized compliment based on score and features"""
    # Select compliment based on score range
    if score >= 90:
        compliment_pool = COMPLIMENTS[:5]  # Top compliments
    elif score >= 80:
        compliment_pool = COMPLIMENTS[5:10]
    else:
        compliment_pool = COMPLIMENTS[10:]
    
    # Add feature-specific compliments
    if face_features and face_features.get('smile_intensity', 0) > 0.7:
        compliment_pool = [
            "Your radiant smile lights up everything around you!",
            "That beautiful smile shows your inner joy!",
            "Your smile is absolutely contagious!"
        ] + compliment_pool
    
    return random.choice(compliment_pool)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'FacePlus API is running'
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    """Analyze uploaded image and return score with compliment"""
    try:
        # Get image data from request
        data = request.get_json()
        
        if not data or 'image' not in data:
            return jsonify({
                'error': 'No image data provided'
            }), 400
        
        image_data = data['image']
        
        # Decode image
        image = decode_base64_image(image_data)
        
        if image is None:
            return jsonify({
                'error': 'Failed to decode image'
            }), 400
        
        # Analyze face
        face_features = analyze_face(image)
        
        if not face_features:
            return jsonify({
                'error': 'No face detected in the image. Please upload a clear photo with a visible face.',
                'score': 0,
                'compliment': 'Please try again with a photo that shows your face clearly!'
            }), 400
        
        # Calculate score
        score = calculate_score(face_features)
        
        # Generate compliment
        compliment = generate_compliment(score, face_features)
        
        # Return results
        return jsonify({
            'success': True,
            'score': score,
            'compliment': compliment,
            'features': {
                'face_detected': face_features['face_detected'],
                'smile_detected': face_features['smile_intensity'] > 0.5,
                'symmetry_score': round(face_features['symmetry'] * 100, 1)
            }
        }), 200
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({
            'error': f'Internal server error: {str(e)}'
        }), 500

@app.route('/api/analyze-file', methods=['POST'])
def analyze_file():
    """Alternative endpoint for file upload"""
    try:
        if 'file' not in request.files:
            return jsonify({
                'error': 'No file provided'
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'error': 'No file selected'
            }), 400
        
        # Read image file
        image_bytes = file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({
                'error': 'Failed to decode image file'
            }), 400
        
        # Analyze face
        face_features = analyze_face(image)
        
        if not face_features:
            return jsonify({
                'error': 'No face detected in the image',
                'score': 0,
                'compliment': 'Please try again with a photo that shows your face clearly!'
            }), 400
        
        # Calculate score
        score = calculate_score(face_features)
        
        # Generate compliment
        compliment = generate_compliment(score, face_features)
        
        # Return results
        return jsonify({
            'success': True,
            'score': score,
            'compliment': compliment,
            'features': {
                'face_detected': face_features['face_detected'],
                'smile_detected': face_features['smile_intensity'] > 0.5,
                'symmetry_score': round(face_features['symmetry'] * 100, 1)
            }
        }), 200
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return jsonify({
            'error': f'Internal server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

