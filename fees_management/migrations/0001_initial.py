# Generated by Django 2.0 on 2018-07-18 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onboarding', '0002_auto_20180718_0656'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('class_user_profiling', '0005_auto_20180717_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='DpyFeeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.FloatField()),
                ('cycle', models.IntegerField()),
                ('cycle_slot', models.IntegerField()),
                ('dsc', models.TextField()),
                ('mop', models.IntegerField(default=1)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'dpy_fee_transaction',
                'verbose_name': 'Dpy Payment Receipt',
            },
        ),
        migrations.CreateModel(
            name='DpyFeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=250)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'dpy_fee_type',
                'verbose_name': 'dpy_fee_type',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteClassFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('cycle', models.PositiveSmallIntegerField()),
                ('display_name', models.CharField(max_length=250)),
                ('bifurcations', models.TextField(null=True)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('fee_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees_management.DpyFeeType')),
                ('institute_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='class_user_profiling.DpyInstituteClass')),
            ],
            options={
                'managed': True,
                'db_table': 'dpy_institute_class_fee',
                'verbose_name': 'Institute Class Fee',
            },
        ),
        migrations.CreateModel(
            name='DpyPaymentReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_or_chequeno', models.TextField(default=0, null=True)),
                ('response', models.TextField(default=0, null=True)),
                ('mop', models.IntegerField(default=4)),
                ('receipt_amount', models.FloatField()),
                ('status', models.PositiveSmallIntegerField()),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('institute_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='onboarding.DpyInstitute')),
            ],
            options={
                'managed': True,
                'db_table': 'dpy_payment_receipt',
                'verbose_name': 'Dpy Payment Receipt',
            },
        ),
        migrations.CreateModel(
            name='DpyUserFeeIgnore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent_discount', models.FloatField()),
                ('status', models.PositiveSmallIntegerField()),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('institute_class_fee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees_management.DpyInstituteClassFee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'db_table': 'dpy_user_fee_ignore',
                'verbose_name': 'Dpy User Fee Ignore',
            },
        ),
        migrations.AddField(
            model_name='dpyfeetransaction',
            name='institute_class_fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees_management.DpyInstituteClassFee'),
        ),
        migrations.AddField(
            model_name='dpyfeetransaction',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees_management.DpyPaymentReceipt'),
        ),
        migrations.AddField(
            model_name='dpyfeetransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
