from django.core.management.base import BaseCommand, CommandError
from circuit_civil.models import CircuitCivil

import glob
import pandas as pd


class Command(BaseCommand):
    help = 'Import all "circuit-civil" data from Schoenfeld CSVs to populate database.'

    def add_arguments(self, parser):

        parser.add_argument('--delete',
                            type=str,
                            help='Possible values are: y')

    def handle(self, *args, **options):

        if options['delete']:
            if options['delete'] == 'y':
                CircuitCivil.objects.all().delete()
                print("Deleted all CircuitCivil objects.")
                exit()
            else:
                print("Invalid option.")
                exit()

        cases_list = glob.glob('schoenfeld-public-data/circuit-civil/*')
        cases_list.sort()
        for c in cases_list:
            print(c)
            df = pd.read_csv(c, low_memory=False)
            df.fillna('', inplace=True)
            cases = []
            for index, row in df.iterrows():
                case = CircuitCivil(
                    fips=row['fips'],
                    filed_date=row['Filed'],
                    filing_type=row['FilingType'],
                    filing_fee_paid=row['FilingFeePaid'],
                    number_of_plaintiffs=row['NumberofPlaintiffs'],
                    number_of_defendants=row['NumberofDefendants'],
                    commenced_by=row['CommencedBy'],
                    bond=row['Bond'],
                    complex_case=row['ComplexCase'],
                    date_ordered_to_mediation=row['DateOrderedToMediation'],
                    judgment=row['Judgment'],
                    final_order_date=row['FinalOrderDate'],
                    appealed_date=row['AppealedDate'],
                    concluded_by=row['ConcludedBy'],
                    plaintiff_1_trading_as=row['Plaintiff1TradingAs'],
                    plaintiff_2_trading_as=row['Plaintiff2TradingAs'],
                    plaintiff_3_trading_as=row['Plaintiff3TradingAs'],
                    plaintiff_1_attorney=row['Plaintiff1Attorney'],
                    plaintiff_2_attorney=row['Plaintiff2Attorney'],
                    plaintiff_3_attorney=row['Plaintiff3Attorney'],
                    defendant_1_trading_as=row['Defendant1TradingAs'],
                    defendant_2_trading_as=row['Defendant2TradingAs'],
                    defendant_3_trading_as=row['Defendant3TradingAs'],
                    defendant_1_attorney=row['Defendant1Attorney'],
                    defendant_2_attorney=row['Defendant2Attorney'],
                    defendant_3_attorney=row['Defendant3Attorney'],
                )
                cases.append(case)
                if len(cases) > 50000:
                    CircuitCivil.objects.bulk_create(cases)
                    cases = []
            if cases:
                CircuitCivil.objects.bulk_create(cases)