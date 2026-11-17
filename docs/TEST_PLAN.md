---

### 2. Plik `TEST_PLAN.md` (Plan testów)

```markdown
# Plan Testów – Aplikacja ToDo

## 1. Cel testów
Celem planu testów jest weryfikacja poprawności działania kluczowych funkcji zarządzania listą zadań w klasie `TodoApp` za pomocą frameworka PyTest.

## 2. Środowisko testowe
- **Język:** Python 3.x
- **Narzędzie testowe:** PyTest
- **System kontroli wersji:** Git / GitHub (GitHub Actions do automatyzacji)

## 3. Przypadki testowe

| ID Testu | Nazwa funkcji / testu | Opis działania | Oczekiwany rezultat |
| :--- | :--- | :--- | :--- |
| **TC01** | `test_dodaj_zadanie` | Dodanie zadania o treści „Poćwiczyć w fl studio” do instancji `TodoApp`. | Lista zawiera 1 element, a dodany tekst zgadza się z oczekiwanym. |
| **TC02** | `test_usun_zadanie` | Dodanie zadania „Iść na spacer”, a następnie jego usunięcie metodą `usun_zadanie`. | Lista zadań jest pusta (długość listy wynosi 0). |