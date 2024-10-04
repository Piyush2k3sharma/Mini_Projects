import customtkinter as ctk
from pytubefix import YouTube
from pytubefix.cli import on_progress

# read documentation of pytubefix...

window = ctk.CTk()
window.title("Youtube Dowloader")
window.geometry("870x500")

def download_video_file():
    link = user_input.get()
    try:
        yt = YouTube(link,on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        out_text = f"Downloaded Successfully!!\n\nTitle : {yt.title}\nDescription : {yt.description[:90]}..."
        video.download(r"C:\Users\ayush\Downloads")
        Output_label.configure(text=out_text)
    except Exception as e:
        Output_label.configure(text=e)

def download_audio_file():
    link = user_input.get()
    try:
        yt = YouTube(link, on_progress_callback =on_progress)
        out_text = f"Downloaded Successfully\n\nTitle : {yt.title}\n\nDescription : {yt.description[:90]}..."
        audio = yt.streams.get_audio_only()
        audio.download(r"C:\Users\ayush\Downloads",mp3=True)
        Output_label.configure(text=out_text)
    except Exception as e:
        Output_label.configure(text=f"ERROR : {e}")

# def switch_mode():
#     if (ctk.get_appearance_mode()=='Light'):
#         ctk.set_appearance_mode('dark')
#     else:
#         ctk.set_appearance_mode('light')

heading = ctk.CTkLabel(window,text='YouTube DownloadeR',font=('Palatino Linotype',64,"bold"),
                       text_color=("#4535C1","#FFBF78"),padx=100)
heading.grid(row=1,column=1,columnspan=2,pady=30)

sub_heading = ctk.CTkLabel(window,text="Paste Your link..",font=('Palatino Linotype',26),
                           text_color=("#4C3BCF","#FFEEA9"))
sub_heading.grid(row=2,column=1,columnspan=2)

user_input = ctk.CTkEntry(window,placeholder_text='Paste Your Link Here...',font=('Palatino Linotype',18,"bold")
                          ,width=550, height=40,
                          placeholder_text_color=("#4C3BCF","#FFEEA9"))
user_input.grid(row=3,column=1,columnspan=2,pady=20)

vid_download_btn = ctk.CTkButton(window,text="Download (Video)",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=400,height=40,command=download_video_file)
vid_download_btn.grid(row=4,column=1,pady=10)

aud_download_btn = ctk.CTkButton(window,text="Download (Audio)",fg_color=("#4535C1","#FFEEA9"),
                           font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
                           text_color=("#EEEEEE","#0F0F0F"),width=400,height=40,command=download_audio_file)
aud_download_btn.grid(row=4,column=2,pady=10)

# mode_change = ctk.CTkButton(window,text="Change",fg_color=("#4535C1","#FFEEA9"),
#                            font=('Palatino Linotype',24),hover_color=("#4C3BCF","#FFBF78"),
#                            text_color=("#EEEEEE","#0F0F0F"),width=400,height=40,command=switch_mode)
# mode_change.grid(row=5,column=1,pady=10)

Output_label = ctk.CTkLabel(window,text="",font=('Palatino Linotype',18),
                           text_color=("#4C3BCF","#FFEEA9"))
Output_label.grid(row=6,column=1,columnspan=2)

window.mainloop()