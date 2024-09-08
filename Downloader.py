from tkinter import *
import pytube as p
# creat main window 
downloader = Tk()
# change the title 
downloader.title("video downloader")

# set width and height for application
downloader.geometry("500x300")

# write text label 
the_text = Label(downloader,text="Past URL for video here : ",height=2,font=("arial",10))
the_text.pack() # place the text into the main windows

# input the url 
url = StringVar()

# creat the input for url 
url_input = Entry(downloader,width=40,font=("arial",15),textvariable=url)
url_input.pack()

# fun for processing
def down():
    # get the url 
    URL = url.get()
    p.YouTube(URL).streams.get_highest_resolution().download('Videos')
    exit()

# set the botton 
btDownload = Button(downloader,width=10,text="download",height=2,bg="#000000"
,fg="white",borderwidth=0,command=down)
btDownload.pack()
# Run app ifinitely 
downloader.mainloop()

