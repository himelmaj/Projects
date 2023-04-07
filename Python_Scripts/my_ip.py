import socket as s
import tkinter as tk

root = tk.Tk()
root.geometry('600x30')
font = ("Helvetica", 14)
root.resizable(False, False)
root.title('MY IP')
root.configure(background='black')


# Get host information
my_hostname = s.gethostname()
my_ip = s.gethostbyname(my_hostname)

tk.Label(root, text=f'Your Hostname is {my_hostname} and you address is {my_ip}', font=font, fg='green', bg='black', anchor='se').grid(row=0, column=0)
root.mainloop()





