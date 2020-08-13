from django.db import models

# Create your models here.
class Region(models.Model):
    RegId = models.AutoField(primary_key=True)
    RegName = models.CharField(max_length=100)

    def __str__(self):
        return self.RegName

    class Meta:
        managed = False
        db_table = '[Partner].[Region]'

class Country(models.Model):

    CntId = models.AutoField(primary_key=True)
    RId = models.IntegerField()
    CName = models.CharField(max_length=50)

    def __str__(self):
        return self.CName

    class Meta:
        managed = False
        db_table = '[Partner].[Country]'

class State(models.Model):
    StId = models.AutoField(primary_key=True)
    CntId = models.IntegerField()
    SName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.SName

    class Meta:
        managed = False
        db_table = '[Partner].[State]'

class District(models.Model):
    DistId = models.AutoField(primary_key=True)
    StId = models.IntegerField()
    DistName = models.CharField(max_length=50)

    def __str__(self):
        return self.DistName

    class Meta:
        managed = False
        db_table = '[Partner].[District]'

class CompanyType(models.Model):
    CtId = models.AutoField(primary_key=True)
    CType = models.CharField(max_length=50)

    def __str__(self):
        return self.CType

    class Meta:
        managed = False
        db_table = '[Partner].[CompanyType]'

class CompanyGroup(models.Model):
    CgId = models.AutoField(primary_key=True)
    CGroup = models.CharField(max_length=20)

    def __str__(self):
        return self.CGroup

    class Meta:
        managed = False
        db_table = '[Partner].[CompanyGroup]'

class SupplyType(models.Model):
    SptId  = models.AutoField(primary_key=True)
    SupplyType = models.CharField(max_length=50)

    def __str__(self):
        return self.SupplyType

    class Meta:
        managed = False
        db_table = '[Partner].[SupplyType]'

class SupplierType(models.Model):
    SltId = models.AutoField(primary_key=True)
    SupplierType = models.CharField(max_length=50)

    def __str__(self):
        return self.SupplierType

    class Meta:
        managed = False
        db_table = '[Partner].[SupplierType]'

class Designation(models.Model):
    DegId = models.AutoField(primary_key=True)
    DegName = models.CharField(max_length=50)

    def __str__(self):
        return self.DegName

    class Meta:
        managed = False
        db_table = '[Partner].[Designation]'

class ContactManagement(models.Model):
    Id = models.AutoField(primary_key=True)
    CId = models.IntegerField()
    ContactPerson = models.CharField(max_length=100)
    Department =  models.CharField(max_length=50)
    DegId = models.IntegerField()
    MobileNo = models.CharField(max_length=10)
    PhoneNo = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return self.ContactPerson

    class Meta:
        managed = False
        db_table = '[Partner].[ContactManagement]'

class Employee(models.Model):
    EmpId = models.AutoField(primary_key=True)
    EmpName = models.CharField(max_length=50)
    StreetAddress = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    DistId = models.ForeignKey('District', on_delete=models.SET_NULL, blank=True, null=True)
    StId = models.IntegerField()
    CntId = models.ForeignKey('Country', on_delete=models.SET_NULL, blank=True, null=True)
    ZipCode = models.CharField(max_length=6)
    DegId = models.ForeignKey('Designation', on_delete=models.SET_NULL, blank=True, null=True)
    MobileNo = models.CharField(max_length=10)
    PhoneNo = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return self.EmpName

    class Meta:
        managed = False
        db_table = '[Partner].[Employee]'

class BranchManagement(models.Model):
    BId = models.AutoField(primary_key=True)
    CId = models.IntegerField()
    BName = models.CharField(max_length=50)
    StreetAddress = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    DistId = models.IntegerField()
    StId = models.IntegerField()
    CntId = models.IntegerField()
    ZipCode = models.CharField(max_length=6)
    ContactPerson = models.CharField(max_length=100)

    def __str__(self):
        return self.BName

    class Meta:
        managed = False
        db_table = '[Partner].[BranchManagement]'

class ShippingInfo(models.Model):
    ShipId = models.AutoField(primary_key=True)
    CId = models.IntegerField()
    ShipName = models.CharField(max_length=50)
    StreetAddress = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    DistId = models.IntegerField()
    StId = models.IntegerField()
    CntId = models.IntegerField()
    ZipCode = models.CharField(max_length=6)

    def __str__(self):
        return self.ShipName

    class Meta:
        managed = False
        db_table = '[Partner].[ShippingInfo]'

class Transpoter(models.Model):
    TransId = models.AutoField(primary_key=True)
    TransName = models.CharField(max_length=50)
    Gstin = models.CharField(max_length=15)
    City = models.CharField(max_length=50)
    DistId = models.IntegerField()
    StId = models.IntegerField()
    CntId = models.IntegerField()
    ZipCode = models.CharField(max_length=6)
    ContactPerson = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=10)
    PhoneNo = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return self.TransName

    class Meta:
        managed = False
        db_table = '[Partner].[Transpoter]'

class TranspoterBranch(models.Model):
    TbId = models.AutoField(primary_key=True)
    TbName = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    DistId = models.IntegerField()
    StId = models.IntegerField()
    CntId = models.IntegerField()
    ZipCode = models.CharField(max_length=6)
    ContactPerson = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=10)
    PhoneNo = models.CharField(max_length=12)
    Email = models.EmailField()

    def __str__(self):
        return self.TbName

    class Meta:
        managed = False
        db_table = '[Partner].[TranspoterBranch]'

class CompanyManagement(models.Model):
    CId = models.AutoField(primary_key=True)
    CtId = models.IntegerField()
    CgId = models.IntegerField()
    Salutation = models.CharField(max_length=5)
    CompanyName = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    DistId = models.IntegerField()
    StId = models.IntegerField()
    CntId = models.IntegerField()
    ZipCode = models.CharField(max_length=6)
    ContactPerson = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=10)
    PhoneNo = models.CharField(max_length=12)
    Email = models.EmailField()
    PaymnetTerm = models.CharField(max_length=100)
    CreditDays = models.IntegerField()
    CreditLimit = models.IntegerField()
    ROIArrear = models.DecimalField(max_digits=5, decimal_places=2)
    Commitment1 = models.BigIntegerField()
    TOD1 = models.IntegerField()
    Commitment2 = models.BigIntegerField()
    TOD2 = models.IntegerField()
    Commitment3 = models.BigIntegerField()
    TOD3 = models.IntegerField()
    DealsIn = models.CharField(max_length=100)
    SlId = models.IntegerField()
    SltId = models.IntegerField()
    DateOfStart = models.DateTimeField()
    CStatus = models.CharField(max_length=1)
    Gstin = models.IntegerField()
    PanNo = models.IntegerField()
    Circle = models.CharField(max_length=20)
    Ward = models.CharField(max_length=20)
    TanNo = models.IntegerField()
    CinNo = models.IntegerField()
    EsiNo = models.IntegerField()
    PfNo = models.IntegerField()
    CstNo = models.CharField(max_length=20)
    TinNo = models.CharField(max_length=20)
    Proof1 = models.TextField(max_length=150)
    ImgProof1 = models.ImageField(upload_to='ImageProof')
    Proof2 = models.TextField(max_length=150)
    ImgProof2 = models.ImageField(upload_to='ImageProof')
    Proof3 = models.TextField(max_length=150)
    ImgProof3 = models.ImageField(upload_to='ImageProof')
    Proof4 = models.TextField(max_length=150)
    ImgProof4 = models.ImageField(upload_to='ImageProof')
    Proof5 = models.TextField(max_length=150)
    ImgProof5 = models.ImageField(upload_to='ImageProof')
    BankName = models.CharField(max_length=50)
    BranchName = models.CharField(max_length=50)
    BankAcName = models.CharField(max_length=50)
    AccountNo = models.IntegerField()
    AccountType = models.CharField(max_length=1)
    IfscCode = models.IntegerField()
    SwiftCode = models.IntegerField()

    def __str__(self):
        return self.CompanyName

    class Meta:
        managed = False
        db_table = '[Partner].[CompanyManagement]'