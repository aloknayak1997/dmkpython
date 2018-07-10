from django.db import models
from onboarding.models import DpyInstitute, DpyUsers
from class_user_profiling.models import DpyDepartment, DpyInstituteClass, DpyInstituteClassSession, DpyInstituteClassSessionSubjects
from dashboard.models  import DpyStudents
# Create your models here.
	
class DpyFeeType(models.Model):
    desc = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'dpy_fee_type'


class DpyInstituteClassFee(models.Model):
    amount = models.IntegerField()
    cycle = models.PositiveSmallIntegerField()
    display_name = models.CharField(max_length=250)
    bifurcations = models.TextField(blank=True, null=True)
    status = models.PositiveSmallIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=0)
    fee_type = models.ForeignKey(DpyFeeType, models.DO_NOTHING)
    institute_class = models.ForeignKey(DpyInstituteClass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dpy_institute_class_fee'

class DpyUserFeeIgnore(models.Model):
    percent_discount = models.FloatField()
    status = models.PositiveSmallIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=0)
    institute_class_fee_id = models.ForeignKey(DpyInstituteClassFee, models.DO_NOTHING)
    user_id = models.ForeignKey(DpyUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dpy_user_fee_ignore'

class DpyPaymentReceipt(models.Model):
    token_or_chequeno = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    mop = models.IntegerField()
    receipt_amount = models.FloatField()
    status = models.PositiveSmallIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=0)
    institute_id = models.ForeignKey(DpyInstitute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dpy_payment_receipt'


class DpyFeeTransaction(models.Model):
    paid_amount = models.FloatField()
    cycle = models.IntegerField()
    cycle_slot = models.IntegerField()
    dsc = models.TextField()
    mop = models.IntegerField()
    status = models.PositiveSmallIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(default=0)
    institute_class_fee_id = models.ForeignKey(DpyInstituteClassFee, models.DO_NOTHING)
    receipt_id = models.ForeignKey(DpyPaymentReceipt, models.DO_NOTHING)
    user_id = models.ForeignKey(DpyStudents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dpy_fee_transaction'
