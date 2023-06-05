# import pandas as pd
from Printers import Printer
# from datetime import datetime, timedelta


class Company3DWiser:

    list_of_printers = []

    def __init__(self):
        pass

    def import_printers_from_excel(self, excel_file):
        data = pd.read_excel(excel_file)

        for index, row in data.iterrows():
            printer_id = str(row["Printer ID"])
            manufacturer = str(row["Manufacturer"])
            model = str(row["Model"])
            technology = str(row["Technology"])
            footprint = str(row["Footprint"])
            voltage = str(row["Voltage"])
            new_printer = Printer(printer_id, manufacturer, model, technology, footprint, voltage)
            self.list_of_printers.append(new_printer)

    def new_printer(self):
        print("Zde zadejte informace k nové tiskárně")
        printer_id = str(len(self.list_of_printers) + 1)
        manufacturer = input("Výrobce: ").lower()
        model = input("Model: ").lower()
        technology = input("Technologie tisku (SLA/FDM/CFF/FDM-HT/WP-LMD): ").upper()
        footprint = input("Velikost tiskárny (industrial/desktop): ").lower()
        voltage = input("Napájení (230V/400V 16 A):")

        printer = Printer(printer_id, manufacturer, model, technology, footprint, voltage)
        self.list_of_printers.append(printer)
        print("Zkontrolujte přidání tiskárny v systému")

    def show_available_printers(self): # jak synchronizovat s kalendarem
        if self.list_of_printers:
            print("Dostupné tiskárny: ")
            for printer in self.list_of_printers:
                print(f"ID: {printer.printer_id}, Výrobce: {printer.manufacture}, Model: {printer.model}")
        else:
            print("Žádné tiskárny nejsou v systému k dispozici.")


company3DWiser = Company3DWiser()
# company3DWiser.import_printers_from_excel("printers.xlsx")
for i in range(29):
    company3DWiser.new_printer()
company3DWiser.show_available_printers()




