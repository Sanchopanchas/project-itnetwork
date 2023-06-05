
class Reservation:

    def __init__(self, date, purpose, description):
        self.date = date
        self.purpose = purpose
        self.description = description

    @staticmethod
    def is_printer_available(printer, date):
        for reservation in printer.reservations:
            if reservation.date == date:
                return False
        return True

    @staticmethod
    def is_printer_reserved(printer, date):
        for reservation in printer.reservations:
            if reservation.date == date:
                return True
        return False



