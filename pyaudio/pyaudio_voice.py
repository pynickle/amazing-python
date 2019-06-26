import pyaudio
import wave
import sys
import tkinter
import tkinter.messagebox
import os
from playsound import playsound


def voice():
    try:
        audio_info.set("---录音开始---")
        top.update()

        frames = []

        for i in range(0, int(RATE / CHUNK * int(second_choose.get()))):
            data = stream.read(CHUNK)
            frames.append(data)

        audio_info.set("---录音结束---")
        top.update()

        stream.stop_stream()
        stream.close()
        p.terminate()

        global file_name
        file_name = file_choose.get() + choice.get()

        wf = wave.open("./" + file_name, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))
        wf.close()
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("wrong!", "input wrong!")


def play_voice():
    os.system(os.getcwd() + "/" + file_name)


def pyaudio_main():
    global audio_info, second_choose, file_choose, choice, top
    global CHUNK, FORMAT, CHANNELS, RATE
    global p, stream
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )
    top = tkinter.Tk()
    audio_info = tkinter.StringVar()
    choice = tkinter.StringVar()
    choice.set(".mp3")

    begin = tkinter.Button(top, text="begin", command=voice).pack()

    second_label = tkinter.Label(top, text="seconds:").pack()

    second_choose = tkinter.Entry(top).pack()

    file_label = tkinter.Label(top, text="filename:").pack()

    file_choose = tkinter.Entry(top).pack()

    choose_mp3 = tkinter.Radiobutton(
        top, text=".mp3", variable=choice, value=".mp3"
    ).pack()
    choose_wav = tkinter.Radiobutton(
        top, text=".wav", variable=choice, value=".wav"
    ).pack()

    get_voice = tkinter.Button(top, text="playback of audio", command=play_voice).pack()

    info = tkinter.Entry(top, textvariable=audio_info).pack()
    audio_info.set("提示信息")

    top.mainloop()


if __name__ == "__main__":
    pyaudio_main()
