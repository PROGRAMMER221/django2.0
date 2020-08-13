from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.BaseView, name="base"),
    url(r'^country/$', views.CountryView, name='country'),
    url(r'^countryaction/$', views.CountryAction, name='countryaction'),
    url(r'^region/$', views.RegionView, name='region'),
    url(r'^state/$', views.StateView, name='state'),
    url(r'^stateaction/$', views.StateAction, name='stateaction'),
    url(r'^district/$', views.DistrictView, name='district'),
    url(r'^districtaction/$', views.DistrictAction, name='districtaction'),
    url(r'^companytype/$', views.CompanyTypeView, name='companyType'),
    url(r'^companygroup/$', views.CompanyGroupView, name='companygroup'),
    url(r'^employee/$', views.EmployeeView, name='form'),
    url(r'^employeeaction/$', views.EmployeeAction, name='employeeaction'),
    url(r'^ctype/$', views.CompanyTypeView, name='ctype'),
    url(r'^cgroup/$', views.CompanyGroupView, name='cgroup'),
    url(r'^supplytype/$', views.SupplyTypeView, name='supplytype'),
    url(r'^suppliertype/$', views.SupplierTypeView, name='suppliertype'),
    url(r'^designation/$', views.DesignationView, name='designation'),
    url(r'^contactmanagement/$', views.ContactManagementView, name='contactmanagement'),
    url(r'^contact/$', views.ContactAction, name='contact'),
    url(r'^transpoter/$', views.TranspoterView, name='transpoter'),
    url(r'^transpoteraction/$', views.TranspoterAction, name='transpoteraction'),
    url(r'^transbranch/$', views.TranspoterBranchView, name='transbranch'),
    url(r'^transbranchaction/$', views.TranspoterBranchAction, name='transbranchaction'),
    url(r'^branchmanagement/$', views.BranchManagementView, name='branchmanagement'),
    url(r'^branchaction/$', views.BranchAction, name='branchaction'),
    url(r'^shippinginfo/$', views.ShippingInfoView, name='shippinginfo'),
    url(r'^shipaction/$', views.ShippingAction, name='shipaction'),
    url(r'^company/$', views.CompanyManagementView, name='company'),
    url(r'^companyaction/$', views.CompanyAction, name='companyaction'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)