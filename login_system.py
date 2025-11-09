#𝗙𝗘𝗜𝗧𝗢 𝗣𝗢𝗥 𝗩𝗜𝗡𝗜𝗖𝗜𝗨𝗦 𝗦𝗔𝗡𝗧𝗢𝗦-𝗧𝗘𝗖𝗛
#𝑰𝑵𝑻𝑬𝑹𝑭𝑨𝑪𝑬 𝑪𝑶𝑴 𝑪𝑼𝑺𝑻𝑶𝑴𝑻𝑲𝑰𝑵𝑻𝑬𝑹

import customtkinter as ctk
from PIL import Image

def Validar_login():
    usuario = entry.get()
    senha = entry2.get()
    if usuario == 'Vinicius' and senha == '12345':
        LabelInv.configure(text= 'Login feito com sucesso!', text_color= 'green')
    else:
        LabelInv.configure(text= 'Usuário ou senha inválidos!', text_color= 'red')

app = ctk.CTk()
ctk.set_appearance_mode('dark')
app.title("Login")
app.geometry('300x300')
app.resizable(False, False)
imagem = ctk.CTkImage(Image.open("fundo.jpg"), size=(300, 300))
label_fundo = ctk.CTkLabel(app, image=imagem, text="")
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

label_usuraio = ctk.CTkLabel(app,text='Usuário')
label_usuraio.pack(pady=10)

entry = ctk.CTkEntry(app,placeholder_text='Digite seu nome')
entry.pack(pady=5)

campo_Senha = ctk.CTkLabel(app,text='Senha')
campo_Senha.pack(pady=2)

entry2 = ctk.CTkEntry(app,placeholder_text='Digite sua Senha')
entry2.pack(pady=2)
ctk.CTkButton(app, text='Login', command=Validar_login).pack(pady=10)

LabelInv = ctk.CTkLabel(app, text="")
LabelInv.pack(pady=10)

app.mainloop()
