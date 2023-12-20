import readline

def input_with_correction(prompt):
    try:
        readline.set_startup_hook(lambda: readline.insert_text(""))
        user_input = input(prompt)
        return user_input
    finally:
        readline.set_startup_hook()