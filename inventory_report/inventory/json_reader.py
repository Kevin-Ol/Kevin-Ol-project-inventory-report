import json


class JsonReader:
    @classmethod
    def read(cls, path):
        with open(path) as file:
            relatory = json.load(file)
        return relatory
