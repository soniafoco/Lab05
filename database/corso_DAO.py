import _mysql_connector
from database import DB_connect
from database.DB_connect import get_connection
from model.corso import Corso

class CorsoDao:

    @staticmethod
    def get_all_corsi():
        cnx = DB_connect.get_connection()
        result =[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM corso"
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_corsi_studente(matricola):
        cnx = DB_connect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM iscrizione i, corso c WHERE i.matricola = %s AND i.codins = c.codins"
            cursor.execute(query, (matricola,))
            for row in cursor:
                result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cursor.close()
            cnx.close()
            return result