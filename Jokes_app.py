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


'''Frame 1'''

frame_1 = ctk.CTkFrame(master=window,fg_color=D_PRIMARY_COLOR,corner_radius=0,height=600,width=200)
frame_1.place(x=0,y=0)

logo = ctk.CTkLabel(frame_1,height=150,width=200,fg_color=D_TERTIARY_COLOR,corner_radius=20)
logo.place(x=0,y=0)

category = ctk.CTkOptionMenu(frame_1,values=["Any","Custom"],fg_color=D_TERTIARY_COLOR,height=30,width=180,corner_radius=15)
category.place(x=10,y=155)

# radiobuttongroup here for custom types

amount_label = ctk.CTkLabel(frame_1,text="Enter The Amount Of Jokes",
    fg_color=D_PRIMARY_COLOR,text_color=D_TEXT_COLOR,
    height=20,width=180,corner_radius=20)
amount_label.place(x=10,y=200)

amount_input = ctk.CTkEntry(frame_1, placeholder_text="Enter Amount here : ",fg_color=D_TERTIARY_COLOR,height=30,width=180,corner_radius=4)
amount_input.place(x=10,y=220)

btn = ctk.CTkButton(frame_1,text="Generate",fg_color=D_TERTIARY_COLOR,height=40,width=180,corner_radius=5)
btn.place(x=10,y=270)

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