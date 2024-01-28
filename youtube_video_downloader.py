import pytube
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloading(url,file_save): # url--> youtube url & file_save---> path

    try:

        dump = YouTube(url) # -----> initilizing the url

        streams = dump.streams.filter(progressive=True,file_extension='mp4')

        # By the above line we can  download the highest quality of video & mp4 is the highest quality

        high_res = streams.get_highest_resolution() # getting the video with high resolution
        high_res.download(output_path = file_save)  # the download will start
        print("Download succesfully go and check")
    except Exception as e:
        print(e)
def video_path():

    folder = filedialog.askdirectory() # select the directory in which dierectory you wanna download video
    if folder:
        print(f"The video download in : {folder}")
    return folder
if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    save = video_path()

    if save:
        v_url = input("please enter the url: ")
        print("Download started")
        downloading(v_url,save)
    else:
        print("Unable to download")
