from _3DWiser import Company3DWiser


class Reservation:

    def __init__(self, date, purpose, description):
        self.date = date
        self.purpose = purpose
        self.description = description
        self.printer_reservation = []

    @staticmethod
    def is_printer_available(printer, date):
        for reservation in printer.reservations:
            if reservation.date == date:
                return False
        return True

    """def is_printer_available(printer, date):
        for reservation in printer.reservations:
            if reservation.date == date:
                return False
        return True"""

    # description dobrovolné
    def book_printer(self, printer_id, date, purpose, description=""):
        self.date = date
        self.purpose = purpose
        self.description = description
        for printer in self.list_of_printers: # list_of_printers mám definované u třídy Company
            if printer.printer_id == printer_id:  # kontrola evidence tiskárny
                if self.is_printer_available(printer, date):
                    # tiskárna je k dispozici, přidáme rezervaci
                    reservation = Reservation(date, purpose, description)
                    printer.add_reservation(reservation)
                    print("Tiskárna byla úspěšně rezervována")
                else:
                    print("Tiskárna není dostupná pro zadané datum")
                break
            else:
                print("Tiskárna s daným ID nebyla nalezena.")
