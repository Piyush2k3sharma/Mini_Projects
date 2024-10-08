import customtkinter as ctk

window = ctk.CTk()
window.title('  JOKES')
window.geometry('800x600')

frame_1 = ctk.CTkFrame(master=window,fg_color='red',corner_radius=0,height=600,width=200)
frame_1.place(x=0,y=0)

logo = ctk.CTkLabel(frame_1,height=150,width=200)
logo.place(x=0,y=0)

category = ctk.CTkOptionMenu(frame_1,values=["Any","Custom"])
category.place(x=0,y=200)

# radiobuttongroup here for custom types

amount_input = ctk.CTkEntry(frame_1, placeholder_text="Enter Amount here : ")
amount_input.place(x=0,y=100)

btn = ctk.CTkButton(frame_1,text="Generate")
btn.place(x=0,y=150)

frame_2 = ctk.CTkFrame(master=window,fg_color='blue',corner_radius=0,height=600,width=600)
frame_2.place(x=200,y=0)

label1 = ctk.CTkLabel(frame_2,text="Here is your joke")
label1.place(x=0,y=0)

text = '''
Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.

The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
'''

output_text = ctk.CTkTextbox(frame_2)
output_text.insert('0.0',text)
output_text.configure(state="disabled")
output_text.place(x=100,y=100)

window.mainloop()