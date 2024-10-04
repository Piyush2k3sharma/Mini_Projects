import customtkinter as ctk
from googletrans import Translator

window = ctk.CTk()
window.title("Google Translator")
window.geometry("900x600")

def switch_mode():
    if (ctk.get_appearance_mode()=='Light'):
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')

def lang_translation(lang):
    user_input = text_area.get(0.0,ctk.END)
    translator = Translator()
    result = translator.translate(user_input,dest=lang)
    Output_label.configure(text=result.text,fg_color=("#EEEEEE","#0F0F0F"))

heading = ctk.CTkLabel(window,text='Google Translator...',font=('Palatino Linotype',60,"bold"),
                       text_color=("#4535C1","#FFBF78"),padx=100)
heading.grid(row=1,column=1,columnspan=3,pady=30)

text_area = ctk.CTkTextbox(window,border_width=2,font=('Palatino Linotype',24,"bold"),width=860)
text_area.grid(row=2,column=1,columnspan=3,padx=20)

translate_btn = ctk.CTkButton(window,text="Translate text",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=250,height=40,
                           command=lambda : lang_translation('english'))
translate_btn.grid(row=3,column=1,pady=10)

hindi_btn = ctk.CTkButton(window,text="Hindi",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=250,height=40,
                           command=lambda : lang_translation('hindi'))
hindi_btn.grid(row=3,column=2,pady=10)

punjabi_btn = ctk.CTkButton(window,text="Punjabi",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=250,height=40,
                           command=lambda : lang_translation('punjabi'))
punjabi_btn.grid(row=3,column=3,pady=10)

Output_label_heading = ctk.CTkLabel(window,text="Translated text : ",font=('Palatino Linotype',24),
                           text_color=("#4C3BCF","#FFEEA9"))
Output_label_heading.grid(row=4,column=1,columnspan=3,pady=10)

Output_label = ctk.CTkLabel(window,text="",font=('Palatino Linotype',20),
                           text_color=("#4C3BCF","#FFEEA9"),corner_radius=10,wraplength=700)
Output_label.grid(row=5,column=1,columnspan=3,pady=10)

mode_change = ctk.CTkButton(window,text="Change",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=400,height=40,command=switch_mode)
mode_change.grid(row=0,column=1,pady=10,columnspan=3)

window.mainloop() 

# we can give the change mode functionality in two different functions using lambda functions...