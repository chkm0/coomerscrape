import requests
from urllib.parse import urlparse
import keyboard
import time

# ASCII-Art am Anfang des Skripts
ascii_art = """███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗                                                                   
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝                                                                   
███████╗██║██╔████╔██║██████╔╝██║     █████╗                                                                     
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝                                                                     
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗                                                                   
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝                                                                   
                                                                                                                 
 ██████╗ ██████╗  ██████╗ ███╗   ███╗███████╗██████╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║   ██║██╔████╔██║█████╗  ██████╔╝    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                 
██████╗ ██╗   ██╗     ██████╗██╗  ██╗██╗  ██╗███╗   ███╗ ██████╗                                                 
██╔══██╗╚██╗ ██╔╝    ██╔════╝██║  ██║██║ ██╔╝████╗ ████║██╔═══██╗                                                
██████╔╝ ╚████╔╝     ██║     ███████║█████╔╝ ██╔████╔██║██║   ██║                                                
██╔══██╗  ╚██╔╝      ██║     ██╔══██║██╔═██╗ ██║╚██╔╝██║██║   ██║                                                
██████╔╝   ██║       ╚██████╗██║  ██║██║  ██╗██║ ╚═╝ ██║╚██████╔╝                                                
╚═════╝    ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝                                                 
                                                                                                                 


"""

print(ascii_art)

# Funktion zur Aktualisierung der Statusanzeige
def update_status(status):
    print(status, end='\r')

def get_username_from_url(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        username = path.split('/')[1]
        return username
    except Exception as e:
        return None

def search_on_other_site(username):
    url = f"https://coomer.su/onlyfans/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

if __name__ == "__main__":
    filename = input("enter filename of URL list: ")
    found_profiles = []

    try:
        with open(filename, 'r') as file:
            total_lines = sum(1 for line in open(filename))
            current_line = 0

            for line in file:
                current_line += 1
                if 'onlyfans' in line.lower():
                    user_input = line.strip()

                    if user_input.startswith('http://') or user_input.startswith('https://'):
                        username = get_username_from_url(user_input)
                        if username:
                            result = search_on_other_site(username)
                            if result:
                                # Verarbeite das Ergebnis, um nur die URL anzuzeigen
                                result = result.split(' ')[0]
                                found_profiles.append(result)

                # Aktualisiere die Statusanzeige
                progress = (current_line / total_lines) * 100
                update_status(f"coo0o0o0o0o0oom is loading: {progress:.2f}%")

        if found_profiles:
            print("\nCoomer Hits:")
            for profile in found_profiles:
                print(profile)
        else:
            print("\nNo Coom today")

        with open('URLs.txt', 'w') as output_file:
            for profile in found_profiles:
                output_file.write(profile + '\n')

        print("Press Enter to close...")
        keyboard.read_event()

    except FileNotFoundError:
        print(f"Die Datei {filename} wurde nicht gefunden. Bitte überprüfen Sie den Dateinamen und versuchen Sie es erneut.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
