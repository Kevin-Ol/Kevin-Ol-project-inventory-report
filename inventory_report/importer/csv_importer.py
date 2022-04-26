import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split(".")[-1]

        if (file_extension != 'csv'):
            raise ValueError("Arquivo inválido")

        relatory = []
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                relatory.append(row)
        return relatory
