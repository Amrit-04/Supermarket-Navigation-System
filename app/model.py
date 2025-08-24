import pickle
import os

# Load the model at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), "recommend_model.pkl")
with open(MODEL_PATH, "rb") as f:
    recommend_model = pickle.load(f)