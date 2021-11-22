import tkinter as tk
from tkinter import messagebox, filedialog
from signer_verifier import Signer
from rsa import encrypt_number

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.signer = Signer('primes.txt', True)

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

    self.signBtn = tk.Button(botFrame, text='Sign Text', width=20, command=self.signFile)
    self.signBtn.grid(row=0, column=0, sticky='nsew')

    self.validBtn = tk.Button(botFrame, text='Validate', width=20, command=self.validateText)
    self.validBtn.grid(row=0, column=1, sticky='nsew')

    self.importBtn = tk.Button(botFrame, text='Import File', width=20, command=self.importFile)
    self.importBtn.grid(row=0, column=2, sticky='nsew')

  # util
  def importFile(self):
    file = filedialog.askopenfile(mode='r')
    fileContent = file.read()
    self.inputText.delete('0.0', 'end')
    self.inputText.insert('0.0', fileContent)

  def signFile(self):
    file = self.inputText.get('0.0', 'end-1c')
    signed, ofile = self.signer.signFile(False, file, encryption_function=encrypt_number)
    self.signedText.config(state="normal")
    self.signedText.delete("0.0", "end")
    self.signedText.insert("0.0", signed)
    self.signedText.config(state="disabled")
    
  def validateText(self):
    file = filedialog.askopenfilename(filetypes=[('Files', '*')])
    validationResult = self.signer.validateSign(file)
    
    if validationResult:
      tk.messagebox.showinfo('Result','Valid')
    else:
      tk.messagebox.showinfo('Result','Invalid')

if __name__=='__main__':
  app = App()
  app.mainloop()