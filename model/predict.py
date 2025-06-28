import pickle
import pandas as pd


with open('model/model.pkl', 'rb') as f: ## rb is read binary because this is binary file
    model= pickle.load(f)
MODEL_VERSION = "1.0.0"  # Example version, can be updated as needed
class_labels =model.classes_.tolist()

def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))

    return{
        'predicted_category': predicted_class,
        'confidence': round(confidence, 4),
        'class_probabilities': class_probs
    }

    output = model.predict(input_df)[0]
    return output