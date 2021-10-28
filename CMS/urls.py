from django.conf.urls import  url
from CMS.views import *

urlpatterns = [
				url(r'^$',home,name = 'home'),
				url(r'^login/$', loginPage, name='login'),
				url(r'^plogin/$', public, name='plogin'),
				url(r'^logout/$', logoutUser, name='logout'),
				url(r'^logoutp/$', logoutP, name='logoutp'),
				url(r'^aindex/$', aindex, name='aindex'),
      			url(r'^index$', index, name='index'),
      			url(r'^register/$', registerPage, name='register'),
				url(r'^complaint/$',complaint,name='complaint'),
				url(r'^status/', complaint_status, name='status'),
				url(r'^viewscomplaint/', views, name='viewscomplaint'),
				url(r'^viewscompp/', viewscompp, name='viewscompp'),
				url(r'^update/(?P<pk>\w{0,50})/$',updatestatus,name='update'),
				url(r'^vcd/', viewcomplid, name='vcd'),
				url(r'^viewsemp/', viewsemp, name='viewsemp'),
				

        

	
]

