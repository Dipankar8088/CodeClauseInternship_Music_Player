# CodeClauseInternship_Music_Player

# Simple Music Player

A simple music player built in Python that allows users to play, pause, and stop music, as well as load and play all songs from a selected folder.

## Features

- *Play, Pause, Stop Controls*: Basic music playback controls to manage songs.
- *Select Folder*: Choose a folder from your computer, and the player will load and play all .mp3 and .wav files in that folder.
- *Sequential Playback*: Plays music files one after another from the selected folder.
- *Pause and Resume*: Pause the current song and resume it when needed.
- *Stop*: Stop the current song at any time.

## Technologies Used

- *Python*: Main programming language.
- *Tkinter*: For the graphical user interface (GUI).
- *pygame*: For audio playback and music control.
- *os* and *glob*: For directory traversal and file management.

## Installation

1. *Clone the repository:*

   bash
   git clone https://github.com/your-username/simple-music-player.git
   cd simple-music-player
   

2. *Install dependencies:*

   The project requires the pygame library for music playback. You can install it using pip:

   bash
   pip install pygame
   

3. *Run the application:*

   To launch the music player, run the Python script:

   bash
   python music_player.py
   

   The application will open a simple GUI where you can select a folder and interact with the music player.

## Usage

1. *Select Folder: Click the **Select Folder* button to choose a folder that contains music files (supports .mp3 and .wav formats).
2. *Play Music: After selecting a folder, click the **Play* button to start playing the first song in the folder.
3. *Pause Music: Click the **Pause* button to pause the current song.
4. *Stop Music: Click the **Stop* button to stop the current song and reset the player.

The music player will automatically play all supported music files from the folder in sequential order.

## Future Enhancements

- *Volume Control*: Implement a slider for controlling the volume.
- *Shuffle and Repeat*: Add options to shuffle the playlist or repeat a song.
- *Support More Formats*: Extend support for more audio file formats (e.g., .flac, .ogg).
- *Track Display*: Display the name of the currently playing song.
- *Playlist Functionality*: Allow users to create and save custom playlists.
