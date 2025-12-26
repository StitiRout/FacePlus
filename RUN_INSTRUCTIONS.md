# FacePlus - How to Run the Application

Complete guide to run both the Backend and Frontend of FacePlus.

## Prerequisites

### For Backend:
- **Python 3.8 or higher** (Check with `python --version`)
- **pip** (Python package manager, usually comes with Python)

### For Frontend:
- **Node.js 16+ and npm** (Check with `node --version` and `npm --version`)
- Download from: https://nodejs.org/

---

## Step 1: Setup Backend (Python Flask)

### 1.1 Navigate to Backend directory
```bash
cd Backend
```

### 1.2 Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 1.3 Activate Virtual Environment

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### 1.4 Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask
- flask-cors
- opencv-python
- numpy
- Pillow

### 1.5 Run the Backend Server
```bash
python app.py
```

You should see output like:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

**✅ Backend is now running on `http://localhost:5000`**

**Keep this terminal window open!**

---

## Step 2: Setup Frontend (React + Vite)

### 2.1 Open a NEW Terminal Window

**Important:** Keep the backend terminal running, open a new terminal for the frontend.

### 2.2 Navigate to Frontend directory
```bash
cd Frontend
```

### 2.3 Install Dependencies
```bash
npm install
```

This will install all React and UI dependencies. It may take a few minutes.

### 2.4 Run the Frontend Development Server
```bash
npm run dev
```

You should see output like:
```
  VITE v6.3.5  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**✅ Frontend is now running on `http://localhost:5173`**

---

## Step 3: Access the Application

1. Open your web browser
2. Navigate to: **http://localhost:5173**
3. You should see the FacePlus splash screen!

---

## Quick Start Summary

**Terminal 1 (Backend):**
```bash
cd Backend
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS/Linux
pip install -r requirements.txt
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd Frontend
npm install
npm run dev
```

**Then open:** http://localhost:5173 in your browser

---

## Troubleshooting

### Backend Issues

**Problem: `python` command not found**
- Use `python3` instead of `python` on macOS/Linux
- Or install Python from https://www.python.org/

**Problem: `pip` command not found**
- Use `python -m pip` instead
- Or install pip: `python -m ensurepip --upgrade`

**Problem: OpenCV installation fails**
- Try: `pip install opencv-python-headless` instead
- Or upgrade pip: `python -m pip install --upgrade pip`

**Problem: Port 5000 already in use**
- Change port in `app.py` or set environment variable:
  ```bash
  set PORT=8000  # Windows
  export PORT=8000  # macOS/Linux
  ```
- Update frontend `.env` file with new port

### Frontend Issues

**Problem: `npm` command not found**
- Install Node.js from https://nodejs.org/
- Restart terminal after installation

**Problem: Port 5173 already in use**
- Vite will automatically use the next available port
- Check terminal output for the actual port

**Problem: Cannot connect to backend**
- Make sure backend is running on port 5000
- Check backend terminal for errors
- Verify CORS is enabled in backend (it should be)

**Problem: Face detection not working**
- Make sure backend is running
- Check browser console for errors (F12)
- Verify image has a clear, visible face
- Check backend terminal for error messages

### General Issues

**Problem: Changes not reflecting**
- Restart both servers
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check terminal for error messages

**Problem: Module not found errors**
- Backend: Reinstall dependencies: `pip install -r requirements.txt`
- Frontend: Delete `node_modules` and reinstall: 
  ```bash
  rm -rf node_modules  # macOS/Linux
  rmdir /s node_modules  # Windows
  npm install
  ```

---

## Stopping the Application

1. **Stop Frontend:** Press `Ctrl+C` in the frontend terminal
2. **Stop Backend:** Press `Ctrl+C` in the backend terminal
3. **Deactivate Virtual Environment (optional):**
   ```bash
   deactivate
   ```

---

## Production Build (Optional)

### Build Frontend for Production:
```bash
cd Frontend
npm run build
```

Built files will be in `Frontend/dist/` directory.

### Run Backend in Production:
Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Need Help?

- Check backend terminal for Python errors
- Check frontend terminal for build errors
- Check browser console (F12) for runtime errors
- Verify both servers are running on correct ports
- Make sure all dependencies are installed

---

## Summary

✅ **Backend runs on:** http://localhost:5000  
✅ **Frontend runs on:** http://localhost:5173  
✅ **Access app at:** http://localhost:5173  

Both servers must be running simultaneously for the app to work!

