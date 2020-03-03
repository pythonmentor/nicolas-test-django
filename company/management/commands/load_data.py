from django.core.management.base import BaseCommand
from django.conf import settings
from company.models import Company, Result
import json


FILE_PATH = settings.BASE_DIR + "/mock_data.json"


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(FILE_PATH) as f:
            data = json.load(f)

        for company in data:
            new_company = Company(
                name=company['name'],
                sector=company['sector'],
                siren=company['siren'],
            )
            new_company.save()

            for result in company["results"]:
                new_result = Result(
                    ca=result['ca'],
                    margin=result['margin'],
                    ebitda=result['ebitda'],
                    loss=result['loss'],
                    year=result['year'],
                    company=new_company,
                )
                new_result.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
