from datetime import date
from statistics import mode


class SimpleReport:
    @classmethod
    def generate(cls, products):
        min_fabrication = min(
            [product["data_de_fabricacao"] for product in products]
        )

        date_today = date.today().isoformat()

        min_valid = min(
            [
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"] > date_today
            ]
        )

        name = mode([product["nome_da_empresa"] for product in products])

        return (
            f"Data de fabricação mais antiga: {min_fabrication}\n"
            f"Data de validade mais próxima: {min_valid}\n"
            f"Empresa com maior quantidade de produtos estocados: {name}\n"
        )
