import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

print("--- START ANTRENARE ---")

# 1. Încărcăm datele
if not os.path.exists('train.csv'):
    print("EROARE: Nu găsesc fișierul 'train.csv'! Asigură-te că e în același folder.")
    exit()

print("1. Se încarcă datele din train.csv...")
df = pd.read_csv('train.csv')
 
print(f"   - Au fost încărcate {len(df)} rânduri.")

# 2. Pregătim datele
X = df['comment_text']
y = df['toxic']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Creăm modelul
print("2. Se construiește modelul...")
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression())
])

# 4. Antrenăm
print("3. Se antrenează modelul (așteaptă câteva secunde)...")
model.fit(X_train, y_train)

# 5. Scor
score = model.score(X_test, y_test)
print(f"4. GATA! Acuratețea este: {score * 100:.2f}%")

# 6. Salvare
print("5. Se salvează fișierul...")
joblib.dump(model, 'model_hate_speech.pkl')

if os.path.exists('model_hate_speech.pkl'):
    print("✅ SUCCES: Fișierul 'model_hate_speech.pkl' a fost creat!")
    print("   Acum poți rula: python3 aplicatia.py")
else:
    print("❌ EROARE: Fișierul nu a putut fi salvat.")