#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(text)
        return True  # Indicate success
    except Exception as e:
        print(f"Error writing to file '{filename}': {str(e)}")
        return False  # Indicate failure

