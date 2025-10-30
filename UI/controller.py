import flet as ft
from UI.alert import AlertManager
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra(self, e):
        lista = self._model.get_automobili()
        self._view.lista_auto.controls.clear()
        for auto in lista:
            self._view.lista_auto.controls.append(ft.Text(str(auto)))
        self._view.lista_auto.update()

    def cerca(self, e, modello):
        if not modello:
            self._view.show_alert("modello non inserito")
            return
        lista = self._model.cerca_automobili_per_modello(modello)
        if not lista:
            self._view.show_alert("auto non trovata")
            self._view.lista_auto_ricerca.controls.clear()
            return
        self._view.lista_auto_ricerca.controls.clear()
        for auto in lista:
            self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto)))
        self._view.lista_auto_ricerca.update()