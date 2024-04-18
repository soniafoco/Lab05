import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corso = None
        self.btn_cerca_iscritti = None
        self.lst_result = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #Row 1
        self.dd_corso = ft.Dropdown(label="Corso", hint_text="Selezionare un corso", width=500, on_change=self._controller.leggi_corso)
        self.fill_dd_corso()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca corso",width=200, tooltip="Metodo per cercare gli studenti iscritti di un corso", on_click=self._controller.get_iscritti_corso)

        row1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[self.dd_corso, self.btn_cerca_iscritti])
        self._page.controls.append(row1)

        #Row 2
        self.txt_matricola = ft.TextField(label="Matricola", hint_text="Inserire la matricola", on_change=self._controller.leggi_matricola)
        self.txt_nome = ft.TextField(label="Nome", hint_text="Nome", read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", hint_text="Cognome", read_only=True)

        row2 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[self.txt_matricola, self.txt_nome, self.txt_cognome])
        self._page.controls.append(row2)

        #Row 3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente",width=200, tooltip="Metodo per cercare uno studente data la matricola", on_click=self._controller.get_studente_matricola)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi",width=200, tooltip="Metodo per cercare i corsi a cui è iscritto uno studente", on_click=self._controller.get_corsi_studente)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi",width=200, tooltip="Metodo per iscrivere uno studente ad un corso", on_click=self._controller.add_studente_corso)

        row3 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi])
        self._page.controls.append(row3)

        # Result
        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fill_dd_corso(self):
        corsi = self.controller.get_all_corsi()
        for corso in corsi:
            self.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
