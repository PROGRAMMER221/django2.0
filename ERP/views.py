from django.shortcuts import render, redirect
from .forms import RegionForm,CompanyTypeForm, CompanyGroupForm, SupplyTypeForm, SupplierTypeForm, DesignationForm
from django.db import connection
from .models import ( Region, Country, State, District ,CompanyType, CompanyGroup, SupplyType, SupplierType,
                    ContactManagement, CompanyManagement, Designation, Transpoter, TranspoterBranch, 
                    Employee , BranchManagement, ShippingInfo ) 


# Create your views here.
def BaseView(request):
    return render(request, 'index.html')

def CountryView(request):
    context = {
        'Reg' : Region.objects.all()
    }
    return render(request, 'country.html', context)

def CountryAction(request):
    CName = request.POST['CName']
    RId = request.POST['RId']
    para = (CName, RId)
    cursor = connection.cursor()
    cursor.execute('exec Partner.Country_Ins %s,%s', para)
    return redirect('/country/')

def RegionView(request):
    if request.method == 'POST':
        form = RegionForm(request.POST or None)
        if form.is_valid():
            RegName = form.cleaned_data['RegName']
            para = (RegName,)
            cursor = connection.cursor()
            cursor.execute('exec Partner.Region_Ins %s', para)
            return redirect('/')
    else:
        form = RegionForm()

    return render (request, 'region.html', {'form' : form})

def StateView(request):
    context = {
        'Cnt' : Country.objects.all()
    }
    return render(request, 'state.html', context)

def StateAction(request):
    SName = request.POST['SName']
    CntId = request.POST['CntId']

    para = (SName, CntId)
    cursor = connection.cursor()
    cursor.execute('exec Partner.State_Ins %s,%s', para)
    return redirect('/state/')

def DistrictView(request):
    context = {
        'State' : State.objects.all()
    }
    
    return render(request, 'district.html', context)

def DistrictAction(request):
    DistName = request.POST['DistName']
    StId = request.POST['StId']

    para = (DistName, StId)
    cursor = connection.cursor()
    cursor.execute('exec Partner.District_Ins %s,%s', para)
    return redirect('/district/')

def CompanyTypeView(request):
    if request.method == 'POST':
        form = CompanyTypeForm(request.POST or None)
        if form.is_valid():
            CType = form.cleaned_data['CType']
            para = (CType,)
            cursor = connection.cursor()
            cursor.execute('exec Partner.CompanyType_Ins %s', para)
            return redirect('/')
    else:
        form = CompanyTypeForm()

    return render(request, 'ctype.html', {'form':form})

def EmployeeView(request):
    context = {
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
        'Designation' : Designation.objects.all()
    }
    return render(request, 'employee.html', context)

def EmployeeAction(request):
    EmpName = request.POST['EmpName']
    StreetAddress = request.POST['StreetAddress']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    DegId = request.POST['DegId']
    MobileNo = request.POST['MobileNo']
    PhoneNo = request.POST['PhoneNo']
    Email = request.POST['Email']

    para = (EmpName, StreetAddress, City, DistId, StId, CntId, ZipCode, DegId, MobileNo, PhoneNo, Email)
    cursor = connection.cursor()
    cursor.execute('exec Partner.Employee_Ins %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s', para)
    return redirect('/employee/')

def CompanyGroupView(request):
    if request.method == 'POST':
        form = CompanyGroupForm(request.POST or None)
        if form.is_valid():
            CGroup = form.cleaned_data['CGroup']
            para = (CGroup,)
            cursor = connection.cursor()
            cursor.execute('execute Partner.CompanyGroup_Ins %s', para)
            return redirect('/')
    else:
        form = CompanyGroupForm()

    return render(request, 'cgroup.html', {'form':form})

def SupplyTypeView(request):
    if request.method == 'POST':
        form = SupplyTypeForm(request.POST or None)
        if form.is_valid():
            SupplyType = form.cleaned_data['SupplyType']
            para = (SupplyType,)
            cursor = connection.cursor()
            cursor.execute('execute Partner.SupplyType_Ins %s', para)
            return redirect('/')
    else:
        form = SupplyTypeForm()

    return render(request, 'supply.html', {'form':form})

def SupplierTypeView(request):
    if request.method == 'POST':
        form = SupplierTypeForm(request.POST or None)
        if form.is_valid():
            SupplierType = form.cleaned_data['SupplierType']
            para = (SupplierType,)
            cursor = connection.cursor()
            cursor.execute('execute Partner.SupplierType_Ins %s', para)
            return redirect('/')
    else:
        form = SupplierTypeForm()

    return render(request, 'supplier.html', {'form':form})

def ContactManagementView(request):
    context = {
        'company' : CompanyManagement.objects.all(),
        'designation' : Designation.objects.all()
    }

    return render(request, 'contact.html', context)

def ContactAction(request):
    CId = request.POST['CId']
    ContactPerson = request.POST['ContactPerson']
    Department = request.POST['Department']
    DegId = request.POST['DegId']
    MobileNo = request.POST['MobileNo']
    PhoneNo = request.POST['PhoneNo']
    Email = request.POST['Email']

    para = [CId, ContactPerson, Department, DegId, MobileNo, PhoneNo, Email]
    cursor = connection.cursor()
    cursor.execute('exec ContactManagement_Ins %s, %s, %s, %s, %s, %s, %s', para)
    return redirect('/')

def CompanyManagementView(request):
    context = {
        'companytype' : CompanyType.objects.all(),
        'companygroup' : CompanyGroup.objects.all(),
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
        'supplytype' : SupplyType.objects.all(),
        'suppliertype' : SupplierType.objects.all()

    }
    return render(request, 'company.html', context)

def CompanyAction(request):
    CtId = request.POST['CtId']
    CgId = request.POST['CgId']
    Salutation = request.POST['Salutation']
    CompanyName = request.POST['CompanyName']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    ContactPerson = request.POST['ContactPerson']
    MobileNo = request.POST['MobileNo']
    PhoneNo = request.POST['PhoneNo']
    Email = request.POST['Email']
    PaymnetTerm = request.POST['PaymnetTerm']
    CreditDays = request.POST['CreditDays']
    CreditLimit = request.POST['CreditLimit']
    ROIArrear = request.POST['ROIArrear']
    Commitment1 = request.POST['Commitment1']
    TOD1 = request.POST['TOD1']
    Commitment2 = request.POST['Commitment2']
    TOD2 = request.POST['TOD2']
    Commitment3 = request.POST['Commitment3']
    TOD3 = request.POST['TOD3']
    DealsIn = request.POST['DealsIn']
    SlId = request.POST['SlId']
    SltId = request.POST['SltId']
    DateOfStart = request.POST['DateOfStart']
    CStatus = request.POST['CStatus']
    Gstin = request.POST['Gstin']
    PanNo = request.POST['PanNo']
    Circle = request.POST['Circle']
    Ward = request.POST['Ward']
    TanNo = request.POST['TanNo']
    CinNo = request.POST['CinNo']
    EsiNo = request.POST['EsiNo']
    PfNo = request.POST['PfNo']
    CstNo = request.POST['CstNo']
    TinNo = request.POST['TinNo']
    Proof1 = request.POST['Proof1']
    ImgProof1 = request.POST['ImgProof1']
    Proof2 = request.POST['Proof2']
    ImgProof2 = request.POST['ImgProof2']
    Proof3 = request.POST['Proof3']
    ImgProof3 = request.POST['ImgProof3']
    Proof4 = request.POST['Proof4']
    ImgProof4 = request.POST['ImgProof4']
    Proof5 = request.POST['Proof5']
    ImgProof5 = request.POST['ImgProof5']
    BankName = request.POST['BankName']
    BranchName = request.POST['BranchName']
    BankAcName = request.POST['BankAcName']
    AccountNo = request.POST['AccountNo']
    AccountType = request.POST['AccountType']
    IfscCode = request.POST['IfscCode']
    SwiftCode = request.POST['SwiftCode']
    
    para = [CtId, CgId, Salutation, CompanyName, City, DistId, StId, CntId, ZipCode, ContactPerson, MobileNo, PhoneNo, Email, PaymnetTerm, CreditDays, CreditLimit, ROIArrear, Commitment1, TOD1, Commitment2, TOD2, Commitment3, TOD3, DealsIn, SlId, SltId, DateOfStart, CStatus, Gstin, PanNo, Circle, Ward, TanNo, CinNo, EsiNo, PfNo, CstNo, TinNo, Proof1, ImgProof1, Proof2, ImgProof2, Proof3, ImgProof3, Proof4, ImgProof4, Proof5, ImgProof5, BankName, BranchName, BankAcName, AccountNo, AccountType, IfscCode, SwiftCode]
    cursor = connection.cursor()
    cursor.execute('exec CompanyManagement_Ins %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s')
    return redirect('/company/')

def DesignationView(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST or None)
        if form.is_valid():
            DegName = form.cleaned_data['DegName']
            para = (DegName,)
            cursor = connection.cursor()
            cursor.execute('execute Region.Designation_Ins %s', para)
            return redirect('/')
    else:
        form = DesignationForm()

    return render(request, 'designation.html', {'form':form})

def TranspoterView(request):
    context = {
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
    }
    return render(request, 'transpoter.html', context)

def TranspoterAction(request):
    TransName = request.POST['TransName']
    Gstin = request.POST['Gstin']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    ContactPerson = request.POST['ContactPerson']
    MobileNo = request.POST['MobileNo']
    PhoneNo = request.POST['PhoneNo']
    Email = request.POST['Email']

    para = [TransName, Gstin, City, DistId, StId, CntId, ZipCode, ContactPerson, MobileNo, PhoneNo, Email]
    cursor = connection.cursor()
    cursor.execute('execute Trnaspoter_Ins %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s', para)
    return redirect('/transpoter/')

def TranspoterBranchView(request):
    context = {
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
    }
    return render(request, 'transpoterbranch.html', context)

def TranspoterBranchAction(request):
    TbName = request.POST['TbName']
    Gstin = request.POST['Gstin']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    ContactPerson = request.POST['ContactPerson']
    MobileNo = request.POST['MobileNo']
    PhoneNo = request.POST['PhoneNo']
    Email = request.POST['Email']

    para = [TbName, Gstin, City, DistId, StId, CntId, ZipCode, ContactPerson, MobileNo, PhoneNo, Email]
    cursor = connection.cursor()
    cursor.execute('execute TrnaspoterBranch_Ins %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s', para)

    return redirect('/transpoterbranch/')

def BranchManagementView(request):
    context = {
        'company' : CompanyManagement.objects.all(),
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
    }
    return render(request, 'branch.html', context)

def BranchAction(request):
    CId = request.POST['CId']
    BName = request.POST['BName']
    StreetAddress = request.POST['StreetAddress']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    ContactPerson = request.POST['ContactPerson']

    para = [CId, BName, StreetAddress, City, DistId, StId, CntId, ZipCode, ContactPerson]
    cursor = connection.cursor()
    cursor.execute('execute BranchManagement_Ins %s, %s, %s, %s, %s, %s, %s, %s, %s', para)
    return redirect('/branchmanagement/')

def ShippingInfoView(request):
    context = {
        'company' : CompanyManagement.objects.all(),
        'District' : District.objects.all(),
        'State' : State.objects.all(),
        'Country': Country.objects.all(),
    }
    return render(request, 'shipping.html', context)

def ShippingAction(request):
    CId = request.POST['CId']
    ShipName = request.POST['ShipName']
    StreetAddress = request.POST['StreetAddress']
    City = request.POST['City']
    DistId = request.POST['DistId']
    StId = request.POST['StId']
    CntId = request.POST['CntId']
    ZipCode = request.POST['ZipCode']
    ContactPerson = request.POST['ContactPerson']

    para = [CId, ShipName, StreetAddress, City, DistId, StId, CntId, ZipCode, ContactPerson]
    cursor = connection.cursor()
    cursor.execute('execute BranchManagement_Ins %s, %s, %s, %s, %s, %s, %s, %s, %s', para)
    return redirect('/shipping/')