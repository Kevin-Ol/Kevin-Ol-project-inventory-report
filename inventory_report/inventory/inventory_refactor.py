from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        types = {
            'simples': SimpleReport,
            'completo': CompleteReport
        }

        relatory = self.importer.import_data(path)

        for product in relatory:
            self.data.append(product)

        return types[type].generate(relatory)

    def __iter__(self):
        return InventoryIterator(self.data)
