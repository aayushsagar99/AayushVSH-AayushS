from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Smart Home IoT Backend")

# Allow your HTML frontend to talk to this backend safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global database variables (stored in memory for simplicity)
latest_sensor_data = {"temperature": 0.0, "humidity": 0.0}
led_status = "OFF"  # Can be "ON" or "OFF"

# Data blueprint for what the ESP32 hardware will send
class SensorReadings(BaseModel):
    temperature: float
    humidity: float

# --- ENDPOINTS FOR THE HARDWARE (ESP32) ---

@app.post("/hardware/data")
async def receive_sensor_data(data: SensorReadings):
    """The physical ESP32 sends temperature/humidity data here."""
    global latest_sensor_data
    latest_sensor_data["temperature"] = data.temperature
    latest_sensor_data["humidity"] = data.humidity
    
    # Immediately reply to the ESP32 telling it whether to turn the LED ON or OFF
    return {"led_command": led_status}

@app.get("/hardware/command")
async def get_led_command():
    """Alternative endpoint for the ESP32 to check the current LED status."""
    return {"led_command": led_status}


# --- ENDPOINTS FOR YOUR HTML/CSS FRONTEND ---

@app.get("/frontend/dashboard")
async def get_dashboard_data():
    """Your HTML dashboard calls this to get the latest room stats and light status."""
    return {
        "sensor_data": latest_sensor_data,
        "led_status": led_status
    }

@app.post("/frontend/toggle-led")
async def toggle_led():
    """Your HTML button calls this to turn the physical desk light ON or OFF."""
    global led_status
    if led_status == "ON":
        led_status = "OFF"
    else:
        led_status = "ON"
    return {"message": "LED status updated successfully", "new_status": led_status}
