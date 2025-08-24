from fastapi import FastAPI, WebSocket, Depends, Query
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app import models, crud, database
from app.pathfinding import a_star
from typing import Optional
import pickle
import os

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Supermarket system is running"}

@app.get("/search")
def search_item(query: str, db: Session = Depends(get_db)):
    item = crud.get_item_by_name(db, query)
    if item:
        return {
            "name": item.name,
            "x": item.x,
            "y": item.y,
            "stock": item.stock,
            "aisle": item.aisle
        }
    return {"error": "Item not found"}

@app.post("/update_stock")
def update_stock(item_id: int, stock: int, db: Session = Depends(get_db)):
    item = crud.update_stock(db, item_id, stock)
    return {"success": True, "new_stock": item.stock} if item else {"error": "Item not found"}

from app.pathfinding import a_star, load_grid_from_csv

@app.get("/navigate")
def navigate(
    to_x: int, to_y: int,
    from_x: Optional[int] = 28, from_y: Optional[int] = 28
):
    grid = load_grid_from_csv()
    path = a_star((from_x, from_y), (to_x, to_y), grid)
    return {"path": path}

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Stock updated: {data}")


# Load recommendation model at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), "walmart_recommender_sentence_transformers.pkl")
with open(MODEL_PATH, "rb") as f:
    recommend_model = pickle.load(f)

@app.get("/recommend")
def recommend(query: str = Query(...)):
    recommendations = recommend_model(query)
    return {"recommendations": recommendations[:5]}