import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}

    file_path = sys.argv[1]
    inventory_report_type = sys.argv[2]
    file_extension = file_path.split(".")[-1]

    inventory = InventoryRefactor(importers[file_extension]).import_data(
        file_path, inventory_report_type
    )

    return print(f"{inventory}", end="")
