from django.core.management.base import BaseCommand, CommandError
from circuit_criminal.models import CircuitCriminal

import glob
import pandas as pd


class Command(BaseCommand):
    help = 'Import all "circuit-criminal" data from Schoenfeld CSVs to populate database.'

    def add_arguments(self, parser):

        parser.add_argument('--delete',
                            type=str,
                            help='Possible values are: y')

    def handle(self, *args, **options):

        if options['delete']:
            if options['delete'] == 'y':
                CircuitCriminal.objects.all().delete()
                print("Deleted all CircuitCriminal objects.")
                exit()
            else:
                print("Invalid option.")
                exit()

        cases_list = glob.glob('schoenfeld-public-data/circuit-criminal/*')
        cases_list.sort()
        for c in cases_list:
            print(c)
            df = pd.read_csv(c, low_memory=False)
            df.fillna('', inplace=True)
            cases = []
            for index, row in df.iterrows():
                case = CircuitCriminal(
                    hearing_date=row['HearingDate'],
                    hearing_result=row['HearingResult'],
                    hearing_jury=row['HearingJury'],
                    hearing_plea=row['HearingPlea'],
                    hearing_type=row['HearingType'],
                    hearing_room=row['HearingRoom'],
                    fips=row['fips'],
                    filed=row['Filed'],
                    commenced_by=row['Commencedby'],
                    locality=row['Locality'],
                    sex=row['Sex'],
                    race=row['Race'],
                    address=row['Address'],
                    charge=row['Charge'],
                    code_section=row['CodeSection'],
                    charge_type=row['ChargeType'],
                    offense_class = row['Class'],
                    offense_date = row['OffenseDate'],
                    arrest_date = row['ArrestDate'],
                    disposition_code = row['DispositionCode'],
                    disposition_date = row['DispositionDate'],
                    concluded_by = row['ConcludedBy'],
                    amended_charge = row['AmendedCharge'],
                    amended_code_section = row['AmendedCodeSection'],
                    amended_charge_type = row['AmendedChargeType'],
                    jail_penitentiary = row['JailPenitentiary'],
                    concurrent_consecutive = row['ConcurrentConsecutive'],
                    life_death = row['LifeDeath'],
                    sentence_time = row['SentenceTime'],
                    sentence_suspended = row['SentenceSuspended'],
                    operator_license_suspension_time = row['OperatorLicenseSuspensionTime'],
                    fine_amount = row['FineAmount'],
                    costs = row['Costs'],
                    fines_cost_paid = row['FinesCostPaid'],
                    program_type = row['ProgramType'],
                    probation_type = row['ProbationType'],
                    probation_time = row['ProbationTime'],
                    probation_starts = row['ProbationStarts'],
                    court_dmv_surrender = row['CourtDMVSurrender'],
                    driver_improvement_clinic = row['DriverImprovementClinic'],
                    driving_restrictions = row['DrivingRestrictions'],
                    restriction_effective_date = row['RestrictionEffectiveDate'],
                    restriction_end_date = row['RestrictionEndDate'],
                    va_alcohol_safety_action = row['VAAlcoholSafetyAction'],
                    restitution_paid = row['RestitutionPaid'],
                    restitution_amount = row['RestitutionAmount'],
                    military = row['Military'],
                    traffic_fatality = row['TrafficFatality'],
                    appealed_date = row['AppealedDate'],
                    person_id = row['person_id'],
                )
                cases.append(case)
                if len(cases) > 50000:
                    CircuitCriminal.objects.bulk_create(cases)
                    cases = []
            if cases:
                CircuitCriminal.objects.bulk_create(cases)
