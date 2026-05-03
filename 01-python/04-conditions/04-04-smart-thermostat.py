# Build Smart Thermostat alert system
# If the 'device_status' is 'active'
    # And 'temperature' > 35 -> Warn: "High temperature alert"
    # Else Normal Temp
# If device is off -> "Device is offline"

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35 :
        print(f"Temparature is high")
    else:
        print("Normal Temperature")
else:
    print("Device is offline")