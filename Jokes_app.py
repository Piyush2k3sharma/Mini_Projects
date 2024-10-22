import customtkinter as ctk
from PIL import Image
import requests

window = ctk.CTk()
window.title('  JOKES')
window.geometry('800x600')
# ctk.set_appearance_mode('light')


''' Color scheme '''

# dark mode -- Purple tone
D_PRIMARY_COLOR = "#2A033E"
D_SECONDARY_COLOR = "#42125B"
D_TERTIARY_COLOR = "#73428C"
D_TEXT_COLOR = "#E2A8FF"

# light mode
L_PRIMARY_COLOR = "#FEB881"
L_SECONDARY_COLOR = "#FFCEA7"
L_TERTIARY_COLOR = "#DB8E51"
L_TEXT_COLOR = "#BB6B2C"



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

categ_dict = {
    '0' : "Programming",
    '1' : "Misc",
    '2' : "Dark",
    '3' : "Pun",
    '4' : "Spooky",
    '5' : "Christmas"
}

def get_info():
    if category.get()=='Any':
        categ = 'Any'
    else:
        categ = categ_dict[categ_val]
    if joke_type=="0":
        j_type = 'single'
    else:
        j_type = 'twopart'
    amnt = int(amount_input.get())
    return categ,j_type,amnt

def gen_joke():
    categ,j_type,amnt = get_info()
    
    url = f"https://v2.jokeapi.dev/joke/{categ}?type={j_type}&amount={amnt}"
    json_data = requests.get(url)
    jokes = json_data.json()
    jokes_text = ""

    if amnt==1:
        if jokes['type'] =='single':
            jokes_text = f"{jokes['joke']}\n"
        else:
            jokes_text += f"Setup : {jokes['setup']}\n"
            jokes_text += f"Delivery : {jokes['delivery']}\n"
    else:
        count = amnt
        for i in range(count):
            jokes_text += f"JOKE : {i+1}\n\n"
            if jokes['jokes'][i]['type']=='single':
                jokes_text += f"{jokes['jokes'][i]['joke']}\n\n"
            else:
                jokes_text += f"{jokes['jokes'][i]['setup']}\n\n"
                jokes_text += f"{jokes['jokes'][i]['delivery']}\n\n"

    output_text.insert('0.0',jokes_text)
    output_text.configure(state="disabled")


'''Frame 1'''

frame_1 = ctk.CTkFrame(master=window,fg_color=(L_PRIMARY_COLOR,D_PRIMARY_COLOR),corner_radius=0,height=600,width=200)
frame_1.place(x=0,y=0)

my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\ayush\OneDrive\Desktop\Netmaxx\Python files\Mini projects\images\10254401.png"),dark_image=Image.open(r"C:\Users\ayush\OneDrive\Desktop\Netmaxx\Python files\Mini projects\images\10254401.png"),size=(165, 165))

logo = ctk.CTkLabel(frame_1,height=150,width=200,fg_color=(L_PRIMARY_COLOR,D_PRIMARY_COLOR),image=my_image,text="",corner_radius=20)
logo.place(x=0,y=0)

category = ctk.CTkOptionMenu(frame_1,values=["Any","Custom"],fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                             button_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                             button_hover_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),dropdown_fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),dropdown_hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),height=30,width=180,corner_radius=15,hover=True,command=lambda event: update_radio_buttons(category.get()))
category.place(x=10,y=155)

# radiobuttongroup here for custom types
categ_val = None
def on_select(value):
    global categ_val
    categ_val = value

var1 = ctk.StringVar()
types_btn1 = ctk.CTkRadioButton(frame_1,text="Programming",variable=var1,value=0,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn1.place(x=10,y=195)

types_btn2 = ctk.CTkRadioButton(frame_1,text="Misc",variable=var1,value=1,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn2.place(x=10,y=220)

types_btn3 = ctk.CTkRadioButton(frame_1,text="Dark",variable=var1,value=2,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn3.place(x=10,y=245)

types_btn4 = ctk.CTkRadioButton(frame_1,text="Pun",variable=var1,value=3,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn4.place(x=10,y=270)

types_btn5 = ctk.CTkRadioButton(frame_1,text="Spooky",variable=var1,value=4,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn5.place(x=10,y=295)

types_btn6 = ctk.CTkRadioButton(frame_1,text="Christmas",variable=var1,value=5,
                                hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                border_width_checked=4,border_width_unchecked=2,
                                command=lambda: on_select(var1.get()))
types_btn6.place(x=10,y=320) 

update_radio_buttons("Any")

amount_label = ctk.CTkLabel(frame_1,text="Enter The Amount Of Jokes",
    fg_color=(L_PRIMARY_COLOR,D_PRIMARY_COLOR),text_color=(L_TEXT_COLOR,D_TEXT_COLOR),
    height=20,width=180,corner_radius=20)
amount_label.place(x=10,y=350)

amount_input = ctk.CTkEntry(frame_1, placeholder_text="Enter Amount here : ",fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),height=30,width=180,corner_radius=4)
amount_input.place(x=10,y=370)

joke_type = None
def on_click(value):
    global joke_type
    joke_type = value

var2 = ctk.StringVar()

type_label = ctk.CTkLabel(frame_1,text="Select The Type of Jokes",
    fg_color=(L_PRIMARY_COLOR,D_PRIMARY_COLOR),text_color=(L_TEXT_COLOR,D_TEXT_COLOR),
    height=20,width=180,corner_radius=20)
type_label.place(x=10,y=410)

joke_type_btn1 = ctk.CTkRadioButton(frame_1,text="Single",variable=var2,value=0,
                                    hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                    border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                    fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                    border_width_checked=4,border_width_unchecked=2,
                                    command=lambda: on_click(var2.get()))
joke_type_btn1.place(x=10,y=435)

joke_type_btn2 = ctk.CTkRadioButton(frame_1,text="Two Part",variable=var2,value=1,
                                    hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                                    border_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                    fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                                    border_width_checked=4,border_width_unchecked=2,
                                    command=lambda: on_click(var2.get()))
joke_type_btn2.place(x=10,y=460)

generate_btn = ctk.CTkButton(frame_1,text="Generate",
                            fg_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
                            hover_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
                            height=40,width=180,corner_radius=5,command=gen_joke)
generate_btn.place(x=10,y=500)

'''Frame 2'''

frame_2 = ctk.CTkFrame(master=window,fg_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),corner_radius=0,height=600,width=600)
frame_2.place(x=200,y=0)

joke_label = ctk.CTkLabel(frame_2,text="Here Is Your Joke",
                            font=("Mongolian Baiti",48,"bold"),text_color=(L_TEXT_COLOR,D_TEXT_COLOR),
                            width=500,height=100)
joke_label.place(x=50,y=50)

output_text = ctk.CTkTextbox(frame_2,width=530,height=400,corner_radius=10,
    text_color=D_TEXT_COLOR,fg_color=(L_SECONDARY_COLOR,D_SECONDARY_COLOR),
    scrollbar_button_color=(L_TERTIARY_COLOR,D_TERTIARY_COLOR),
    scrollbar_button_hover_color=(L_PRIMARY_COLOR,D_PRIMARY_COLOR),
    font=("Mongolian Baiti",24))
output_text.insert('0.0',text="")
output_text.place(x=35,y=160)

window.mainloop()

'''
Color pallete website - https://paletton.com/
Image logo link - https://www.freepik.com/free-psd/3d-emoji-isolated_133742319.htm#fromView=search&page=1&position=18&uuid=3f2b9d28-0797-454e-8cfe-761b7e381b24
'''