from django.shortcuts import render, redirect 
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from CMS.models import *
from CMS.forms import * 


from django.contrib import messages


def index(request):
	context={}
	return render(request,'pindex.html',context)

def aindex(request):
    html = {}
    data=Complaint.objects.all()
    total_complaint = data.count()
    html = {'total_complaint':total_complaint}
    return render(request,'index.html',html)


def home(request):
		context = {}
		return render(request,'home.html',context)

def registerPage(request):
	if request.method =='POST':
		profile_form = UserForm(data=request.POST)
		info_form = InfoProfileForm(data=request.POST)
		if profile_form.is_valid() and info_form.is_valid():
			user = profile_form.save()
			
			user.set_password(user.password)
			user.save()
			profile = info_form.save(commit=False)
			profile.user = user
			profile.save()
			return redirect('/plogin')

			user1 = profile_form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user1)


		else:
			HttpResponse("<h1>Something wrong with form </h1>")
	else:
		profile_form = UserForm(data=request.POST)
		info_form = InfoProfileForm(data=request.POST)


	return render(request,'register.html',{'profile_form':profile_form,'info_form':info_form,})

	
def public(request):
	if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			if user :
				if user.is_active:
						login(request, user)


						return redirect('CMS:index')
			else:
				messages.info(request, 'Username OR password is incorrect')
	context={}
	return render(request,'plogin.html',context)

def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			

			if username == 'Admin12' and password == '3264':
						
		 
						user = authenticate(username=request.POST['username'], password=request.POST['password'])
			
						if user :
							if user.is_active:
									login(request, user)
									return redirect('CMS:aindex')
			else:
				messages.info(request, 'Username OR password is incorrect')

		
		return render(request, 'login.html')


def logoutUser(request):
				logout(request)
				return redirect('CMS:home')
def logoutP(request):
				logout(request)
				return redirect('CMS:home')

def views(request):
	context={}
	data=Complaint.objects.all()
	total_complaint = data.count()
	context = {'data':data }
	return render(request,'viewscomplaint.html',context)



def complaint(request):
		context={}
		if request.method == 'POST':
				data = ComplaintForm(data=request.POST)
				data.save()
				return redirect('/index')
				print ("..........saved successfully.............")
				context['save'] = "Data saved successfully"
				return redirect('CMS:complaint')
				
				
				


		a=ComplaintForm()
		context['data']=a
	
		print('______________________got here +++++++++++++++++++++'),context['data']
		return render(request,'Complaint.html',context)

def updatestatus(request, pk):

	order = Complaint.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('CMS:aindex')

	context = {'form':form}
	return render(request, 'update.html', context)

def complaint_status(request):
	if request.method == 'POST':
			form = StatusForm(request.POST) 
			if form.is_valid():
				cd = form.cleaned_data['idnumber']
				
				status = Complaint.objects.get(id=cd)
				form = StatusForm()
				# After submission of complaint user will be shown homepage
				return render(request, 'status.html', {'form':form, 'status':status})
			
	else:
			# If the request was not a POST, display the form to enter details.
		form = StatusForm()

	return render(request, 'status.html', {'form':form, 'cs':"active"})


def viewscompp(request):
	context={}
	if 'user.id' in request.GET:
		name=request.GET['user.id']
		data=Complaint.objects.filter(user_id=name)
		if data:
			context['data']=data
			messages.info(request, " your complaints ")

	return render(request,'viewscompp.html',context)


def viewcomplid(request):
	context={}
	if 'name' in request.GET:
		name=request.GET['name']
		data=Complaint.objects.filter(user_id=name)
		if data:
			context['data']=data
		else:
			messages.info(request, "This Zone doesn't exist. Enter Valid one !!")
	return render(request,'vcomplid.html',context)
	



def viewsemp(request):
	context={}
	if 'name' in request.GET:
		name=request.GET['name']
		data=Employee.objects.filter(zone=name)
		if data:
			context['data']=data
		else:
			messages.info(request, "This Zone doesn't exist. Enter Valid one !!")

		
		
		

	return render(request,'viewsemp.html',context)


