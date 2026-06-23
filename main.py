import os
import pygame
import customtkinter as ctk

class music_player:
    def __init__(self):
        self.is_loaded = False
        self.is_playing = False
        self.song_name = None

def song_change(music_player, new_name, play_button):
    music_player.is_loaded = False
    music_player.is_playing = False
    music_player.song_name = new_name
    play_button.configure(text = "Play")

def play_song(folder, player, button):
    
    file_path = os.path.join(folder, player.song_name)
    if (os.path.exists(file_path) == 0): #safety
        print("error with song file path")
        return

    if not (player.is_loaded):
        button.configure(text = "Pause")
        player.is_loaded = True
        player.is_playing = True
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()        
    elif (player.is_playing == 1):
        button.configure(text = "Unpause")
        player.is_playing = False
        pygame.mixer.music.pause()
    elif (player.is_playing == 0):
        button.configure(text = "Pause")
        player.is_playing = True
        pygame.mixer.music.unpause()

def main():

    song_player = music_player()

    try:
        pygame.mixer.init()
    except pygame.error: #safety
        print("error with pygame mixer") 
        return

    songs_folder = "songs"
    if not (os.path.isdir(songs_folder)): #safety
        print("error with songs folder") 
        return 
    
    songs_list = []
    for i in os.listdir(songs_folder):
        if (i.endswith(".ogg") or i.endswith(".mp3")):
            songs_list.append(i)

    #app window
    window = ctk.CTk()
    window.geometry("500x500")
    window.title("Music Player App")
    window.configure()
    window.config(background="#000000")

    #play button 
    play_button = ctk.CTkButton(window)
    play_button.configure(text = "Play", 
                          command = lambda: play_song(songs_folder, song_player, play_button)
                         )
    play_button.pack()

    #songs lists selection
    scroll_selection = ctk.CTkScrollableFrame(window)
    for i in songs_list:
        song_i = ctk.CTkButton(scroll_selection)
        song_i.configure(text = i, 
                         command = lambda local_song = i: song_change(song_player, local_song, play_button)
                        )
        song_i.pack()
    scroll_selection.pack()

    window.mainloop()

if (__name__ == "__main__"):
    main()
