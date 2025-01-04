import tkinter as tk
from tkinter import filedialog
import pygame
import os
import glob
from time import sleep

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x200")

        # Initialize Pygame Mixer for music playback
        pygame.mixer.init()

        # Initialize state variables
        self.is_playing = False
        self.is_paused = False
        self.song_list = []
        self.current_song_index = -1

        # GUI Elements
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

    def select_folder(self):
        """Allow user to select a folder and load all music files."""
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Get all .mp3 and .wav files in the selected folder
            self.song_list = glob.glob(os.path.join(folder_path, "*.mp3")) + \
                             glob.glob(os.path.join(folder_path, "*.wav"))
            if self.song_list:
                self.current_song_index = 0
                print(f"Loaded {len(self.song_list)} songs.")
            else:
                print("No valid music files found.")

    def play_music(self):
        """Play or resume the current song."""
        if self.current_song_index == -1:
            print("No songs loaded. Please select a folder.")
            return

        if not self.is_playing:
            song = self.song_list[self.current_song_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"Playing: {os.path.basename(song)}")
            self.play_button.config(text="Pause")  # Change the play button to Pause
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.play_button.config(text="Pause")  # Update button to show Pause
            print("Resumed playing.")

    def pause_music(self):
        """Pause the current song."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.play_button.config(text="Play")  # Change the button back to Play
            print("Paused music.")

    def stop_music(self):
        """Stop the current song."""
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.is_paused = False
            self.play_button.config(text="Play")  # Reset play button to Play
            print("Stopped music.")

    def next_song(self):
        """Play the next song in the list."""
        if self.current_song_index < len(self.song_list) - 1:
            self.current_song_index += 1
        else:
            self.current_song_index = 0  # Loop back to the first song
        self.play_music()

    def prev_song(self):
        """Play the previous song in the list."""
        if self.current_song_index > 0:
            self.current_song_index -= 1
        else:
            self.current_song_index = len(self.song_list) - 1  # Loop back to the last song
        self.play_music()

    def play_all_songs(self):
        """Play all songs sequentially."""
        if self.song_list:
            for song in self.song_list:
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(30)
                sleep(1)  # Wait a bit before starting the next song
            print("All songs have been played.")

# Create the main window
root = tk.Tk()

# Initialize the music player
player = MusicPlayer(root)

# Start the main event loop
root.mainloop()
