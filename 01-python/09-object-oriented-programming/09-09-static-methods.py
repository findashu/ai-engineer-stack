class Problems:

    # Have to use decorator @staticmethod to declare
    @staticmethod
    def clearText(text):
        return [item.strip() for item in text.split(",")]
    
raw = "Test , Exaple, Hello World ! , there "

# static methods can be directly called without initialisation (Not dependent on Object)
result = Problems.clearText(raw)
print(result)