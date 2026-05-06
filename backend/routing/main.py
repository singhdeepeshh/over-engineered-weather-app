from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/weather/{city}")
async def weather(city: str):
    # Placeholder for weather data retrieval logic
    return {"city": city, "temperature": "25°C", "condition": "Sunny"}