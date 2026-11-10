def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

def farewell(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}! See you next comit."

if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
