from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This part allows your HTML file to talk securely to your Python backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is a basic "endpoint" or route
@app.get("/")
def read_root():
    return {"message": "Hello from the Python backend!"}

# Keep your existing code above, just add this to the bottom:

@app.get("/greet")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}! Your Python backend successfully processed this request!"}


# Add this to the absolute bottom of main.py:

@app.get("/calculate")
def add_numbers(num1: float, num2: float):
    total = num1 + num2
    return {"result": f"{num1} + {num2} = {total}"}