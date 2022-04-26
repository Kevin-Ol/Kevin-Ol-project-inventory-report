import csv


class CsvReader:
    @classmethod
    def read(cls, path):
        relatory = []
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                relatory.append(row)
        return relatory
