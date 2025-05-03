from database import setup_database
from auth import Auth
from main import main
import builtins

class InputSimulator:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def __call__(self, _=None):
        if self.index < len(self.inputs):
            value = self.inputs[self.index]
            print(f"> {value}")
            self.index += 1
            return value
        return ""

def setup_environment():
    setup_database()

def run_test_case():
    simulated_inputs = [
        "2",                # Login
        "Orik",             # Username
        "wawawawawawa",     # Password
        "2",                # Login
        "Kazu",             # Username
        "wrongpass",        # Password
        "3"                 # Exit
    ]
    original_input = builtins.input
    builtins.input = InputSimulator(simulated_inputs)
    try:
        main()
    finally:
        builtins.input = original_input

if __name__ == "__main__":
    setup_environment()
    run_test_case()