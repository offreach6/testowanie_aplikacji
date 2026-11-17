from app import TodoApp

def test_dodaj_zadanie():
    app = TodoApp()
    app.dodaj_zadanie("Poćwiczyć w fl studio")
    
    assert len(app.zadania) == 1
    assert app.zadania[0] == "Poćwiczyć w fl studio"

def test_usun_zadanie():
    app = TodoApp()
    app.dodaj_zadanie("Iść na spacer")
    
    app.usun_zadanie("Iść na spacer")
    
    assert len(app.zadania) == 0