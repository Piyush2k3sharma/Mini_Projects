import customtkinter as ctk

window = ctk.CTk()
window.title('  JOKES')
window.geometry('800x600')

heading = ctk.CTkLabel(window,text="Jokes")
heading.pack(pady=5)

window.mainloop()