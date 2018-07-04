# Generated by Django 2.0 on 2018-07-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DpyEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='First Name', max_length=20)),
                ('middle_name', models.CharField(db_column='Middle Name', max_length=20)),
                ('last_name', models.CharField(db_column='Last Name', max_length=20)),
                ('designation', models.CharField(db_column='Designation', max_length=20)),
                ('department', models.CharField(db_column='Department', max_length=20)),
                ('gender', models.CharField(db_column='Gender', max_length=10)),
                ('date_of_join', models.CharField(db_column='Date of Join', max_length=10)),
                ('basic_salary', models.IntegerField(db_column='Basic Salary')),
                ('mobile_number', models.CharField(db_column='Mobile Number', max_length=12)),
                ('email', models.CharField(db_column='Email', max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DpyEmployeeSalaryStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('basic', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('da', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('spal', models.IntegerField()),
                ('med', models.IntegerField()),
                ('others', models.IntegerField()),
                ('tds', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('pt', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_employee_salary_structure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=25)),
                ('leave_type', models.CharField(max_length=25)),
                ('start_date', models.CharField(max_length=25)),
                ('end_date', models.CharField(max_length=25)),
                ('reason', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_employee_leave',
                'managed': False,
            },
        ),
    ]
