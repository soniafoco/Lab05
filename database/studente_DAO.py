# Add whatever it is needed to interface with the DB Table studente
from database import DB_connect
from database.DB_connect import get_connection
from model.studente import Studente

class StudenteDao:

    @staticmethod
    def get_iscritti_corso(codins):
        cnx = DB_connect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM iscrizione i, studente s WHERE i.codins = %s AND i.matricola = s.matricola"
            cursor.execute(query, (codins,))
            for row in cursor:
                result.append(Studente(row["matricola"],
                                    row["cognome"],
                                    row["nome"],
                                    row["CDS"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_studente_matricola(matricola):
        cnx = DB_connect.get_connection()
        if cnx is None:
            print("errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM studente s WHERE s.matricola = %s"
            cursor.execute(query, (matricola,))
            result = cursor.fetchone()
            if result is None:
                return
            student = Studente(result["matricola"], result["cognome"], result["nome"], result["CDS"])
            cursor.close()
            cnx.close()
            return student


    def add_studente_corso(matricola, codins):
        cnx = DB_connect.get_connection()
        if cnx is None:
            print("errore connessione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = "INSERT INTO iscrizione(matricola, codins) VALUES (%s, %s)"
            cursor.execute(query, (matricola, codins,))
            success = False
            try:
                cnx.commit()
                success = True
            except Exception as e:
                cnx.rollback()
            cursor.close()
            cnx.close()
            return success