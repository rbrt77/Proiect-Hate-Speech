from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Încărcăm modelul antrenat anterior
model = joblib.load('model_hate_speech.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Luăm textul introdus de utilizator
        mesaj = request.form['mesaj']
        
        # Facem predicția (modelul nostru știe să transforme textul singur datorită Pipeline-ului)
        predictie = model.predict([mesaj])[0]
        
        # Interpretăm rezultatul
        if predictie == 1:
            rezultat = "TOXIC / HATE SPEECH ⚠️"
            culoare = "red"
        else:
            rezultat = "Non-Toxic (Safe) ✅"
            culoare = "green"
            
        return render_template('index.html', prediction_text=rezultat, color=culoare, input_text=mesaj)

if __name__ == '__main__':
    app.run(debug=True)