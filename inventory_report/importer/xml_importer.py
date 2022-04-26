import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_extension = path.split(".")[-1]

        if (file_extension != 'xml'):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            xml_content = file.read()
            xml_dict = xmltodict.parse(xml_content)
            relatory = xml_dict['dataset']['record']
        return relatory
