def serve_coffee(flavour):
    try:
        print(f"Preparing {flavour} coffee...")
        if flavour == "unknown":
            raise ValueError("We don't have that flavour available.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Here is your {flavour} coffee!")
    finally: # Always runs
        print("Next customer please")

serve_coffee("latte")
serve_coffee("unknown")