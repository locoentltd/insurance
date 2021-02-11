# Generated by Django 2.0 on 2021-02-11 13:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portal.fields.currency
import portal.fields.percentage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('territory', models.CharField(default='A', max_length=5)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DedLimitMultiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplier', models.DecimalField(decimal_places=5, default=1.0, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DedLimitPremium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', portal.fields.currency.CurrencyField(blank=True, decimal_places=2, default=0, max_digits=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deductible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='Insured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('title_other', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField()),
                ('max', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('min', 'max'),
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performs', models.BooleanField(default=False)),
                ('work_percentage', portal.fields.percentage.PercentageField(default=0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)])),
                ('note', models.TextField(blank=True)),
                ('procedure_type', models.CharField(choices=[('laser', 'LASER'), ('bariatric', 'BARIATRIC'), ('telemedicine', 'TELEMEDICINE'), ('correctional_facilities', 'CORRECTIONAL FACILITIES'), ('nursing homes', 'NURSING HOMES')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuickQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, ''), (10, ''), (20, ''), (30, ''), (40, ''), (50, ''), (60, '')], default=0)),
                ('surgery', models.PositiveSmallIntegerField(choices=[(0, 'None'), (50, 'Minor'), (100, 'Major')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('friendly_name', models.CharField(blank=True, max_length=50)),
                ('agency_name', models.CharField(max_length=50)),
                ('agent_name', models.CharField(max_length=30)),
                ('agent_email', models.EmailField(max_length=254)),
                ('insured_name', models.CharField(max_length=30)),
                ('prior_acts_effective_date', models.DateField(blank=True, null=True)),
                ('prior_acts_retroactive_date', models.DateField(blank=True, null=True)),
                ('board_actions_last_10_years', models.PositiveSmallIntegerField(default=0)),
                ('weekly_hours', models.PositiveSmallIntegerField(default=0)),
                ('weekly_patients', models.PositiveSmallIntegerField(default=0)),
                ('weekly_procedures', models.PositiveSmallIntegerField(default=0)),
                ('weekly_deliveries', models.PositiveSmallIntegerField(default=0)),
                ('weekly_reads', models.PositiveSmallIntegerField(default=0)),
                ('entity_coverage', models.BooleanField(default=False)),
                ('entity_note', models.TextField(blank=True)),
                ('professional_coverage', models.BooleanField(default=False)),
                ('professional_note', models.TextField(blank=True)),
                ('cosmetic_elective_percentage', portal.fields.percentage.PercentageField(default=0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)])),
                ('cosmetic_recon_percentage', portal.fields.percentage.PercentageField(default=0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)])),
                ('claims_last_10_years', models.PositiveSmallIntegerField(default=0)),
                ('open_claims', models.PositiveSmallIntegerField(default=0)),
                ('closed_claims', models.PositiveSmallIntegerField(default=0)),
                ('current_carrier', models.CharField(blank=True, max_length=50)),
                ('expiring_premium', models.CharField(blank=True, max_length=10)),
                ('note', models.TextField(blank=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Agent')),
                ('cosmetic_surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('insured', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Insured')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('practice_percentage', portal.fields.percentage.PercentageField(default=0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)])),
                ('speciality_type', models.CharField(choices=[('primary', 'PRIMARY'), ('secondary', 'SECONDARY')], max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('abbr', models.CharField(max_length=2, unique=True)),
                ('counties', models.ManyToManyField(editable=False, to='portal.County')),
                ('limits', models.ManyToManyField(to='portal.Limit')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StateCoverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_percentage', portal.fields.percentage.PercentageField(default=0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)])),
                ('cover', models.CharField(choices=[('primary', 'PRIMARY'), ('secondary', 'SECONDARY')], max_length=30)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portal.Address')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=('portal.address',),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='primary_practice',
            field=models.ManyToManyField(related_name='primary_address', to='portal.Address'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='secondary_practice',
            field=models.ManyToManyField(related_name='secondary_address', to='portal.Address'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State'),
        ),
        migrations.AddField(
            model_name='insured',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Title'),
        ),
        migrations.AddField(
            model_name='dedlimitpremium',
            name='deductible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Deductible'),
        ),
        migrations.AddField(
            model_name='dedlimitpremium',
            name='limit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Limit'),
        ),
        migrations.AddField(
            model_name='dedlimitmultiplier',
            name='deductible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Deductible'),
        ),
        migrations.AddField(
            model_name='dedlimitmultiplier',
            name='limit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Limit'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Agency'),
        ),
        migrations.AddField(
            model_name='agent',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Agency'),
        ),
    ]
