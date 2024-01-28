import customtkinter as ctk
import os

def path_to_files():
    root = ctk.CTk()
    PATH = os.path.abspath(ctk.filedialog.askdirectory())
    root.destroy()
    return PATH

def get_titrino_data():
    PATH = path_to_files()
    files = os.listdir(PATH)
    
    titrino_files = []
    for file in files:
        titrino_files.append(os.path.join(PATH, file))

    return titrino_files

def extract_titrino_data():
    
    global frame1

    files = get_titrino_data()
    resultados = []

    DIRNAME = os.path.dirname(os.path.dirname(files[0]))
    FOLDER = os.path.basename(os.path.dirname(files[0]))
    OUTPUT_PATH = os.path.join(DIRNAME, f"Resultado da titulação - {FOLDER}.txt")

    for file in files:
        if not ".ini" in file:
            with open(file, 'r', encoding="windows-1252") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if "Sample" in line:
                        amostra = lines[i+1].split()[0]
                    if "Results" in line:
                        valor = lines[i+2].split()[:4]
            resultados.append(" ".join([amostra, valor[0], valor[1], valor[2], valor[3]]))
    
    with open(OUTPUT_PATH, 'w') as f2:
        for resultado in resultados:
            f2.write(resultado)
            f2.write("\n")
    
    ctk.CTkLabel(frame1, text=f"Done! Check output folder.", font=("Roboto", 14),
                 bg_color='black', fg_color="transparent").pack(pady=5)

    return None


app = ctk.CTk()

app.title("Titration analysis") 
app.geometry("400x200+10+10")
# app.minsize(width=600, height=400)
app.resizable(width=True, height=True)

# Title frame
frame0 = ctk.CTkFrame(master=app, corner_radius=0, border_color=None, height=50, bg_color='black', fg_color="transparent")
frame0.pack(fill='both', expand=True)

# App title
welcome = ctk.CTkLabel(frame0, text="Titration analysis", 
                       font=("Roboto bold", 28), text_color='white', bg_color='black', fg_color="transparent")
welcome.pack(padx=1, pady=5)

welcome2 = ctk.CTkLabel(frame0, text="Get titration results of Metrohm Titrino 848", 
                        font=("Roboto", 14), text_color='white', bg_color='black', fg_color="transparent")
welcome2.pack(padx=1, pady=5)

# Frame with descriptions
frame1 = ctk.CTkFrame(master=app, corner_radius=0, border_color=None, 
                      bg_color='black', fg_color="transparent")
frame1.pack(fill='both', expand=True)

# Choose directory btn
choose_dir = ctk.CTkButton(frame1, text="Choose a directory", 
                           fg_color="#E8DFF5", hover_color="#d4afb9", text_color="black", command=extract_titrino_data)
choose_dir.pack()

# Close button
ctk.CTkButton(master=frame1, width=75, text="Quit", command=app.destroy, 
              fg_color="#E8DFF5", hover_color="#d4afb9", text_color='black').pack(pady=5)

app.mainloop()