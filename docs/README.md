# testowanie_aplikacji
# Projekt: Prosta Aplikacja ToDo (Python + PyTest)

## Opis projektu
Projekt przedstawia prostą aplikację listy zadań stworzoną w języku Python. Umożliwia ona dodawanie nowych zadań oraz ich usuwanie po nazwie. Całość została objęta testami jednostkowymi przy użyciu biblioteki PyTest oraz zautomatyzowana za pomocą GitHub Actions.

## Struktura projektu
- `src/app.py` – główny kod aplikacji z klasą `TodoApp`.
- `src/test_app.py` – testy jednostkowe sprawdzające poprawność działania aplikacji.
- `.github/workflows/tests.yml` – konfiguracja automatycznego uruchamiania testów.

## Instrukcja uruchomienia
1. Sklonuj repozytorium na swój komputer.
2. Zainstaluj bibliotekę testową PyTest (jeśli jej nie masz):
   ```bash
   pip install pytest