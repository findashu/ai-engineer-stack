from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Access Denied! Admins Only")
            return None # Optional with newer version
        else:
            return func(role)
    return wrapper

@require_admin
def access_inventory(role):
    print("Access Granted")


access_inventory("user")
access_inventory("admin")
        
        

