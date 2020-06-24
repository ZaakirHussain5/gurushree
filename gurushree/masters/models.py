from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=25)
    priority = models.IntegerField()
    isActive = models.BooleanField()
    addedBy = models.CharField(max_length=32, null=True)
    addedDate = models.DateTimeField(auto_now_add=True)
    editedBy = models.CharField(max_length=32, null=True)
    editedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subDepartment = models.CharField(max_length=25)
    priority = models.IntegerField()
    isActive = models.BooleanField()
    addedBy = models.CharField(max_length=32, null=True)
    addedDate = models.DateTimeField(auto_now_add=True)
    editedBy = models.CharField(max_length=32, null=True)
    editedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subDepartment + ',' + self.department


class generalType(models.Model):
    genType = models.CharField(max_length=32)
    name=models.CharField(max_length=32, null=True)
    genValue = models.CharField(max_length=32)
    isActive = models.BooleanField()
    addedBy = models.CharField(max_length=32, null=True)
    addedDate = models.DateTimeField(auto_now_add=True)
    editedBy = models.CharField(max_length=32, null=True)
    editedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.genType+','+self.genValue


class registrationType(models.Model):
    regType = models.CharField(max_length=32)
    regFee = models.IntegerField()
    renevalFee = models.IntegerField()
    isActive = models.BooleanField()
    addedBy = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.regType+','+self.regFee


class discounType(models.Model):
    discType = models.CharField(max_length=32)
    discount = models.IntegerField()
    userId = models.CharField(max_length=32)
    password = models.CharField(max_length=1000,null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.discType+','+self.discount


class user(models.Model):
    userName = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=32, null=True)
    fullName = models.CharField(max_length=32, null=True)
    empCode = models.CharField(max_length=32, null=True)
    department = models.CharField(max_length=32, null=True)
    user = models.CharField(max_length=32, null=True)
    counter = models.CharField(max_length=32, null=True)
    mobileno = models.CharField(max_length=32, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=32, null=True)
    marital = models.CharField(max_length=32, null=True)
    date_of_birth = models.CharField(max_length=32, null=True)
    emailid = models.CharField(max_length=32, null=True)
    photo = models.FileField(max_length=355, null=True)
    relationtype = models.CharField(max_length=32, null=True)
    relationname = models.CharField(max_length=32, null=True)
    alternateContact = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=32, null=True)
    isactive = models.BooleanField(null=True)
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName+','+self.emailid


class income_expenses(models.Model):
    Type = models.CharField(max_length=32, null=True)
    particular = models.CharField(max_length=32, null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Type+','+self.particular


class hospital(models.Model):
    hospitalName = models.CharField(max_length=100, null=True)
    address1 = models.CharField( max_length=1000,null=True)
    address2 = models.CharField(max_length=1000, null=True)
    shortName = models.CharField(max_length=32, null=True)
    phone = models.CharField(max_length=32, null=True)
    FAX = models.CharField(max_length=32, null=True)
    pincode = models.CharField(max_length=32, null=True)
    Logo1 = models.FileField(max_length=355, null=True)
    Logo2 = models.FileField(max_length=355, null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospitalName+','+self.shortName


class professional(models.Model):
    title = models.CharField(max_length=32, null=True)
    professionalName = models.CharField(max_length=32, null=True)
    qualification = models.CharField(max_length=32, null=True)
    designation = models.CharField(max_length=32, null=True)
    department = models.CharField(max_length=32,null=True)
    category = models.CharField(max_length=32, null=True)
    OPNewVisit = models.IntegerField(null=True)
    OPRevisit = models.IntegerField(null=True)
    OPfollowup = models.IntegerField(null=True)
    OPShare = models.DecimalField(max_digits=10, decimal_places=2)
    OPShareamount = models.DecimalField(max_digits=10, decimal_places=2)
    IPAmount = models.IntegerField(null=True)
    IPShare = models.DecimalField(max_digits=10, decimal_places=2)
    IPShareamount = models.DecimalField(max_digits=10, decimal_places=2)
    licenceNo = models.CharField(max_length=32, null=True)
    photo = models.FileField(max_length=355, null=True)
    contactNo = models.CharField(max_length=32, null=True)
    email = models.CharField(max_length=32, null=True)
    hospitalName = models.CharField(max_length=32, null=True)
    priority = models.IntegerField(null=True)
    token = models.BooleanField(null=True)
    appointment = models.BooleanField(null=True)
    duration = models.IntegerField(null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title+','+self.professionalName


class menu(models.Model):
    MenuName = models.CharField(max_length=32, null=True)
    MenuIcon = models.CharField(max_length=32, null=True)
    priority = models.IntegerField(null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.MenuName


class pagemaster(models.Model):
    pageName = models.CharField(max_length=32, null=True)
    menuid = models.CharField(max_length=32, null=True)
    submenuName = models.CharField(max_length=32, null=True)
    url = models.CharField(max_length=32, null=True)
    priority = models.IntegerField(null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pageName + ',' + self.submenuName


class State(models.Model):
    name = models.CharField(max_length=32)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.state+','+self.name


class Area(models.Model):
    city = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    pincode = models.CharField(max_length=32)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city+','+self.name

class GenType(models.Model):
    name=models.CharField(max_length=32)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class service(models.Model):
    SerType=models.CharField(max_length=32, null=True)
    ServiceName=models.CharField(max_length=32, null=True)
    ShortName=models.CharField(max_length=32, null=True) 
    DeptId= models.IntegerField(null=True)
    DeptName=models.CharField(max_length=32, null=True)
    SubDeptId = models.IntegerField(null=True)
    SubDeptName=models.CharField(max_length=32, null=True)
    SerAmount = models.IntegerField(null=True)
    OPDrNameinBilling=models.BooleanField(null=True)
    OPReferalBilling=models.BooleanField(null=True)
    OPDiscountApply=models.BooleanField(null=True)
    OPEditServiceAmt=models.BooleanField(null=True)
    OPEditQty=models.BooleanField(null=True)
    OPToken=models.BooleanField(null=True)
    IPDrNameinBilling=models.BooleanField(null=True)
    IPReferalBilling=models.BooleanField(null=True)
    IPDiscountApply=models.BooleanField(null=True)
    IPEditServiceAmt=models.BooleanField(null=True)
    IPEditQty=models.BooleanField(null=True)
    IPToken=models.BooleanField(null=True)
    IRDACode=models.CharField(max_length=32, null=True)
    IRDAName=models.CharField(max_length=32, null=True)
    Outsource=models.BooleanField(null=True)
    BillingSequence= models.IntegerField(null=True)
    isActive = models.BooleanField()
    addedBY = models.CharField(max_length=32, null=True)
    addeddate = models.DateTimeField(auto_now_add=True)
    editedby = models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ServiceName

class packagemapping(models.Model):
    PackCode = models.IntegerField(null=True)
    PackName=models.CharField(max_length=40)
    PackSerCode = models.IntegerField(null=True)
    PackSerName=models.CharField(max_length=40)
    PackSerAmt = models.IntegerField(null=True)
    DrCode = models.IntegerField(null=True)
    isActive =models.BooleanField(null=True)
    AddedBY =models.CharField(max_length=32, null=True)
    Addeddate = models.DateTimeField(auto_now_add=True)
    editedby =models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PackCode

    
