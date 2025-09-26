import tkinter as tk
# widgets are gui things like buttons textboxes etc 
# window is the the container for all that
window = tk.Tk() #instantiate the instance of a window
window.title("password generator")
window.geometry("1080x1080")
label = tk.Label(window , text="welcome to the free password generator")
label.pack(pady=30)




window.mainloop()