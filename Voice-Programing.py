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


ctk.set_appearance_mode("Dark") 
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
        self.aba_Principal.add("Preferências")
        self.aba_Principal.add("Sistema")
        
        #abas que vou criar
        self.abaLateral()
        self.abaPrincipal()
        self.abaPreferencias()
        self.abaSistema()
        
        
    def abaLateral(self):
        self.titulo = ctk.CTkLabel(self.barra_Lateral, 
                                   text="VoiceCode", 
                                   font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo.pack(pady=(30,10), padx=(20,20))
        
        #Tipo de Linguagem
        self.tipo_Linguagem = ctk.IntVar(value=0)
        radiolabel = ctk.CTkLabel(self.barra_Lateral, text="Selecione a linguagem de programação")
        self.radio_Python = ctk.CTkRadioButton(self.barra_Lateral, text="Python",
                                               variable=self.tipo_Linguagem,
                                               value=1)
        
        self.radio_Java = ctk.CTkRadioButton(self.barra_Lateral, text="Java",
                                               variable=self.tipo_Linguagem,
                                               value=2)
        radiolabel.pack()
        self.radio_Python.pack(pady=10)
        self.radio_Python.select()
        self.radio_Java.pack(pady=10)
        
        btn_Testar_Microfone = ctk.CTkButton(self.barra_Lateral,
                                            text="Testar Microfone",
                                            font=ctk.CTkFont(size=15),
                                            command=self.ir_para_Sistema)
        btn_Testar_Microfone.pack(pady=10, padx=10)
        
        self.switch_Tema = ctk.CTkSwitch(self.barra_Lateral, text="Modo escuro",
                                         command=self.mudarDarkMode)
        self.switch_Tema.pack(pady=(10,10), side="bottom")
        self.switch_Tema.select()
        
    def abaPrincipal(self):
        
        paginaPrincipal = self.aba_Principal.tab("Principal")
        
        texto="Ouvir"
        self.btn_Ouvir = ctk.CTkButton(paginaPrincipal, text=texto,
                                       width=200, height=40, 
                                       fg_color="red", 
                                       hover_color="darkred")
        
        self.btn_Ouvir.pack(pady=(10,10))
        
        self.Text_Viewer = ctk.CTkLabel(paginaPrincipal, height=150, width= 200)
        self.Text_Viewer.pack(pady=10,padx=10)

        #self.btn_Parar = ctk.CTkButton(paginaPrincipal, text=texto)
        #self.btn_Parar.pack(pady=(10,10)) 
        
    def abaPreferencias(self):
        paginaPreferencias = self.aba_Principal.tab("Preferências")
        
        label_Idiomas = ctk.CTkLabel( paginaPreferencias, text="Selecione o idioma:")
        label_Idiomas.pack(pady=(20,10))
        
        menu_Idiomas = ctk.CTkOptionMenu( paginaPreferencias, values=["Português","Ingles","Espanhol"])
        menu_Idiomas.pack(pady=(0,10))
        
        label_Volume = ctk.CTkLabel(paginaPreferencias , text="Volume do sistema:")
        label_Volume.pack(pady=(10,5))
        
        self.slider_Volume = ctk.CTkSlider(paginaPreferencias, 
                                           from_=0,
                                           to=100,
                                           command=self.mudarVolume)
        self.slider_Volume.pack(pady=(20,10))
        self.slider_Volume.set(50)
        
        self.label_Value_Volume = ctk.CTkLabel(paginaPreferencias, text="50%")
        self.label_Value_Volume.pack()
            
    def abaSistema(self):   
        paginaSistema = self.aba_Principal.tab("Sistema")
        
        label_Select_Micro = ctk.CTkLabel(paginaSistema , 
                                          text="Selecione um microfone:",
                                          font=ctk.CTkFont(size=15))
        label_Select_Micro.pack(pady=(20,10))
        
        menu_Microfone = ctk.CTkOptionMenu( paginaSistema, 
                                           values=["Microfone default",
                                                   "microfone externo1",
                                                   "Microfone externo2"])
        menu_Microfone.pack(pady=(0,10))
        
        
        label_Testar_Microfone = ctk.CTkLabel(paginaSistema,
                                              text="Testar Microfone",
                                              font=ctk.CTkFont(size=15))
        label_Testar_Microfone.pack(pady=(10,10))
        
        
        progress_Micro = ctk.CTkProgressBar(paginaSistema, width=500)
        
        progress_Micro.pack(pady=(10,20))
        progress_Micro.set(0)
        
        btn_Testar_Micro = ctk.CTkButton(paginaSistema, 
                                        text="Iniciar Teste", 
                                        width=200,
                                        height=50)
        btn_Testar_Micro.pack()

    def ir_para_Sistema(self):
        self.aba_Principal.set("Sistema")
        
    def mudarDarkMode(self):
        if self.switch_Tema.get() == 1:
            ctk.set_appearance_mode("Dark") 
        else:
            ctk.set_appearance_mode("Light") 
            
    def mudarVolume(self, novo_valor):
        self.label_Value_Volume.configure(text=f"{int(novo_valor)}%")
       
       
    
        
janela = Aplicação()
janela.mainloop()
