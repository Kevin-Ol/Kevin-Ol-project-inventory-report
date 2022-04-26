import xmltodict


class XmlReader:
    @classmethod
    def read(cls, path):
        with open(path) as file:
            xml_content = file.read()
            xml_dict = xmltodict.parse(xml_content)
            relatory = xml_dict['dataset']['record']
        return relatory
