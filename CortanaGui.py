from tkinter import *
from Cortana import get_data

#creating window
master = Tk()
master.title("Cortana")
master.minsize(1200, 600)
master.maxsize(1200, 600)

#creating data fetcher
tosearch = StringVar()
SearchLabel = Label(master, text="what do you want to search about master? : ")
SearchLabel.grid(row=0)
SearchEntry = Entry(master, width=40)
SearchEntry.grid(row=1)

#processing data
def Search():
    try:
        dataCanvas.delete('1.0', END)
        tosearch = SearchEntry.get()
        title, data = get_data(tosearch)
        dataCanvas.insert(INSERT, "\t\t\t\t\t\t\t\t{}\n\n".format(title.upper()))
        for onedata in data:
            if onedata is not None:
                if onedata.name == 'h2':
                    dataCanvas.insert(INSERT , "\n\t\t\t\t\t\t\t\t{}\n\n".format(onedata.text.upper()))
                elif onedata.name == 'p':
                    dataCanvas.insert(INSERT, onedata.text)
                else:
                    continue
    except TypeError as e:
        print(e)
        dataCanvas.insert(INSERT, "data load failed\n")

#creating search button
SearchButton = Button(master, text='Search', command=Search)
SearchButton.grid(row=2)

#creating text box
dataCanvas = Text(master, height=30, width = 147)
dataCanvas.config(state="normal")
dataCanvas.grid(row=3, column=0)

#creating scrollbar
dataCanvasScrollBar = Scrollbar(master)
dataCanvasScrollBar.grid(row=3, column=1, rowspan=25, sticky='ns')

#attaching list box and scrollbar
dataCanvas.configure(yscrollcommand=dataCanvasScrollBar.set)
dataCanvasScrollBar.config(command=dataCanvas.yview)
