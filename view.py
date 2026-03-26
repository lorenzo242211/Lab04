import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.tendinaRicerca = None
        self.tendinaLingua = None
        self.testoIn = None
        self.lv = None
        self.page = page
        self.page.title = "TdP 2026 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page


    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        # Add your stuff here
        #riga1
        self.tendinaLingua = ft.Dropdown( expand=True, label= "Scegli la lingua", value= "", options=[
            ft.dropdown.Option(text = "Italiano", key = "italian"),
            ft.dropdown.Option(text = "Inglese", key = "english"),
            ft.dropdown.Option(text = "Spagnolo", key = "spanish")]) #capire come gestire e salvare selezione
        riga1 = ft.Row(controls=[self.tendinaLingua], alignment=ft.MainAxisAlignment.START)

        #riga2
        self.tendinaRicerca = ft.Dropdown(width=200, label="Modalità di ricerca", options=[
            ft.dropdown.Option(text = "Default", key = "Default"),
            ft.dropdown.Option(text = "Lineare", key = "Linear"),
            ft.dropdown.Option(text = "Dicotomica", key = "Dichotomic")])
        self.testoIn = ft.TextField(expand= True, label="Inserisci testo")

        # Questa è la funzione che "reagisce" al click e associa i nuovi valori dell'UI al metodo
        def gestisci_click(evento):
            # 1. Quando scatta l'evento, andiamo a leggere i valori inseriti dall'utente
            testo = self.testoIn.value
            lingua = self.tendinaLingua.value
            ricerca = self.tendinaRicerca.value
            #gestisco eccezioni semplici, return vuoto che permette di uscire dal metodo
            if not lingua:
                self.lv.controls.append(ft.Text("Attenzione: Lingua non selezionata!", color="red"))
                self.update()
                return
            if not ricerca:
                self.lv.controls.append(ft.Text("Attenzione: Modalità di ricerca non selezionata!", color="red"))
                self.update()
                return
            if not testo.strip():
                self.lv.controls.append(ft.Text("Attenzione: Inserisci del testo prima di avviare!", color="red"))
                self.update()
                return
            sbagliate, tempo = self.__controller.handleSentence(testo, lingua, ricerca) #il metodo restituisce lista parole sbagliate e tempo di ricerca
            self.lv.controls.append(ft.Text("Frase digitata dall'utente: " + testo))
            if len(sbagliate) > 3:
                self.lv.controls.append(ft.Text("Parole sbagliate: " + sbagliate , color="blue"))
            elif len(sbagliate) == 3: # " - " la stringa vuota di parole sbagliate è proprio spazio tratto spazio --> len 3
                self.lv.controls.append(ft.Text("Parola sbagliate: Nessuna", color = "blue"))
            self.lv.controls.append(ft.Text(f"Il tempo impiegato per la ricerca '{ricerca} è: {tempo:.4f}\n"
                                            f"----------------------------------------------------------------", color = "green"))
            self.testoIn.value = ""
            self.update()

        self.avviaSpell = ft.ElevatedButton(width=170, text="Avvia Spell Check", on_click= gestisci_click)
        #avvio handleSentece e gli passo i valori di testoIn, modalità ricerca e lingua

        riga2 = ft.Row(controls=[self.tendinaRicerca, self.testoIn, self.avviaSpell],alignment=ft.MainAxisAlignment.START)


        #riga 3 è la list view, ovvero la finestra che stampa ciò che ha fatto il programma
        #ovviamente viene richiamata dal controller ovvero stampa solo all'evenienza da codice
        self.lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


        self.page.add(riga1, riga2, self.lv)
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller): #viene usato direttamente nel main, controller e view si "parlano" grazie al main; diverso da come visto a lezione
        self.__controller = controller #in questo caso controller è passato come classe parametro nel metodo richiamato nel main, nel quale importo sia view che controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
