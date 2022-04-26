from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.csv_reader import CsvReader
from inventory_report.inventory.json_reader import JsonReader
from inventory_report.inventory.xml_reader import XmlReader


class Inventory:

    @classmethod
    def import_data(cls, path, type):
        types = {
            'simples': SimpleReport,
            'completo': CompleteReport
        }
        readers = {
            'csv': CsvReader,
            'json': JsonReader,
            'xml': XmlReader
        }
        file_extension = path.split(".")[-1]
        relatory = readers[file_extension].read(path)
        return types[type].generate(relatory)
