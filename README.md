# Password Security Checker  
## Descriere
Acest script Python verifică dacă parolele dintr-un fișier text au fost compromise folosind API-ul "Have I Been Pwned".  
Parolele sunt convertite în hash SHA-1, iar primele 5 caractere ale hash-ului sunt utilizate pentru a interoga baza de date a API-ului.

## Cum funcționează?

- Scriptul citește parolele din fișierul `pass.txt`.
- Fiecare parolă este convertită în hash SHA-1.
- Primele 5 caractere ale hash-ului sunt folosite pentru a interoga API-ul [Have I Been Pwned](https://haveibeenpwned.com/).
- API-ul returnează o listă de hash-uri parțiale potrivite.
- Scriptul verifică dacă sufixul hash-ului original se află în lista returnată.
- Dacă hash-ul este găsit, scriptul afișează de câte ori a fost compromisă parola respectivă.
- Dacă nu este găsit, parola este considerată sigură.  

## Dependențe
- Python 3
- Biblioteca requests se poate instala folosind
```sh
pip install requests
```
## Utilizare
- Creați un fișier pass.txt și adăugați parolele pe care doriți să le verificați (câte una pe fiecare linie).
- Rulați scriptul folosind comanda:
```sh
python script.py
```
- Scriptul va afișa dacă parolele au fost compromise și de câte ori.

## Notă
- Acest script folosește metoda ["k-Anonymity"](https://en.wikipedia.org/wiki/K-anonymity), ceea ce înseamnă că parola nu este transmisă în mod direct către API, asigurând astfel un grad ridicat de confidențialitate.
