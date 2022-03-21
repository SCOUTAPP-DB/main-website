# Generated by Django 3.2.5 on 2022-01-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CircuitCriminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hearing_date', models.CharField(blank=True, max_length=10, null=True)),
                ('hearing_result', models.CharField(blank=True, max_length=108, null=True)),
                ('hearing_jury', models.CharField(blank=True, max_length=3, null=True)),
                ('hearing_plea', models.CharField(blank=True, max_length=17, null=True)),
                ('hearing_type', models.CharField(blank=True, max_length=41, null=True)),
                ('hearing_room', models.CharField(blank=True, max_length=4, null=True)),
                ('fips', models.CharField(blank=True, max_length=3, null=True)),
                ('filed', models.CharField(blank=True, max_length=10, null=True)),
                ('commencedby', models.CharField(blank=True, max_length=46, null=True)),
                ('locality', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=6, null=True)),
                ('race', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('charge', models.CharField(blank=True, max_length=48, null=True)),
                ('code_section', models.CharField(blank=True, max_length=20, null=True)),
                ('charge_type', models.CharField(blank=True, max_length=39, null=True)),
                ('offense_class', models.CharField(blank=True, max_length=3, null=True)),
                ('offense_date', models.CharField(blank=True, max_length=10, null=True)),
                ('arrest_date', models.CharField(blank=True, max_length=10, null=True)),
                ('disposition_code', models.CharField(blank=True, max_length=32, null=True)),
                ('disposition_date', models.CharField(blank=True, max_length=10, null=True)),
                ('concluded_by', models.CharField(blank=True, max_length=26, null=True)),
                ('amended_charge', models.CharField(blank=True, max_length=48, null=True)),
                ('amended_code_section', models.CharField(blank=True, max_length=19, null=True)),
                ('amended_charge_type', models.CharField(blank=True, max_length=39, null=True)),
                ('jail_penitentiary', models.CharField(blank=True, max_length=12, null=True)),
                ('concurrent_consecutive', models.CharField(blank=True, max_length=11, null=True)),
                ('life_death', models.CharField(blank=True, max_length=13, null=True)),
                ('sentence_time', models.CharField(blank=True, max_length=7, null=True)),
                ('sentence_suspended', models.CharField(blank=True, max_length=7, null=True)),
                ('operator_license_suspension_time', models.CharField(blank=True, max_length=7, null=True)),
                ('fine_amount', models.CharField(blank=True, max_length=9, null=True)),
                ('costs', models.CharField(blank=True, max_length=10, null=True)),
                ('fines_cost_paid', models.CharField(blank=True, max_length=3, null=True)),
                ('program_type', models.CharField(blank=True, max_length=41, null=True)),
                ('probation_type', models.CharField(blank=True, max_length=22, null=True)),
                ('probation_time', models.CharField(blank=True, max_length=7, null=True)),
                ('probation_starts', models.CharField(blank=True, max_length=10, null=True)),
                ('court_dmv_surrender', models.CharField(blank=True, max_length=65, null=True)),
                ('driver_improvement_clinic', models.CharField(blank=True, max_length=3, null=True)),
                ('driving_restrictions', models.CharField(blank=True, max_length=3, null=True)),
                ('restriction_effective_date', models.CharField(blank=True, max_length=10, null=True)),
                ('restriction_end_date', models.CharField(blank=True, max_length=10, null=True)),
                ('va_alcohol_safety_action', models.CharField(blank=True, max_length=3, null=True)),
                ('restitution_paid', models.CharField(blank=True, max_length=3, null=True)),
                ('restitution_amount', models.CharField(blank=True, max_length=10, null=True)),
                ('military', models.CharField(blank=True, max_length=14, null=True)),
                ('traffic_fatality', models.CharField(blank=True, max_length=3, null=True)),
                ('appealed_date', models.CharField(blank=True, max_length=10, null=True)),
                ('person_id', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
