# FacePlus
A fun and intelligent face-analysis application that detects facial features, calculates a positivity score, and generates encouraging compliments. Built using computer vision and machine learning, it analyzes expressions like smile and eye openness to provide a friendly, confidence-boosting experience.

## Overview
- Detects faces using computer vision.
- Calculates a fun “confidence score” based on smile/eye features.
- Shows encouraging comments to the user.

## Tech Stack
- Python, OpenCV, MediaPipe
- (Optional) Flask + HTML/CSS/JS for web UI

## How to Run
1. Clone the repo
2. Install dependencies
3. Run the main script
4. Open the web page / see the result window

## Future Work
- Better scoring logic
- Mobile app version

##Folder Structure
FaceComplimentAI/
│── backend/
│   ├── models/
│   ├── utils/
│   └── main.py


│── frontend/
│   ├── templates/
│   ├── static/
│   └── app.py


│── samples/
│   └── test_images/
│
│── README.md
│── requirements.txt
│── .gitignore

## Prerequisites

Make sure the following are installed before running the project:

System Requirements

Python 3.8 or above

pip (Python package manager)

A webcam (for live detection) 

Git (for cloning the repository)

##Python Libraries

Install all dependencies using:

pip install -r requirements.txt

Main Libraries Used

OpenCV

MediaPipe

NumPy

Flask (if using the web interface)

Add them to your requirements.txt:

opencv-python
mediapipe
numpy
flask

##Usage
1. Clone the Repository
git clone https://github.com/StitiRout/FacePlus.git
cd FacePlus

2. Install Dependencies
pip install -r requirements.txt

3. Run the Face Detection + Compliment Generator

If you are using the backend script:

python backend/main.py


For the web-based UI:

python frontend/app.py

4. Upload an Image or Use Webcam

The backend script will open your webcam or load an image.

The web app will allow you to upload an image.

You will receive:

Facial landmarks

Positivity/Expression score

A kind compliment

## Development Scripts

Useful commands for development and testing:

-Run Backend
python backend/main.py

-Run Frontend (Flask web app)
python frontend/app.py

Update Requirements File
pip freeze > requirements.txt


