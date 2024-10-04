import customtkinter as ctk
import wikipedia as wiki

ctk.set_appearance_mode('light')

window = ctk.CTk()
window.title("Wikipedia")
window.geometry("850x650")


def fetch_data():
    query = user_input.get() # same as input function...
    try:
        data = wiki.summary(query,sentences=2)
        output_label.configure(text=data,fg_color=("#BFF6C3","#AD88C6"))
    except:
        output_label.configure(text="No Data Found...")    

heading = ctk.CTkLabel(window,text='WikiPediA...',font=('Palatino Linotype',64,"bold"),
                       text_color=("#088C6F","#6643B5"),padx=100)
heading.pack(pady=30)

sub_heading = ctk.CTkLabel(window,text="Search below ",font=('Palatino Linotype',32,"italic"),
                           text_color=("#088C6F","#6643B5"))
sub_heading.pack()

user_input = ctk.CTkEntry(window,placeholder_text='Ex : IPhone',font=('Palatino Linotype',12,"bold")
                          ,width=400, height=40,
                          placeholder_text_color=("#088C6F","#6643B5"))
user_input.pack(pady=20)

search_btn = ctk.CTkButton(window,text=" Search ",fg_color=("#00DFA2","#AD88C6"),
                           font=('Palatino Linotype',24),hover_color=("#088C6F","#6643B5"),
                           width=400,height=40,command=fetch_data)
search_btn.pack()

output_label = ctk.CTkLabel(window,text="",font=('Palatino Linotype',32,"italic"),text_color=("#088C6F","#6643B5"),wraplength=700,corner_radius=15)
output_label.pack(pady=10)

window.mainloop() 

# task to print hello on gui...
