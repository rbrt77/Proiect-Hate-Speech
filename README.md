# 🧠 Detectarea Hate Speech-ului --- Proiect Machine Learning

Acest proiect reprezintă o aplicație web simplă care utilizează tehnici
de **Inteligență Artificială** pentru a detecta mesaje toxice sau „hate
speech". Modelul este antrenat pe date text și integrat într-o interfață
web realizată cu **Flask**.

------------------------------------------------------------------------

## 👥 Echipa

1.  **\[Tudorache Robert\]** --- Procesare date\
2.  **\[Craciun Alexandru\]** --- Antrenare model\
3.  **\[David Denis\]** --- Evaluare și testare\
4.  **\[Onete Andrei\]** --- Interfață Web

------------------------------------------------------------------------

## 📂 Structura proiectului

  -----------------------------------------------------------------------
  Fișier                        Descriere
  ----------------------------- -----------------------------------------
  `antrenare.py`                Scriptul pentru citirea datelor și
                                antrenarea modelului.

  `aplicatia.py`                Codul aplicației web Flask.

  `model_hate_speech.pkl`       Modelul AI salvat (creierul aplicației).

  `requirements.txt`            Lista de librării necesare proiectului.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 Cum se rulează proiectul

### 1. Crearea și activarea mediului virtual

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalarea librăriilor necesare

``` bash
pip install pandas scikit-learn flask joblib
```

### 3. Antrenarea modelului
``` bash
python antrenare.py
```

### 4. Pornirea aplicației web

``` bash
python aplicatia.py
```

Apoi deschide browserul la: http://127.0.0.1:5000
