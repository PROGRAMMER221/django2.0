from django import forms
from .models import ( Region, Country, State, District ,CompanyType, CompanyGroup, SupplyType, SupplierType,
                        ContactManagement, CompanyManagement, Designation, Transpoter, TranspoterBranch, Employee , BranchManagement,
                        ShippingInfo )

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['RegName',]
        widgets = {
            'RegName' : forms.TextInput(attrs={
                'class' : 'form-control col-4'
            })}

        
class CompanyTypeForm(forms.ModelForm):
    class Meta:
        model = CompanyType
        fields = ['CtId','CType']
        widgets = {
            'CType' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

class CompanyGroupForm(forms.ModelForm):
    class Meta:
        model = CompanyGroup
        fields = ['CgId','CGroup']
        widgets = {
            'CGroup' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

class SupplyTypeForm(forms.ModelForm):
    class Meta:
        model = SupplyType
        fields = ['SptId','SupplyType']
        widgets = {
            'SupplyType' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

class SupplierTypeForm(forms.ModelForm):
    class Meta:
        model = SupplierType
        fields = ['SltId','SupplierType']
        widgets = {
            'SupplierType' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['DegId', 'DegName']
        widgets = {
            'DegName' : forms.TextInput(attrs={
                'class' : 'form-control'
            })
        }

