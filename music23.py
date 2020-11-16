






from tkinter import *
from tkinter import filedialog
from pygame import mixer


mixer.init()
mixer.music.load('deadmouse.wav')
mixer.music.play()


mixer.music.pause()

mixer.music.unpause()

mixer.music.stop()




class MusicPlayer:
        def __init__(self, window ):
            window.geometry('320x100'); window.title('Music Player2.0'); window.config(background="blue")
            Load = Button(window, bg="cyan", text = 'Load', width = 10, font = ('Times', 10), command = self.load_song)
            Play = Button(window,bg="cyan", text = 'Play', width = 10,font = ('Times', 10), command = self.play_song)
            Pause = Button(window,bg="cyan", text = 'Pause', width = 10, font = ('Times', 10), command = self.pause_song)
            Stop = Button(window ,bg="cyan",text = 'Stop', width = 10, font = ('Times', 10), command = self.stop_song)
            Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=60,y=60)
            self.music_file = False
            self.playing_state = False

        def load_song(self):
            self.music_file = filedialog.askopenfilename()

        def play_song(self):
            if self.music_file:
                mixer.init()
                mixer.music.load(self.music_file)
                mixer.music.play()

        def pause_song(self):
             if not self.playing_state:
                mixer.music.pause()
                self.playing_state=True
             else:
                mixer.music.unpause()
                self.playing_state = False

        def stop_song(self):
            mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()