# import tkinter
# from pygame import mixer

# mixer.init()
# mixer.music.load('play.mp3')
# mixer.music.play()
# mixer.music.stop()



from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self, windows):
        windows.geometry('320x100'); windows.title('Python Tiny Player'); windows.resizable(0,0)
        Load = Button(windows, text="Load", width=10, font= ('Times', 10), command= self.load)
        Play = Button(windows, text="Play", width=10, font= ('Times', 10), command= self.play)
        Pause = Button(windows, text="Pause", width=10, font= ('Times', 10), command= self.pause)
        Stop = Button(windows, text="Stop", width=10, font= ('Times', 10), command= self.stop)
        Load.place(x=0, y=20); Play.place(x=110, y=20); Pause.place(x=220, y=20); Stop.place(x=110, y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file= filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(slef):
        mixer.music.stop()

new_root = Tk()
player_app = Player(new_root)
new_root.mainloop()