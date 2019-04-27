import wave as we
import numpy as np
import matplotlib.pyplot as plt


def wavread(path):
    wavfile = we.open(path, "rb")
    params = wavfile.getparams()
    framesra, frameswav = params[2], params[3]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.frombuffer(datawav, dtype=np.short)
    datause.shape = -1, 2
    datause = datause.T
    time = np.arange(0, frameswav) * (1.0 / framesra)
    return datause, time


def main():
    global path
    path = input("music file path:")
    try:
        wavdata, wavtime = wavread(path)
        title = path + "'s frames"
        plt.title(title)
        plt.subplot(211)
        plt.plot(wavtime, wavdata[0], color="green")
        plt.subplot(212)
        plt.plot(wavtime, wavdata[1])
        plt.show()
    except:
        print("path wrong!")


if __name__ == "__main__":
    main()
