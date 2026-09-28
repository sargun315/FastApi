from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name: str=None):
    return {"name": name}

@app.get("/product")
def get_users(limit: int=10):
    return {"limit": limit}

@app.get("/multip")
def get_users(name: str=None, price: int=None):
    return {"name": name, "price": price}