from rest_framework import serializers
from .models import civil_case, crim_case

class CrimCaseSerializer(serializers.ModelSerializer):
    """Serializer to map the User instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = crim_case
        fields = ('address','aka1','aka2','amended_case_type','amended_charge','amended_code','arrest_date','case_number','case_type','charge','code_section','complainant','costs','court','crim_class','date_of_birth','defense_attorney','filed_date','final_disposition','fine','fine_costs_due','fine_costs_paid','fine_costs_paid_date','gender','hearing_info','locality','name','offense_date','operator_license_restriction_codes','operator_license_suspension_effective_date','operator_license_suspension_time','probation_starts','probation_time','probation_type','race','sentence_suspended_time','sentence_time','status','vasap')

class CivilCaseSerializer(serializers.ModelSerializer):
    """Serializer to map the User instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = civil_case
        fields = ('address','answer_date','appeal_date','appealed_by','attorney_fees','case_number','case_type','costs','court','date_satisfaction_filed','debt_type','defendant_info','filed_date','further_case_info','garnishee','garnishee_answer','hearing_info','homestead_exemption_waived','interest_award','is_judgement_satisifed','judgment','number_of_checks_received','other_amount','other_awarded','plaintiff_info','possession','principal_amount','writ_issue_date')


