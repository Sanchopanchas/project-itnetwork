from Printers import Printer
from Reservation import Reservation
import sqlite3


class Company3DWiser:
    list_of_printers = []

    def __init__(self):
        pass

    def new_printer(self): # přidání nové tiskárny do seznamu tiskáren
        print("Zde zadejte informace k nové tiskárně")
        printer_id = str(len(self.list_of_printers) + 1)
        manufacturer = input("Výrobce: ").lower()
        model = input("Model: ").lower()
        technology = input("Technologie tisku (SLA/FDM/CFF/FDM-HT/WP-LMD): ").upper()
        footprint = input("Velikost tiskárny (industrial/desktop): ").lower()
        voltage = input("Napájení (230V/400V 16 A): ")

        printer = Printer(printer_id, manufacturer, model, technology, footprint, voltage)
        self.list_of_printers.append(printer)
        print("Tiskárna byla úspěšně přidána do systému")

    def remove_printer(self): # odebrání vyřazené tiskárny ze seznamu
        if self.list_of_printers:
            printer_id = input("Zadejte ID tiskárny k odebrání: ")
            for printer in self.list_of_printers:
                if printer.printer_id == printer_id:  # kontrola id_tiskárny
                    self.list_of_printers.remove(printer)
                    print("Tiskárna byla úspěšně odebrána ze systému")
                    break
            else:
                print("Tiskárna s daným ID nebyla nalezena.")
        else:
            print("Žádné tiskárny nejsou v systému k dispozici.")

    def show_available_printers(self):  # kontrola dostupnosti tiskáren
        if self.list_of_printers:
            print("Dostupné tiskárny: ")
            for printer in self.list_of_printers:
                print(f"ID: {printer.printer_id}, Výrobce: {printer.manufacture}, Model: {printer.model}")
        else:
            print("Žádné tiskárny nejsou v systému k dispozici.")

    def book_printer(self, printer_id, date, purpose, description=""):  # rezervování tiskárny
        for printer in self.list_of_printers:
            if printer.printer_id == printer_id:  # kontrola id_tiskárny
                if Reservation.is_printer_available(printer, date):
                    # tiskárna je k dispozici, přidáme rezervaci
                    reservation = Reservation(date, purpose, description)
                    printer.reservations.append(reservation)  # přidá rezervaci do tiskárny
                    print("Tiskárna byla úspěšně rezervována")
                else:
                    print("Tiskárna není dostupná pro zadané datum")
                break
        else:
            print("Tiskárna s daným ID nebyla nalezena.")

    def cancel_printer_reservation(self, printer_id, date):
        for printer in self.list_of_printers:
            if printer.printer_id == printer_id:
                if Reservation.is_printer_reserved(printer, date):
                    # tiskárna je rezervována na zadané datum, zrušíme rezervaci
                    for reservation in printer.reservations:
                        if reservation.date == date:
                            printer.reservations.remove(reservation)
                            print("Rezervace byla úspěšně zrušena")
                            break
                    else:
                        print("Tiskárna není rezervovaná na zadané datum.")
                else:
                    print("Tiskárna není rezervovaná na zadané datum")
                break
        else:
            print("Tiskárna s daným ID nebyla nalezena")


    def load_printers_from_database(self):
        conn = sqlite3.connect('printers_database.db')  # Připojení k databázi
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM printers')  # Vykonání SQL dotazu na získání všech záznamů z tabulky "printers"
        rows = cursor.fetchall()  # Načtení všech řádků z výsledku dotazu

        for row in rows:
            # Načtení hodnot z řádku a vytvoření instance tiskárny
            printer_id = str(row[0])
            manufacturer = row[1].lower()
            model = row[2].lower()
            technology = row[3].upper()
            footprint = row[4].lower()
            voltage = row[5]

            printer = Printer(printer_id, manufacturer, model, technology, footprint, voltage)
            self.list_of_printers.append(printer)

        conn.close()  # Uzavření spojení s databází

company = Company3DWiser()
company.load_printers_from_database()

# Tisk seznamu načtených tiskáren
for printer in company.list_of_printers:
    print(f"ID: {printer.printer_id}, Výrobce: {printer.manufacture}, Model: {printer.model}")



