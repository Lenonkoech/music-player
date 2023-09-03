# -*- coding: utf-8 -*-
"""
@author: Lenon
"""
import os
from tkinter import*
from tkinter import filedialog
from pygame import mixer

root=Tk()
root.title('LenPlayer')
root.geometry('920x600+290+85')
root.config(bg='#002')
root.resizable(False,False)
mixer.init()
#icon and logo
def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def Play_Music(): 
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
def close():
    root.destroy()    
Label(root,text="@Lenon's Project",font='chiller 13',foreground='springgreen',background='#002').pack(side='bottom')
Music=PhotoImage(file='music icon.png')
Label(image=Music,bg='#002',bd=0).place(x=1,y=1)
Button(root,text='Play',bg='#002',fg='gold',font='forte 24',command=Play_Music).place(x=225,y=385)
Button(root,text='Stop',bg='#002',fg='gold',font='forte 22',command=mixer.music.stop).place(x=145,y=445)
Button(root,text='Resume\nPlay',bg='#002',fg='gold',font='forte 17',command=mixer.music.unpause).place(x=226,y=500)
Button(root,text='pause',bg='#002',fg='gold',font='forte 22',command=mixer.music.pause).place(x=319,y=445)
Button(root, text="Add Music", width=15,bd=0, height=2, font='forte 16 ',fg="goldenrod", bg="#002", command= Add_Music).place(x=580, y=100)
Button(root,text='Close\nApp',bg='#002001',fg='gold',font='chiller 16',command=close,bd=1).place(x=875,y=1)
Label(root, bg="#002").pack(padx=10, pady=50, side=RIGHT)
Frame_Music = Frame(root, bd=1, relief = RIDGE)
Frame_Music.place(x=510, y=145, width=400, height=450)
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",11), bg="#000", fg="lavender", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
root.mainloop()