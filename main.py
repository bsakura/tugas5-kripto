import tkinter as tk
from tkinter import filedialog

def openFile():
  filePath = filedialog.askopenfilename(filetypes=[('File', '*')])
  if filePath is not None:
    pass
  return filePath

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('Tugas 5 Kripto')
    self.resizable(False, False)

    # top
    topFrame = tk.Frame(self, padx=25, pady=15)
    topFrame.grid(row=0, column=0)

    self.inputLabel = tk.Label(topFrame, text='Input')
    self.inputLabel.grid(row=0, column=0, sticky='n')
    self.inputText = tk.Text(topFrame, height=25, width=30)
    self.inputText.grid(row=1, column=0)

    self.signedLabelText = tk.StringVar()
    self.signedLabelText.set('Signed Text')
    self.signedLabel = tk.Label(topFrame, textvariable=self.signedLabelText)
    self.signedLabel.grid(row=0, column=1, sticky='n')
    self.signedText = tk.Text(topFrame, height=25, width=30, state='disabled')
    self.signedText.grid(row=1, column=1)


    # bottom
    botFrame = tk.Frame(self, padx=25, pady=15)
    botFrame.grid(row=1, column=0)

    self.signBtn = tk.Button(botFrame, text='Sign Text', width=25)
    self.signBtn.grid(row=0, column=0, sticky='nsew')

    self.validBtn = tk.Button(botFrame, text='Check Text', width=25)
    self.validBtn.grid(row=0, column=1, sticky='nsew')

    self.importBtn = tk.Button(botFrame, text='Import File', width=25)
    self.importBtn.grid(row=1, column=0, sticky='nsew')

    self.importKeyBtn = tk.Button(botFrame, text='Import Key', width=25)
    self.importKeyBtn.grid(row=1, column=1, sticky='nsew')

if __name__=='__main__':
  app = App()
  app.mainloop()