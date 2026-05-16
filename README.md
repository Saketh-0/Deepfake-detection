# 🎭 Deepfake Video Detector

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

> A web application that detects whether a video is AI-generated (deepfake) or authentic, and issues a **verifiable authenticity certificate** for genuine videos.

---

## ✨ Features

- 📤 Upload any video file through a clean web UI
- 🤖 Deep learning model analyzes video frames for manipulation artifacts
- 📊 Returns a **probability score** (0–1) for deepfake likelihood
- 📜 Generates an authenticity certificate for videos classified as real
- ⚡ Flask backend for fast, lightweight serving

---

## 🏗️ Architecture

```
User uploads video
      ↓
Flask backend (app.py)
      ↓
Frame extraction & preprocessing
      ↓
Pretrained deep learning model
  • Analyzes facial inconsistencies
  • Detects temporal artifacts
      ↓
Prediction: Real / Fake + probability score
      ↓
Certificate generation (if authentic)
```

---

## 🗂️ Project Structure

```
Deepfake-detection/
├── app.py                  # Flask application & routing
├── models/                 # Pretrained deepfake detection model
├── templates/              # HTML templates (upload page, results page)
├── static/                 # CSS, JavaScript assets
├── uploaded_videos/        # Temporary storage for uploaded videos
├── instance/               # Flask instance config
└── requirement.txt         # Python dependencies
```

---

## ⚡ Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Saketh-0/Deepfake-detection.git
cd Deepfake-detection
```

### 2. Install dependencies
```bash
pip install -r requirement.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## 🧪 Example Output

```
Input:  video.mp4 (uploaded via UI)

Output:
  Deepfake Probability: 0.87
  Prediction: ⚠️ FAKE
  
  -- or --
  
  Deepfake Probability: 0.06
  Prediction: ✅ AUTHENTIC
  Certificate: issued ✔
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| ML Model | PyTorch (pretrained deepfake classifier) |
| Frontend | HTML, CSS, JavaScript |
| Video Processing | OpenCV / frame extraction |

---

## 📚 Key Learnings

- Building end-to-end ML-powered web applications with Flask
- Integrating pretrained deep learning models into a REST-style backend
- Video preprocessing and frame-level analysis for temporal artifact detection
- Designing user-facing interfaces for AI predictions

---

*Part of my AI/ML portfolio — [View more projects](https://github.com/Saketh-0)*
