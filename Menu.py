from _3DWiser import Company3DWiser


class ReservationSystem:
    def __init__(self):
        self.company = Company3DWiser()

    def display_menu(self):
        print("Rezervační systém - Hlavní menu")
        print("1 - Zobrazit dostupné tiskárny")  # def show_availables_printers
        print("2 - Přidat novou tiskárnu")  # def new_printer
        print("3 - Odebrat tiskárnu")
        print("4 - Rezervovat tiskárnu")  # def book_printer
        print("5 - Zrušit rezervaci")  # def cancel_reservation
        print("6 - Ukončit program")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Zadejte číslo volby: ")

            if choice == "1":
                self.company.show_available_printers()
            elif choice == "2":
                self.company.new_printer()
            elif choice == "3":
                self.company.remove_printer()
            elif choice == "4":
                printer_id = input("Zadejte ID tiskárny: ")
                date = input("Zadejte datum rezervace (DD.MM.RRRR): ")
                purpose = input("Zadejte účel rezervace: ")
                description = input("Zadejte popis rezervace (volitelné): ")
                self.company.book_printer(printer_id, date, purpose, description)
            elif choice == "5":
                printer_id = input("Zadejte ID tiskárny: ")
                date = input("Zadejte datum rezervace (DD.MM.RRRR): ")
                self.company.cancel_printer_reservation(printer_id, date)
            elif choice == "6":
                print("Konec programu")
                break
            else:
                print("Neplatná volba. Zvolte prosím znovu")


reservation_system = ReservationSystem()
reservation_system.run()
