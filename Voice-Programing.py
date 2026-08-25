import threading
import speech_recognition as sr
import customtkinter as ctk
from tkinter.font import Font

recognizer = sr.Recognizer()
running = False


#DEVERIA GUARDAR SO O AUDIO
def ouvir():
    global running
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while running:
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=10)
                texto = recognizer.recognize_google(audio, language="pt-PT")
                #print(texto)
                decidir(texto)
            except sr.WaitTimeoutError:
                # Não falou nada
                pass
            except Exception as e:
                print(e)

def decidir(texto):
    if texto == "" or texto == " ":
        return None
    
    argu =  texto.split()
    prim= argu[0]
    
    opcoes = ["if", "while", "for", "will", "wild", "try"]
    opcao_E = ""
    for i in opcoes:
        if i == prim.lower() :
            opcao_E = i
            
    if opcao_E == "":
        print("Vou criar variavel")
        print(texto)
        print(prim +" = " + argu[2] )
        
    elif opcao_E == "if":
        print("Entrei no if com")
        print(texto)
        
    elif opcao_E[0] == "w":
        print("Entrei no while com")
        print(texto)
   
    elif opcao_E == "for":
        print("Entrei no for com")
        print(texto)
     
def iniciar():
    global running
    if not running:
        running = True
        threading.Thread(target=ouvir, daemon=True).start()

def parar():
    global running
    running = False


ctk.set_appearance_mode("System") 

ctk.set_default_color_theme("orange.json")

class Aplicação(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VoiceCoding")
        self.geometry("900x600")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        self.barra_Lateral = ctk.CTkFrame(self, width=200)
        self.barra_Lateral.grid(row=0,column=0,sticky="nsew", pady=10)
        
        self.aba_Principal = ctk.CTkTabview(self, width=400)
        self.aba_Principal.grid(row=0,column=1,sticky="nsew", padx=10, pady=10)
        self.aba_Principal.add("Principal")
        self.aba_Principal.add("Preferencias")
        self.aba_Principal.add("Configurações")
        
        #abas que vou criar
        self.abaLateral()
        self.abaPrincipal()
        self.abaPreferencias()
        self.abaSistema()
        
        
        self.criarPagina()
        
    
    def criarPagina(self):
        pass
        
    
    def abaLateral(self):
        self.titulo = ctk.CTkLabel(self.barra_Lateral, text="Selecione a linguagem de programação", font=ctk.CTkFont(size=15, weight="bold"))
        
        self.titulo.pack(pady=(30,10), padx=(20,20))
        
        #Tipo de Linguagem
        
        
       
        
        self.switch_Tema = ctk.CTkSwitch(self.barra_Lateral, text="Modo escuro")
        self.switch_Tema.pack(pady=(10,10), side="bottom")
        
    def abaPrincipal(self):
        
        paginaPrincipal = self.aba_Principal.tab("Principal")
        self.btn_Ouvir = ctk.CTkButton(self.barra_Lateral, text="Ouvir")
        self.btn_Ouvir.pack(pady=(10,10))
        
        self.btn_Parar = ctk.CTkButton(self.barra_Lateral, text="Para")
        self.btn_Parar.pack(pady=(10,10)) 
       
    
        
    def abaPreferencias(self):
        pass
            
    def abaSistema(self):
        pass
        
        
janela = Aplicação()
janela.mainloop()

#titulo = ctk.CTkLabel(text="Voice Code", font=Font(size=22, weight="bold", family="Arial"))
#titulo.pack(pady=(50,50), padx=(5,10))

#ctk.CTkButton(janela, text="Iniciar", command=iniciar).pack(pady=10)
#ctk.CTkButton(janela, text="Parar", command=parar).pack(pady=10)

