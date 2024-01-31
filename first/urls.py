from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('one',views.cars,name="home"),
    path('petrol',views.petrol,name="petrol"),
    path('diesel',views.diesel,name="diesel"),
    path('electric',views.electric,name="electric"),
    path('cng',views.cng,name="cng"),
    path('tata',views.tata,name="tata"),
    path('mg',views.mg,name="mg"),
    path('mahindra',views.mahindra,name="mahindra"),
    path('maruti',views.maruti,name="maruti"),
    path('hyundai',views.hyundai,name="hyundai"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('det/<int:id>',views.cdetail,name="det"),
    path('tataaltroz',views.tataaltroz,name='tataaltroz'),
    path('mghector',views.mghector,name='mghector'),
    path('mahindraxuv300',views.mahindraxuv300,name='mahindraxuv300'),
    path('marutisuzukiswiftldi',views.marutisuzukiswiftldi,name='marutisuzukiswiftldi'),
    path('hyundaivenue',views.hyundaivenue,name='hyundaivenue'),
    path('tatanexon',views.tatanexon,name='tatanexon'),
    path('mgastor',views.mgastor,name='mgastor'),
    path('mahindrascorpion',views.mahindrascorpion,name='mahindrascorpion'),
    path('marutisuzukifronx',views.marutisuzukifronx,name='marutisuzukifronx'),
    path('hyundaii20nline',views.hyundaii20nline,name='hyundaii20nline'),
    path('tatatiagoev',views.tatatiagoev,name='tatatiagoev'),
    path('mgcometev',views.mgcometev,name='mgcometev'),
    path('mahindraxuv400',views.mahindraxuv400,name='mahindraxuv400'),
    path('marutigrandvitara',views.marutigrandvitara,name='marutigrandvitara'),
    path('hyundaikonaelectric',views.hyundaikonaelectric,name='hyundaikonaelectric'),
    path('tatatiago',views.tatatiago,name='tatatiago'),
    path('mgastorcng',views.mgastorcng,name='mgastorcng'),
    path('mahindrakuv100nxttrip',views.mahindrakuv100nxttrip,name='mahindrakuv100nxttrip'),
    path('marutisuzukispresso',views.marutisuzukispresso,name='marutisuzukispresso'),
    path('hyundaigrandi10nios',views.hyundaigrandi10nios,name='hyundaigrandi10nios')
    


    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)