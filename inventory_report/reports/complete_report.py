from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)

        companies = [product["nome_da_empresa"] for product in products]

        products_by_company = {
            company: companies.count(company) for company in companies
        }

        company_and_product = "\n".join(
            [f"- {key}: {value}" for key, value in products_by_company.items()]
        )

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{company_and_product}\n"
        )
