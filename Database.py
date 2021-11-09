import sqlite3
class DBconnect:
    def __init__(self):
        self.db=sqlite3.connect("Covid.db")
        self.db.row_factory=sqlite3.Row
        self.db.execute("CREATE TABLE IF NOT EXISTS CovidDataBase ( Name text , Gender text, Fever text , Tired text ,Cough text , Breathing text , RunnyNose text , sorethroat text , Nasalcongestion text ,Diarrhea text)")
        self.db.commit()

    def Add(self,Gender,Fever,Tired,Cough,Breathing,RunnyNose,sorethroat,Nasalcongestion,Diarrhea):
        self.db.execute("INSERT  INTO CovidDataBase(Gender,Fever,Tired,Cough,Breathing,RunnyNose,sorethroat,Nasalcongestion,Diarrhea) values(?,?,?,?,?,?,?,?,?)",(Gender,Fever,Tired,Cough,Breathing,RunnyNose,sorethroat,Nasalcongestion,Diarrhea))
        self.db.commit()
        return "Request is submitted"
    

    def ListRequest(self):
        cursor=self.db.execute("SELECT * FROM CovidDataBase")
        record=cursor.fetchall()
        return record