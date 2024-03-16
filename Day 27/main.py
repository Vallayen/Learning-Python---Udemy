import tkinter

window = tkinter.Tk()
window.minsize(width=600, height=300)
window.title("Test")


def click3():
  button3.destroy()
  label = tkinter.Label(window, text='wow you actually fell for it twice')
  label.pack()
  button4.pack(side='bottom')
  
def click2():
  button2.destroy()
  label = tkinter.Label(window, text='just kidding, there is no real end')
  label.pack()
  button3.pack(side='bottom')
  

def click():
  button_test.destroy()
  label = tkinter.Label(window, text='haha, now you are stuck')
  label.pack()
  button2.pack(side='bottom')
  
#buttons
button_test = tkinter.Button(window, text="Click Me", command=click)
button2 = tkinter.Button(window, text="Its okay, this button will let you out", command=click2)
button3 = tkinter.Button(window, text="no for real this time...", command=click3)
button4 = tkinter.Button(window, text="click here to close this annoying window")  
  
  
  
  
  
button_test = tkinter.Button(window, text="Click Me", command=click)
button_test.pack(side='bottom')
#leave @ bottom
window.mainloop()