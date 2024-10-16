import customtkinter as ctk

window = ctk.CTk()
window.title('  JOKES')
window.geometry('800x600')

''' Color scheme '''

# dark mode -- Purple tone
D_PRIMARY_COLOR = "#2A033E"
D_SECONDARY_COLOR = "#42125B"
D_TERTIARY_COLOR = "#73428C"
D_TEXT_COLOR = "#E2A8FF"

# light mode
L_PRIMARY_COLOR = ""
L_SECONDARY_COLOR = ""
L_TERTIARY_COLOR = ""
L_TEXT_COLOR = ""

def update_radio_buttons(category):
    if category == "Custom":
        types_btn1.configure(state="normal")
        types_btn2.configure(state="normal")
        types_btn3.configure(state="normal")
        types_btn4.configure(state="normal")
        types_btn5.configure(state="normal")
        types_btn6.configure(state="normal")
    else:
        types_btn1.configure(state="disabled")
        types_btn2.configure(state="disabled")
        types_btn3.configure(state="disabled")
        types_btn4.configure(state="disabled")
        types_btn5.configure(state="disabled")
        types_btn6.configure(state="disabled")

def disp():
    category = category.get()
    amount = amount_input.get()
    joke_type = joke_type
    print(category)
    print(amount)
    print(joke_type)

'''Frame 1'''

frame_1 = ctk.CTkFrame(master=window,fg_color=D_PRIMARY_COLOR,corner_radius=0,height=600,width=200)
frame_1.place(x=0,y=0)

logo = ctk.CTkLabel(frame_1,height=150,width=200,fg_color=D_TERTIARY_COLOR,corner_radius=20)
logo.place(x=0,y=0)

category = ctk.CTkOptionMenu(frame_1,values=["Any","Custom"],fg_color=D_TERTIARY_COLOR,height=30,width=180,corner_radius=15,command=lambda event: update_radio_buttons(category.get()))
category.place(x=10,y=155)

# radiobuttongroup here for custom types
categ_val = ''
def on_select(value):
    categ_val = value

var1 = ctk.StringVar()
types_btn1 = ctk.CTkRadioButton(frame_1,text="Programming",variable=var1,command=lambda: on_select(var1.get()))
types_btn1.place(x=10,y=195)

types_btn2 = ctk.CTkRadioButton(frame_1,text="Misc",variable=var1,command=lambda: on_select(var1.get()))
types_btn2.place(x=10,y=220)

types_btn3 = ctk.CTkRadioButton(frame_1,text="Dark",variable=var1,command=lambda: on_select(var1.get()))
types_btn3.place(x=10,y=245)

types_btn4 = ctk.CTkRadioButton(frame_1,text="Pun",variable=var1,command=lambda: on_select(var1.get()))
types_btn4.place(x=10,y=270)

types_btn5 = ctk.CTkRadioButton(frame_1,text="Spooky",variable=var1,command=lambda: on_select(var1.get()))
types_btn5.place(x=10,y=295)

types_btn6 = ctk.CTkRadioButton(frame_1,text="Christmas",variable=var1,command=lambda: on_select(var1.get()))
types_btn6.place(x=10,y=320) 

update_radio_buttons("Any")

amount_label = ctk.CTkLabel(frame_1,text="Enter The Amount Of Jokes",
    fg_color=D_PRIMARY_COLOR,text_color=D_TEXT_COLOR,
    height=20,width=180,corner_radius=20)
amount_label.place(x=10,y=350)

amount_input = ctk.CTkEntry(frame_1, placeholder_text="Enter Amount here : ",fg_color=D_TERTIARY_COLOR,height=30,width=180,corner_radius=4)
amount_input.place(x=10,y=370)

joke_type = ''
def on_click(value):
    global joke_type
    joke_type = value

var2 = ctk.StringVar()

type_label = ctk.CTkLabel(frame_1,text="Select The Type of Jokes",
    fg_color=D_PRIMARY_COLOR,text_color=D_TEXT_COLOR,
    height=20,width=180,corner_radius=20)
type_label.place(x=10,y=405)

joke_type_btn1 = ctk.CTkRadioButton(frame_1,text="Single",variable=var2,command=lambda: on_click(var2.get()))
joke_type_btn1.place(x=10,y=430)

joke_type_btn2 = ctk.CTkRadioButton(frame_1,text="Two Part",variable=var2,command=lambda: on_click(var2.get()))
joke_type_btn2.place(x=10,y=455)

generate_btn = ctk.CTkButton(frame_1,text="Generate",fg_color=D_TERTIARY_COLOR,height=40,width=180,corner_radius=5,command=disp)
generate_btn.place(x=10,y=500)

'''Frame 2'''

frame_2 = ctk.CTkFrame(master=window,fg_color='#42125B',corner_radius=0,height=600,width=600)
frame_2.place(x=200,y=0)

joke_label = ctk.CTkLabel(frame_2,text="Here Is Your Joke",font=("Mongolian Baiti",48,"bold"),width=500,height=100)
joke_label.place(x=50,y=50)

text = '''
Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.

The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.

The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
'''

output_text = ctk.CTkTextbox(frame_2,width=530,height=400,corner_radius=10,
    text_color=D_TEXT_COLOR,fg_color=D_SECONDARY_COLOR)
output_text.insert('0.0',text)
output_text.configure(state="disabled")
output_text.place(x=35,y=160)

window.mainloop()

'''

Color pallete website - https://paletton.com/

'''