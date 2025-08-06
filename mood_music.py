import tkinter as tk
from tkinter import messagebox
import cv2
from deepface import DeepFace
import random
import webbrowser
from datetime import datetime
import csv
import os
from mood_songs import songs_dict

# Map surprise → happy, disgust → angry
emotion_map = {
    "surprise": "happy",
    "disgust": "angry"
}

def play_song(emotion):
    if emotion in songs_dict:
        song_list = songs_dict[emotion]
        selected_song = random.choice(song_list)
        webbrowser.open(selected_song)
        return selected_song
    return None

def log_emotion(emotion, song):
    file_exists = os.path.isfile("emotion_log.csv")
    with open("emotion_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Emotion", "Song URL"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), emotion, song])

def capture_emotion():
    cap = cv2.VideoCapture(0)
    captured = False

    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Webcam error. Exiting.")
            break

        cv2.putText(frame, "Press 's' to capture | 'q' to quit", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.imshow("Mood Music Detector", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            captured = True
            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if not captured:
        return

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        detected = result[0]['dominant_emotion']
        mapped_emotion = emotion_map.get(detected, detected)

        song_url = play_song(mapped_emotion)
        if song_url:
            emoji_map = {
                "happy": "😊", "sad": "😢", "angry": "😠", "neutral": "😐", "fear": "😨"
            }
            status_label.config(text=f"Detected Emotion: {mapped_emotion.capitalize()} {emoji_map.get(mapped_emotion, '')}", fg="#2c3e50")
            song_link_label.config(text=song_url, fg="#3498db", cursor="hand2")
            song_link_label.bind("<Button-1>", lambda e: webbrowser.open(song_url))
            log_emotion(mapped_emotion, song_url)
        else:
            status_label.config(text="No song found for this emotion.", fg="red")
    except Exception as e:
        messagebox.showerror("Detection Failed", str(e))

# Initialize GUI
app = tk.Tk()
app.title("Mood Music Player 🎵")
app.geometry("550x400")
app.configure(bg="#f0f4f7")

# Title
title_label = tk.Label(app, text="Mood Music Player", font=("Helvetica", 24, "bold"), bg="#f0f4f7", fg="#2c3e50")
title_label.pack(pady=20)

# Capture Button
capture_btn = tk.Button(app, text="Capture Emotion 🎭", font=("Helvetica", 16), command=capture_emotion,
                        bg="#27ae60", fg="white", padx=20, pady=10, bd=0, relief="ridge")
capture_btn.pack(pady=10)

# Status Label
status_label = tk.Label(app, text="Your emotion will appear here.", font=("Helvetica", 14), bg="#f0f4f7", fg="#7f8c8d")
status_label.pack(pady=15)

# Song URL
song_link_label = tk.Label(app, text="", font=("Helvetica", 11, "underline"), bg="#f0f4f7", fg="#3498db")
song_link_label.pack()

# Exit Button
exit_btn = tk.Button(app, text="Exit", font=("Helvetica", 12), command=app.quit,
                     bg="#e74c3c", fg="white", padx=15, pady=5, bd=0, relief="ridge")
exit_btn.pack(pady=30)

app.mainloop()
