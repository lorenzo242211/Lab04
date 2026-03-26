import flet as ft

import controller as c #importo controller, gestisce tutti i casi e seleziona lingua e modalità come già visto nel lab 3
import view as v


def main(page: ft.Page):
    # Setup model, view, control according to MVC pattern
    view = v.View(page) #attivo view come visto a lezione
    controller = c.SpellChecker(view) #passo view a controller, in modo tale che ciò che l'utente sceglie inserisce dall'interfaccia possa passare ed essere gestito nel controller, "l'algoritmo vero del codice"
    view.setController(controller) #per gestire l'interfaccia
    view.add_content()
ft.app(target=main)