# AI Music Player 🎵

An intelligent music player that detects your mood using real-time facial emotion analysis via webcam and plays songs accordingly.

## 🔍 About the Project

This AI Music Player uses your **facial expressions** (captured through your webcam) to predict your **emotional state** and then plays songs matching your mood. It's a seamless fusion of computer vision, emotion AI, and Python-based audio control.

## 🧠 Technologies Used

- **Python 3.x**
- **OpenCV** – for webcam access and face detection
- **DeepFace** – for real-time facial emotion recognition
- **Tkinter** – for simple GUI
- **os / random** – to manage and select songs dynamically

## 😃 Supported Emotions

The model detects and classifies the following emotions:

- Happy
- Sad
- Angry
- Neutral
- Surprise
- Fear
- Disgust

Based on the detected emotion, it plays songs from the respective folder (e.g., `happy/`, `sad/`, etc.).

## 📁 Project Structure

AI_music_player/
│
├── mood_music.py        # Main script that detects emotion via webcam and plays music accordingly
├── mood_songs.py        # Contains the mapping of emotions to song lists
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Files and folders to be ignored by Git

## 📦 Requirements

pip install -r requirements.txt

✨ Features

- 🎥 Real-time mood detection using webcam  
- 🧠 Emotion recognition via DeepFace (no manual input required)  
- 🎶 Automatically plays songs matching detected emotion  
- 🗂️ Folder-wise song organization (happy/, sad/, etc.)  
- 👩‍💻 Beginner-friendly and easy to customize  
- ⚡ Lightweight, no complex setup needed  

