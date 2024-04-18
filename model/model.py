from database.corso_DAO import CorsoDao
from database.studente_DAO import StudenteDao


class Model:
    def __init__(self):
        pass

    def get_all_corsi(self):
        return CorsoDao.get_all_corsi()

    def get_iscritti_corso(self, codins):
        return StudenteDao.get_iscritti_corso(codins)

    def get_studente_matricola(self, matricola):
        return StudenteDao.get_studente_matricola(matricola)

    def get_corsi_studente(self, matricola):
        return CorsoDao.get_corsi_studente(matricola)

    def add_studente_corso(self, matricola, codins):
        return StudenteDao.add_studente_corso(matricola, codins)