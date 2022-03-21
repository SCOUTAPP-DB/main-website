from django.core.management.base import BaseCommand, CommandError
from district_criminal.models import DistrictCriminal

import glob
import pandas as pd


class Command(BaseCommand):
    help = 'Import all "district-criminal" data from Schoenfeld CSVs to populate database.'

    def add_arguments(self, parser):

        parser.add_argument('--delete',
                            type=str,
                            help='Possible values are: y')

    def handle(self, *args, **options):

        if options['delete']:
            if options['delete'] == 'y':
                DistrictCriminal.objects.all().delete()
                print("Deleted all DistrictCriminal objects.")
                exit()
            else:
                print("Invalid option.")
                exit()

        cases_list = glob.glob('schoenfeld-public-data/district-criminal/*')
        cases_list.sort()
        for c in cases_list:
            print(c)
            df = pd.read_csv(c, low_memory=False)
            df.fillna('', inplace=True)
            cases = []
            for index, row in df.iterrows():
                case = DistrictCriminal(
                    hearing_date=row['HearingDate'],
                    hearing_result=row['HearingResult'],
                    hearing_plea=row['HearingPlea'],
                    hearing_continuance_code=row['HearingContinuanceCode'],
                    hearing_type=row['HearingType'],
                    hearing_courtroom=row['HearingCourtroom'],
                    fips=row['fips'],
                    filed_date=row['FiledDate'],
                    locality=row['Locality'],
                    status=row['Status'],
                    defense_attorney=row['DefenseAttorney'],
                    address=row['Address'],
                    gender=row['Gender'],
                    race=row['Race'],
                    charge=row['Charge'],
                    code_section=row['CodeSection'],
                    case_type=row['CaseType'],
                    offense_class = row['Class'],
                    offense_date = row['OffenseDate'],
                    arrest_date = row['ArrestDate'],
                    complainant = row['Complainant'],
                    amended_charge = row['AmendedCharge'],
                    amended_code = row['AmendedCode'],
                    amended_case_type = row['AmendedCaseType'],
                    final_disposition = row['FinalDisposition'],
                    sentence_time = row['SentenceTime'],
                    sentence_suspended_time = row['SentenceSuspendedTime'],
                    probation_type = row['ProbationType'],
                    probation_time = row['ProbationTime'],
                    probation_starts = row['ProbationStarts'],
                    operator_license_suspension_time = row['OperatorLicenseSuspensionTime'],
                    restriction_effective_date = row['RestrictionEffectiveDate'],
                    restriction_end_date = row['RestrictionEndDate'],
                    operator_license_restriction_codes = row['OperatorLicenseRestrictionCodes'],
                    fine = row['Fine'],
                    costs = row['Costs'],
                    fine_costs_due = row['FineCostsDue'],
                    fine_costs_paid = row['FineCostsPaid'],
                    fine_costs_paid_date = row['FineCostsPaidDate'],
                    vasap = row['VASAP'],
                    fine_costs_past_due = row['FineCostsPastDue'],
                    person_id = row['person_id'],
                )
                cases.append(case)
                if len(cases) > 50000:
                    DistrictCriminal.objects.bulk_create(cases)
                    cases = []
            if cases:
                DistrictCriminal.objects.bulk_create(cases)