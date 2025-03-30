from datetime import datetime

def generate_event():
    # Vstupní údaje od uživatele
    name = input("Zadej název události: ")
    place = input("Zadej místo události: ")
    link = input("Zadej odkaz (link) na místo: ")
    date_str = input("Zadej datum a čas události (formát: YYYY-MM-DD HH:MM): ")

    # Konverze na datetime objekt
    event_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    # Generování dlouhého data pro Discord timestamp
    timestamp = f"<t:{int(event_datetime.timestamp())}:F>"

    # Výstup ve formátu pro Discord
    event_text = f"""
# {name}
## Kdy
{timestamp}
## Kde
- [{place}]({link})
## Podmínky
Doplním potom v Discordu.
"""
    print(event_text)

# Spustí funkci
generate_event()
