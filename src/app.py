class TodoApp:
    def __init__(self):
        self.zadania = []
    def dodaj_zadanie(self, zadanie):
        self.zadania.append(zadanie)
    def usun_zadanie(self, zadanie):
        self.zadania.remove(zadanie)