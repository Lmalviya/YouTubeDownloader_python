
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *



file_size = 0

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)

        # changing Btn text
        dBtn.config(text='Please Wait...')
        dBtn.config(state=DISABLED)

        path_to_save_file = askdirectory()
        if path_to_save_file is None:
            dBtn.config(text='Start Download')
            dBtn.config(state=NORMAL)
            return

        ob = YouTube(url)
        strms = ob.streams.filter(progressive=True, file_extension='mp4').first()
        file_size = strms.filesize
        showinfo("File Information", "{}\n Video Size : {:00.0f} MB \n Video Resolution : {}".format(strms.title,strms.filesize/(1024*1024), strms.resolution))

        # strms.download(path_to_save_file)
        print('done...')

        #changing btn texr again
        urlField.delete(0, END)

        # changing Btn text
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Downloaded Finished", "Downloaded successFully")
    except Exception as e:
        print(e)
        print('there is some error!!')
        # changing Btn text
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Downloaded Status", "There is Something Missing")


# creating new thread
def startDownloadThead():
    #creat thread
    thread = Thread(target=startDownload())
    thread.start()

# create GUI for app
main = Tk()

main.title('My Youtube Downloader')
main.iconbitmap('video-download-icon-png-16.ico')
main.geometry('500x600')

#heading icon
file = PhotoImage(file = 'video-download-icon-png-16.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side = TOP)

#url text field
urlField = Entry(main, font=('verdana', 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx =20)

#download Button
dBtn = Button(main, text='Start Download', font=("verdana", 18), command=startDownloadThead )
dBtn.pack(side=TOP, pady = 10)


main.mainloop()