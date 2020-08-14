def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def unmutemusic():
    global currentvol
    root.MuteButton.grid()
    root.UnmuteButton.grid_remove()
    mixer.music.set_volume(currentvol)

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)

def stopmusic():
    mixer.music.stop()
    AudioStausLabel.configure(text='Stopped')

def pausemusic():
    mixer.music.pause()
    root.ResumeButton.grid()
    root.PauseButton.grid_remove()
    AudioStausLabel.configure(text='Paused')

def resumemusic():
    root.PauseButton.grid()
    root.ResumeButton.grid_remove()
    mixer.music.unpause()
    AudioStausLabel.configure(text='Playing...')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    AudioStausLabel.configure(text='Playing...')

def musicurl():
    try:
        dd=filedialog.askopenfilename(initaldir='C:Users/anant/OneDrive/Desktop/Audio',
                                      title='Select Audio File',
                                      filetype=(('.MP3','*.mp3'),'WAV','*.wav'))
    except:
        dd = filedialog.askopenfilename(title ='Select Audio File',filetype=(('.MP3','*.mp3'),('WAV','*.wav')))

    audiotrack.set(dd)

def createwidth():
    global iamplay,iamstop,iampause,iamvolumeup,iamvolumedown,iambrowse,iamresume,iammute,iamunmute,AudioStausLabel

    ################### Images Register #####################################################################
    iamplay = PhotoImage(file='play-button.png')
    iamstop = PhotoImage(file='stop.png')
    iampause = PhotoImage(file='pause-button.png')
    iamvolumeup = PhotoImage(file='volume-up.png')
    iamvolumedown = PhotoImage(file='volume-down.png')
    iambrowse = PhotoImage(file='searching.png')
    iamresume = PhotoImage(file='resume.png')
    iammute = PhotoImage(file='mute.png')
    iamunmute = PhotoImage(file='unmute.png')

    ################################ change size ############################################################
    iamplay = iamplay.subsample(18,18)
    iamstop = iamstop.subsample(18,18)
    iampause = iampause.subsample(18,18)
    iamvolumeup = iamvolumeup.subsample(18,18)
    iamvolumedown = iamvolumedown.subsample(18,18)
    iambrowse = iambrowse.subsample(18,18)
    iamresume = iamresume.subsample(18, 18)
    iammute = iammute.subsample(18, 18)
    iamunmute = iamunmute.subsample(18, 18)

    ################ Label #####,#############################################################################
    TrackLabel = Label(root,text='Select_Audio_Songs:', background='light sky blue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
    AudioStausLabel = Label(root,text='Paused', background='light sky blue',font=('arial',15,'italic bold'),width=20)
    AudioStausLabel.grid(row=2,column=2)

    ################### Entrybox ##############################################################################
    TrackLabelEntry = Entry(root,font=('arial',17,'italic bold'),width=38,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=2,padx=20,pady=20)

    #################### Buttons ###############################################################################
    BrowseButton = Button(root,text='Search',background='lawn green',font=('arial',9,'italic bold'),width=200,bd=5,activebackground='purple4',image=iambrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=3,padx=20,pady=20)
    PlayButton = Button(root, text='Play', background='green', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iamplay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)
    StopButton = Button(root, text='Stop', background='red', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iamstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)
    root.PauseButton = Button(root, text='Pause', background='yellow', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iampause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1, column=2, padx=20, pady=20)
    root.ResumeButton = Button(root, text='Resume', background='yellow', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iamresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1, column=2, padx=20, pady=20)
    root.ResumeButton.grid_remove()
    root.UnmuteButton = Button(root,text='Unmute',background='yellow',width=100,activebackground='purple4',bd=5,image=iamunmute,compound=RIGHT,command=unmutemusic)
    root.UnmuteButton.grid(row=3,column=3)
    root.MuteButton = Button(root,text='Mute',background='yellow',width=100,activebackground='purple4',bd=5,image=iammute,compound=RIGHT,command=mutemusic)
    root.MuteButton.grid(row=3,column=3)
    VolumeUpButton = Button(root, text='VolumeUp(+)', background='red', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iamvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1, column=3, padx=20, pady=20)
    VolumeDownButton = Button(root, text='VolumeDown(-)', background='red', font=('arial', 9, 'italic bold'), width=200,
                          bd=5, activebackground='purple4',image=iamvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2, column=3, padx=20, pady=20)

#####################################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.geometry("1100x500+200+50")
root.title("Music_Player")
root.iconbitmap('images.ico')
root.resizable(False,False)
root.configure(bg='light sky blue')

################################################ global variable ################################################
audiotrack=StringVar()
currentvol = 0

###################################### creating slider ################################################################
ss ='Developed by "Anant Prakash"'
count=0
text=''
SliderLabel = Label(root,text=ss,bg='light sky blue',font=('arial',30, 'italic bold'))
SliderLabel.grid(row=5, column=0, padx=20, pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidth()
root.mainloop()
