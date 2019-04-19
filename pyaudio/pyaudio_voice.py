import pyaudio
import wave
import sys
import tkinter
import tkinter.messagebox
import os
from playsound import playsound  

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000

file_name = ''

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def voice():
    try:
        audio_info.set("---录音开始---")

        frames = []

        for i in range(0, int(RATE / CHUNK * int(second_choose.get()))):
            data = stream.read(CHUNK)
            frames.append(data)

        audio_info.set("---录音结束---")

        stream.stop_stream()
        stream.close()
        p.terminate()

        global file_name
        file_name = file_choose.get()+choice.get()

        wf = wave.open('./'+file_name, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    except:
        tkinter.messagebox.showerror("wrong!", "input wrong!")


def play_voice():
    os.system(os.getcwd()+'/'+file_name)


top = tkinter.Tk()
audio_info = tkinter.StringVar()
choice = tkinter.StringVar()
choice.set(".mp3")

begin = tkinter.Button(top, text="begin", command=voice)
begin.pack()

second_label = tkinter.Label(top, text="seconds:")
second_label.pack()

second_choose = tkinter.Entry(top)
second_choose.pack()

file_label = tkinter.Label(top, text="filename:")
file_label.pack()

file_choose = tkinter.Entry(top)
file_choose.pack()

choose_mp3 = tkinter.Radiobutton(
    top, text=".mp3", variable=choice, value=".mp3")
choose_mp3.pack()
choose_wav = tkinter.Radiobutton(
    top, text=".wav", variable=choice, value=".wav")
choose_wav.pack()

get_voice = tkinter.Button(top, text="playback of audio", command=play_voice)
get_voice.pack()

info = tkinter.Entry(top, textvariable=audio_info)
info.pack()
audio_info.set('提示信息')


top.mainloop()
