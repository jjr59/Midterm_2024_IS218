# main.py
from app import app    

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = app().start()  # Instantiate an instance of App