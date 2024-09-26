from file_downloader import download_file as dwld
import tkinter as tk

root= tk.Tk()
root.title('File Downloder')
root.geometry("500x200")

def buttonCall():
    url=urlInput.get()
    fname=filenameInput.get()
    print(f"Url:{url}\nFilename:{fname}")
    dwld(url, fname)
    

#label enter url
urlLabel=tk.Label(root, text="URL")
#urlLabel.pack(padx=10,pady=10)
urlLabel.grid(row=0,column=0)

#url entry
urlInput=tk.Entry(root)
#urlInput.pack(padx=20,pady=10)
urlInput.grid(row=0,column=1)

#label entry filename
filenameLabel=tk.Label(root,text='Filename')
filenameLabel.grid(row=1,column=0)

#filename entry
filenameInput=tk.Entry(root)
filenameInput.grid(row=1,column=1)

#button
downloadButton=tk.Button(root,text="download",command=buttonCall)
downloadButton.grid(row=2, column=1)

root.mainloop()
