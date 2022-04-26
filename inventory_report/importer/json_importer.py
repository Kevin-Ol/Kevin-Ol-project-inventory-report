import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split(".")[-1]

        if (file_extension != 'json'):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            relatory = json.load(file)
        return relatory
