from app.database import SessionLocal, engine
from app.models import Base, Item

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

sample_items = [
  {"name": "Milk", "aisle": "Dairy", "x": 31, "y": 9, "stock": 10},
  {"name": "Apples", "aisle": "Produce", "x": 45, "y": 20, "stock": 40},
  {"name": "Shampoo", "aisle": "Health + Beauty", "x": 20, "y": 12, "stock": 15},
  {"name": "Bread", "aisle": "Grab + Go", "x": 11, "y": 9, "stock": 35},
  {"name": "Ice Cream", "aisle": "Frozen", "x": 20, "y": 9, "stock": 18},
  {"name": "Wine", "aisle": "Wine", "x": 15, "y": 11, "stock": 30},
  {"name": "Toilet Paper", "aisle": "Bulk", "x": 40, "y": 5, "stock": 50},
  {"name": "Soda", "aisle": "Cooler", "x": 31, "y": 5, "stock": 20},
  {"name": "Snacks", "aisle": "Grocery", "x": 30, "y": 11, "stock": 45},
  {"name": "Eggs", "aisle": "Dairy", "x": 36, "y": 4, "stock": 28}
]

db = SessionLocal()
for item in sample_items:
    db_item = Item(**item)
    db.add(db_item)

db.commit()
db.close()

print("Seeded dummy data into store.db")