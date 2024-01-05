import getpass
import subprocess
from rich.console import Console
from rich.text import Text
import time
import random

def print_welcome_banner():
    console = Console()

    # ASCII art
    ascii_art = r'''
 ____ ___  _              
/  _ \\  \//              
| | // \  /               
| |_\\ / /                
\____//_/                 
'''
    console.print(ascii_art)

    time.sleep(0.5)  # Ajoutez un délai pour l'effet d'animation

    console.clear()

    letters = ["T", "R", "H", "A", "C", "K", "N", "O", "N"]

    for letter in letters:
        glitched_letter = add_glitch(letter)
        console.print(f"[#ff0000]{glitched_letter}[/#ff0000]", end='')
        time.sleep(0.5)  # Délai entre chaque lettre

    console.clear()

    # ASCII art restant
    ascii_art1 = f'''
\033[1;95m _____ \033[0m
\033[1;95m/__ __\\ \033[0m
\033[1;95m  / \\   \033[0m
\033[1;95m  | |   \033[0m
\033[1;95m  \\_/   \033[0m

\033[1;93m ____ \033[0m
\033[1;93m/  __\\ \033[0m
\033[1;93m|  \\/| \033[0m
\033[1;93m|    /  \033[0m
\033[1;93m\\_/\\_\\ \033[0m

\033[1;92m _  __ \033[0m
\033[1;92m/ |/ / \033[0m
\033[1;92m|   /  \033[0m
\033[1;92m|   \\  \033[0m
\033[1;92m\\_|\\_\\ \033[0m

\033[1;96m _     \033[0m
\033[1;96m/ \\  /|\033[0m
\033[1;96m| |\\ ||\033[0m
\033[1;96m| | \\||\033[0m
\033[1;96m\\_/  \\|\033[0m
'''

    console.print(f"[#ff0000]{ascii_art1}[/#ff0000]")

    time.sleep(0.5)  # Ajoutez un délai pour l'effet d'animation

    console.clear()

    banner_text = Text.from_markup(
        f"[#ff0000]{ascii_art1}[/#ff0000]\n"
        "[#ae00ff]this is a Tool modded by[/#ae00ff][#00ffe1][bold] TRHACKNON![/#00ffe1][/bold]"
    )

    console.print(banner_text)

def add_glitch(letter):
    glitch_chance = 0.2  # Probabilité d'ajouter un glitch
    glitch_intensity = 3  # Intensité du glitch

    if random.random() < glitch_chance:
        glitched_letter = ""
        for char in letter:
            glitched_letter += char * glitch_intensity
        return glitched_letter
    else:
        return letter

def authenticate_user():
    expected_password = "trkn"
    entered_password = getpass.getpass("Enter password: ")

    return entered_password == expected_password

def execute_main_script():
    try:
        subprocess.run(["python", "lara.py"])
    except Exception as e:
        console = Console()
        console.print(f"[#ff0000]Error executing main script: {e}[/#ff0000]")

if __name__ == '__main__':
    print_welcome_banner()

    if authenticate_user():
        console = Console()
        console.print("[#00ff00]Authentication successful![/#00ff00]")
        execute_main_script()
    else:
        console = Console()
        console.print("[#ff0000]Authentication failed.[/#ff0000][#ff5900] contact TRHACKNON for the password Exiting...[/#ff5900]")