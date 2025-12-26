##FacePlus – Instant Face Beauty Analyzer

FacePlus is a web-based application that analyzes a user’s facial image and provides a beauty score along with a positive compliment. The project focuses on face positivity, user-friendly design, and smooth interaction using a modern web interface.

The application guides users through a multi-step experience—starting with an engaging splash screen, followed by a brief project introduction, and finally an interactive dashboard where users can upload a photo or use their camera for analysis.

⚠️ Note: This project is intended for educational and experimental purposes only and promotes positivity, not judgment.

 ##Features

🌈 Attractive landing splash with project branding

🧭 Step-by-step navigation (Splash → Welcome → Dashboard)

📷 Upload image or use live camera

📊 Instant beauty score generation

💬 Positive compliment based on analysis

🎨 Modern UI inspired by Figma designs

⚡ Smooth animations and transitions

## Tech Stack
##Frontend

HTML

CSS

JavaScript

React (with TypeScript)

Tailwind CSS (for styling)

Framer Motion (for animations)

Backend (Planned / Optional)

Node.js / Express (for future AI integration)

Python (optional – for ML-based face analysis)

## Folder Structure
FacePlus/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SplashScreen.tsx
│   │   │   ├── WelcomeScreen.tsx
│   │   │   ├── DashboardScreen.tsx
│   │   │   └── AnalysisScreen.tsx
│   │   ├── styles/
│   │   │   └── globals.css
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── index.html
│   ├── package.json
│   └── README.md
│
└── backend/ (optional / future scope)

## Prerequisites

Node.js (v16 or above)

npm or yarn

A modern web browser (Chrome recommended)

VS Code / Cursor IDE

## Usage

Clone the repository:

git clone https://github.com/StitiRout/FacePlus.git


Navigate to frontend:

cd FacePlus/frontend


Install dependencies:

npm install


Start the development server:

npm run dev


Open in browser:

http://localhost:5173

🧪 Development Scripts
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build

## Future Enhancements

Real AI-based facial analysis using ML models

Backend API integration

User history and analytics

Improved accuracy and fairness metrics
