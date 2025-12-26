# FacePlus Backend

Python Flask backend for the FacePlus face analysis application.

## Features

- Face detection using OpenCV
- Positivity score calculation (0-100)
- Personalized compliment generation
- RESTful API endpoints
- CORS enabled for frontend communication

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Navigate to the Backend directory:
```bash
cd Backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python app.py
```

The server will start on `http://localhost:5000` by default.

You can change the port by setting the `PORT` environment variable:
```bash
set PORT=8000  # Windows
export PORT=8000  # macOS/Linux
python app.py
```

## API Endpoints

### Health Check
- **GET** `/api/health`
- Returns server status

### Analyze Image (Base64)
- **POST** `/api/analyze`
- **Request Body:**
  ```json
  {
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "score": 85,
    "compliment": "You look absolutely amazing today!",
    "features": {
      "face_detected": true,
      "smile_detected": true,
      "symmetry_score": 92.5
    }
  }
  ```

### Analyze Image (File Upload)
- **POST** `/api/analyze-file`
- **Request:** Multipart form data with `file` field
- **Response:** Same as `/api/analyze`

## How It Works

1. **Image Processing**: Receives image data (base64 or file upload)
2. **Face Detection**: Uses OpenCV's Haar Cascade classifier to detect faces
3. **Feature Analysis**: Analyzes:
   - Face size and position
   - Eye openness
   - Smile intensity
   - Facial symmetry
4. **Score Calculation**: Combines features to generate a positivity score (0-100)
5. **Compliment Generation**: Selects appropriate compliment based on score and features

## Error Handling

- Returns appropriate error messages for:
  - Missing image data
  - Invalid image format
  - No face detected
  - Server errors

## Development

To run in development mode with auto-reload:
```bash
export FLASK_ENV=development
python app.py
```

## Notes

- The face detection uses OpenCV's pre-trained Haar Cascade model
- Score calculation is based on multiple facial features
- Compliments are selected from a curated list based on score ranges
- The API is designed to work with the FacePlus frontend application

