# Generated by Django 2.0.5 on 2018-07-10 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DpyDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_department',
                'verbose_name': 'Department',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteAdditionalField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('field_type', models.PositiveSmallIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_institute_additional_field',
                'verbose_name': 'Field',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=255)),
                ('division', models.CharField(blank=True, max_length=100, null=True)),
                ('batch', models.PositiveSmallIntegerField(default=1)),
                ('sort_index', models.PositiveSmallIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_institute_class',
                'verbose_name': 'Institute Class',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteClassSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_month', models.PositiveSmallIntegerField()),
                ('end_month', models.PositiveSmallIntegerField()),
                ('prerequisite_session', models.IntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_class_session',
                'verbose_name': 'Institute Class Session',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteClassSessionSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('prerequisite_subject', models.IntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_class_session_subject',
                'verbose_name': 'Class Session Subject',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteClassSessionSubjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(default=1)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_class_session_subject_user',
                'verbose_name': 'Class Session Subject User',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteTimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('lecture_no', models.PositiveSmallIntegerField()),
                ('day_id', models.PositiveSmallIntegerField()),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_institute_time_table',
                'verbose_name': 'Time Table',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteUserAdditionalField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dpy_institute_user_additional_field',
                'verbose_name': 'Field',
            },
        ),
        migrations.CreateModel(
            name='DpyInstituteUserClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(default=1)),
                ('roll_no', models.CharField(max_length=20, null=True)),
                ('is_class_teacher', models.PositiveSmallIntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField(default=0)),
                ('ic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='class_user_profiling.DpyInstituteClass')),
            ],
            options={
                'db_table': 'dpy_institute_user_class',
                'verbose_name': 'Institute User Class',
            },
        ),
    ]
