from django.core.management.base import BaseCommand, CommandError
from district_civil.models import DistrictCivil

import glob
import pandas as pd


class Command(BaseCommand):
    help = 'Import all "district-civil" data from Schoenfeld CSVs to populate database.'

    def add_arguments(self, parser):

        parser.add_argument('--delete',
                            type=str,
                            help='Possible values are: y')

    def handle(self, *args, **options):

        if options['delete']:
            if options['delete'] == 'y':
                DistrictCivil.objects.all().delete()
                print("Deleted all DistrictCivil objects.")
                exit()
            else:
                print("Invalid option.")
                exit()

        cases_list = glob.glob('schoenfeld-public-data/district-civil/*')
        cases_list.sort()
        for c in cases_list:
            print(c)
            df = pd.read_csv(c, low_memory=False)
            df.fillna('', inplace=True)
            cases = []
            for index, row in df.iterrows():
                case = DistrictCivil(
                    fips=row['fips'],
                    filed_date=row['FiledDate'],
                    case_type=row['CaseType'],
                    debt_type=row['DebtType'],
                    judgment=row['Judgment'],
                    costs=row['Costs'],
                    attorney_fees=row['AttorneyFees'],
                    principal_amount=row['PrincipalAmount'],
                    other_amount=row['OtherAmount'],
                    interest_award=row['InterestAward'],
                    possession=row['Possession'],
                    writ_issued_date=row['WritIssuedDate'],
                    homestead_exemption_waived=row['HomesteadExemptionWaived'],
                    is_judgment_satisfied=row['IsJudgmentSatisfied'],
                    date_satisfaction_filed=row['DateSatisfactionFiled'],
                    other_awarded=row['OtherAwarded'],
                    further_case_information=row['FurtherCaseInformation'],
                    garnishee=row['Garnishee'],
                    address=row['Address'],
                    garnishee_answer=row['GarnisheeAnswer'],
                    answer_date=row['AnswerDate'],
                    number_of_checks_received=row['NumberofChecksReceived'],
                    appeal_date=row['AppealDate'],
                    appealed_by=row['AppealedBy'],
                    writ_of_eviction_issued_date=row['WritofEvictionIssuedDate'],
                    writ_of_fieri_facias_issued_date=row['WritofFieriFaciasIssuedDate'],
                    plaintiff_1_DBATA=row['Plaintiff1DBATA'],
                    plaintiff_1_address=row['Plaintiff1Address'],
                    plaintiff_1_attorney=row['Plaintiff1Attorney'],
                    plaintiff_2_DBATA=row['Plaintiff2DBATA'],
                    plaintiff_2_address=row['Plaintiff2Address'],
                    plaintiff_2_attorney=row['Plaintiff2Attorney'],
                    plaintiff_3_DBATA=row['Plaintiff3DBATA'],
                    plaintiff_3_address=row['Plaintiff3Address'],
                    plaintiff_3_attorney=row['Plaintiff3Attorney'],
                    defendant_1_DBATA=row['Defendant1DBATA'],
                    defendant_1_address=row['Defendant1Address'],
                    defendant_1_attorney=row['Defendant1Attorney'],
                    defendant_2_DBATA=row['Defendant2DBATA'],
                    defendant_2_address=row['Defendant2Address'],
                    defendant_2_attorney=row['Defendant2Attorney'],
                    defendant_3_DBATA=row['Defendant3DBATA'],
                    defendant_3_address=row['Defendant3Address'],
                    defendant_3_attorney=row['Defendant3Attorney'],
                )
                cases.append(case)
                if len(cases) > 50000:
                    DistrictCivil.objects.bulk_create(cases)
                    cases = []
            if cases:
                DistrictCivil.objects.bulk_create(cases)
