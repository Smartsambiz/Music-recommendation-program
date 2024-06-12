import tkinter as tk
from tkinter import messagebox
import random
import pygame  # For playing audio

# Initialize pygame mixer
pygame.mixer.init()

# Define lists of gospel songs with local file paths for each genre
gospel_rock_recommendations = [
    {"title": "Shout to the Lord by Hillsong", "path": "songs/Rock/Shout-To-The-Lord-Hillsong-WorshipCeeNaija.com_.mp3"},
    {"title": "Mighty to Save by Hillsong", "path": "songs/Rock/Hillsong-mighty to save.mp3"},
    {"title": "Cornerstone by Hillsong", "path": "songs/Rock/Hillsong_Worship_-_Cornerstone_CeeNaija.com_.mp3"},
    {"title": "God's not dear by Newboys", "path": "songs/Rock/Gods not dead.mp3"}    
]

gospel_jazz_recommendations = [
    {"title": "Get back right by Lecrae", "path": "songs/Jazz/Lecrae_Zaytoven_-_Get_Back_Right_CeeNaija.com_.mp3"},
    {"title": "Jazzy Christmas by Samsong", "path": "songs/Jazz/Samsong_-_Jazzy_Christmas_CeeNaija.com_.mp3"},
    {"title": "Redeemed by Spirit Jazz", "path": "songs/Jazz/Spirit_Jazz_Quartet_-_Redeemed_CeeNaija.com_.mp3"},
    {"title": "Loruko Jesus by B_jazz", "path": "songs/Jazz/B_Jazz_-_Loruko_Jesu_CeeNaija.com_.mp3"}
]

gospel_classical_recommendations = [
    {"title": "How Great Thou Art by The Piano Guys", "path": "songs/Classical/Christian_Hymn_-_How_Great_Thou_Art_CeeNaija.com_.mp3"},
    {"title": "Grow as we go by The Piano Guys", "path": "songs/Classical/The_Piano_Guys_-_Grow_As_We_Go_Ft_Mat_Savanna_Shaw_CeeNaija.com_.mp3"},
    {"title": "The Hallelujah Chorus by Handel", "path": "songs/Classical/hallelujah-chorus-9MB.mp3"}
]

# Function to play a randomly selected song from the selected genre
def play_random_song(genre):
    if genre.lower() == "rock":
        songs = gospel_rock_recommendations
    elif genre.lower() == "jazz":
        songs = gospel_jazz_recommendations
    elif genre.lower() == "classical":
        songs = gospel_classical_recommendations
    else:
        messagebox.showinfo("Invalid Genre", "Sorry, the genre you entered is not supported.")
        return

    if songs:
        song = random.choice(songs)
        play_song(song)
    else:
        messagebox.showinfo("No Songs", "Sorry, no songs available for the selected genre.")

# Function to play the selected song
def play_song(song):
    recommendation_label.config(text="Playing: " + song["title"])
    root.update()
    pygame.mixer.music.load(song["path"])  # Load the song from local file path
    pygame.mixer.music.play()  # Play the song

# Function to handle the play button click event
def play_button_clicked():
    genre = genre_entry.get()
    play_random_song(genre)

# Set up the main application window
root = tk.Tk()
root.title("Gospel Music Player")

# Change the background color of the main window
root.configure(bg='yellow')

# Create and place the widgets
label = tk.Label(root, text="Enter the genre you want to listen to (rock, jazz, classical):", font=("Arial", 12))
label.pack(pady=10)

genre_entry = tk.Entry(root, font=("Arial", 12))
genre_entry.pack(pady=5)

play_button = tk.Button(root, text="Recommend and play Song", command=play_button_clicked, font=("Arial", 12))
play_button.pack(pady=10)

recommendation_label = tk.Label(root, text="", font=("Helvetica", 16))
recommendation_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
