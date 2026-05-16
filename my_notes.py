import tkinter as tk


#create the main window
#Tk() is a class and window is the object
window = tk.Tk()
window.title("My EEE Notebook")
window.geometry('900x600')
window.configure(bg="#1e1e1e")

#sidebar frame inside window(parent)
sidebar = tk.Frame(window, bg="#252526", width=200)
#pack() - dispalys the object by geometrically positioning it
sidebar.pack(side='left', fill='y')
tk.Label(sidebar, text='My Notebook', bg="#252526", fg="#ffffff",font=('Ariel', 13)).pack(pady=20, padx=16)

#main frame inside window(parent)
main = tk.Frame(window, bg="#1e1e1e")
main.pack(side='left', fill='both', expand=True)

topics = ['Charge', 'Conductors', 'Voltage', 'Current', 'Resistance']

content = {
    "Charge": 'is defined as number of electrons times value of one electron',
    "Conductors": '',
    "Voltage": 'is the '
}

def show_topic(topic):
    for label in main.winfo_children():
        label.destroy()
    

    tk.Label(main, text=topic, bg='#1e1e1e', fg='#ffffff', font=('Arial', 20)).pack(pady=20)
    tk.Label(main, text=content.get(topic, "coming soon..."), bg='#1e1e1e', fg='#aaaaaa', font=('Arial', 12)).pack(pady=10)


for topic in topics:
    label = tk.Label(
        sidebar, 
        text=topic, 
        bg='#252526',
        fg='#aaaaaa',
        font=('Arial', 11),
        padx=16,
        pady=8,
        anchor='w')
    label.pack(fill='x')
    label.bind("<Button-1>", lambda e, t=topic: show_topic(t))



#shows the window as a loop
window.mainloop()