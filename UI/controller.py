import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._codins = None
        self._matricola = None

    def get_all_corsi(self):
        corsi = self._model.get_all_corsi()
        return corsi

    def get_iscritti_corso(self, e):
        if self._codins is None:
            self._view.create_alert("Selezionare un corso!")
            return
        studenti = self._model.get_iscritti_corso(self._codins)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Ci sono {len(studenti)} nel corso:"))
        for studente in studenti:
            self._view.lst_result.controls.append(ft.Text(studente.__str__()))
        self._view.update_page()

    def get_studente_matricola(self, e):
        if self._matricola is None:
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.get_studente_matricola(self._matricola)
        if studente is None:
            self._view.create_alert("Non esiste uno studente con quella matricola!")
            return
        self._view.txt_nome.value = studente.nome
        self._view.txt_cognome.value = studente.cognome
        self._view.update_page()

    def get_corsi_studente(self, e):
        if self._matricola is None:
            self._view.create_alert("Inserire una matricola!")
            return
        corsi = self._model.get_corsi_studente(self._matricola)
        if len(corsi) is None:
            self._view.create_alert("Non esiste uno studente con quella matricola!")
            return
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi"))
        for corso in corsi:
            self._view.lst_result.controls.append(ft.Text(corso.__str__()))
        self._view.update_page()

    def add_studente_corso(self, e):
        if self._matricola is None:
            self._view.create_alert("Inserire una matricola!")
            return
        if self._codins is None:
            self._view.create_alert("Inserire un corso!")
            return
        studente = self._model.get_studente_matricola(self._matricola)
        if studente is None:
            self._view.create_alert("Non esiste uno studente con quella matricola!")
            return

        success = self._model.add_studente_corso(self._matricola, self._codins)
        if success:
           self._view.create_alert("Studente iscritto con successo")
        else:
            self._view.create_alert("Errore durante l'iscrizione")
        self._view.update_page()

    def leggi_corso(self, e):
        self._codins = self._view.dd_corso.value

    def leggi_matricola(self, e):
        self._matricola = self._view.txt_matricola.value