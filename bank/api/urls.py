from django.conf.urls import url
from .views import BankAPIView,BankCreateAPIView,BankDetailAPIView,BankUpdateAPIView,BankDeleteAPIView

urlpatterns = [
	url(r'^$', BankAPIView.as_view()),
	url(r'^create/$', BankCreateAPIView.as_view()),
	url(r'^(?P<pk>\d+)/$', BankDetailAPIView.as_view()),
	url(r'^(?P<pk>\d+)/update/$',BankUpdateAPIView.as_view()),
	url(r'^(?P<pk>\d+)/delete/$',BankDeleteAPIView.as_view()),
]
