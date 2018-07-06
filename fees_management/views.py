from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
# from urllib.parse import urlparse
# from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from onboarding.models import DpyInstitute, DpyInstituteUsers, DpyUsers
from dashboard.models import DpyStudents
from .models import DpyFeeType, DpyInstituteClassFee
from class_user_profiling.models import DpyDepartment, DpyInstituteClass, DpyInstituteClassSession, DpyInstituteClassSessionSubjects 
from onboarding.serializers import InstituteUserSerializer, UserSerializer
# Create your views here.


from django.views.decorators.csrf import csrf_exempt
@login_required(login_url='/')
@csrf_exempt

def add_fee(request):
	queryset = DpyInstituteUsers.objects.get(user_id=request.user.id)
	serializer = InstituteUserSerializer(queryset)
	InstUserid = (serializer.data["id"])
	InstUser = DpyInstituteUsers.objects.get(id=InstUserid)
	students = DpyStudents.objects.all().filter(institute_id = InstUser.institute_id).order_by('student_class','section')
	total_classes = DpyInstituteClass.objects.all().filter(institute_id = InstUser.institute_id).order_by('standard','division')
	# section_class = []
	institute_classes = []
	counter = 0
	# for student in students:
	# 	student_class = student.student_class
	# 	student_section =student.section
	# 	student_class_section = student_class +" "+ student_section
	# 	if student_class_section in section_class:
	# 		continue
	# 	print(student_class_section)
	# 	section_class.append(student_class_section)
	for one_class in total_classes:
		institute_class = one_class.standard
		class_section = one_class.division
		institute_classes.append(institute_class+""+class_section)
	if request.method == 'GET':
		return render(request,'fees_management/add_fee.html',{'section_class':institute_classes,'students':students})
	# return render(request,'add_fee.html',{})

	if request.method == 'POST':
		formData = request.POST.getlist('formData[]')
		classes = request.POST.getlist('classes[]')
		fee = DpyFeeType(desc=formData[0])
		fee.save()
		for i in range(0,len(classes),1):
			one_class = classes[i]
			# fee_class = one_class[:-1]
			# section = one_class[-1:]
			print(student_class)
			print(section)
		
		InstituteClass = DpyInstituteClass.objects.get(institute_id=serializer.data["institute"])
		# for i in range(0,len(classes),1):
		# 	one_class = classes[i]
		# 	fee_class = one_class[:-1]
		# 	section = one_class[-1:]
		# 	print(student_class)
		# 	print(section)
		# 	# fee_class_section = DpyInstituteClass
		# 	class_id =  DpyInstituteClass.objects.all().filter(standard=fee_class,division=section)
		# 	inst_class_fee = DpyInstituteClassFee(amount=int(formData[1]),cycle=formData[2],bifurcations='-',fee_type_id=fee.id,institute_class_id=class_id)
		# 	inst_class_fee.save()
		response_data ={'Status':True, 'Message': attendence_date }
		return HttpResponse(json.dumps(response_data), content_type="application/json")
		return render(request,'fees_management/add_fee.html',{})

def pay(request):
	queryset = DpyInstituteUsers.objects.get(user_id=request.user.id)
	serializer = InstituteUserSerializer(queryset)
	InstUserid = (serializer.data["id"])
	InstUser = DpyInstituteUsers.objects.get(id=InstUserid)
	students = DpyStudents.objects.all().filter(institute_id = InstUser.institute_id).order_by('student_class','section')
	total_classes = DpyInstituteClass.objects.all().filter(institute_id = InstUser.institute_id).order_by('standard','division')
	fees = DpyInstituteClassFee.objects.all()
	i=0
	data = {}    
	for one_class in total_classes:
		data[i]= {
			'class_sec':one_class.standard+one_class.division,
			'class_id':str(one_class.id)
		}
		i=i+1
	institute_classes = []
	counter = 0
	for one_class in total_classes:
		institute_class = one_class.standard
		class_section = one_class.division
		calss_id=str(one_class.id)
		institute_classes.append(institute_class+""+class_section)
	
	if request.method == 'GET':
		return render(request,'fees_management/pay.html',{'section_class':data,'total_classes':total_classes,'students':students,'fees':fees})

	if request.method == 'POST':
		formData = request.POST.getlist('formData[]')
		classes = request.POST.getlist('classes[]')
		fee = DpyFeeType(desc=formData[0])
		fee.save()
		for i in range(0,len(classes),1):
			one_class = classes[i]
			print(student_class)
			print(section)
		
		InstituteClass = DpyInstituteClass.objects.get(institute_id=serializer.data["institute"])
		response_data ={'Status':True, 'Message': attendence_date }
		return HttpResponse(json.dumps(response_data), content_type="application/json")
		return render(request,'fees_management/pay.html',{})
