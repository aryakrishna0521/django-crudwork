from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from crm.form import MobileForm,SignInForm,SignUpForm,MobileUpdateForm
from crm.models import Mobile
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from crm.decorators import signin_required

from django.db.models import Q


# Create your views here.
@method_decorator(signin_required,name="dispatch")

class MobileView(View):
    template_name="mobile.html"
    form_class=MobileForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            Mobile.objects.create(**data)
            messages.success(request,"mobile added successfully")
            return redirect("mobile-list")
        messages.error(request,"mobile failed to add")


        return render(request,self.template_name,{"form":form_instance})

@method_decorator(signin_required,name="dispatch")

class MobileList(View):
    template_name="mobile_list.html"
    def get(self,request,*args,**kwargs):
        search_text=request.GET.get("filter")
        # print(query_parameter)
        qs=Mobile.objects.all()
        all_names=Mobile.objects.values_list("name",flat=True).distinct()
        all_brand_types=Mobile.objects.values_list("brand",flat=True).distinct()
        all_ram_types=Mobile.objects.values_list("RAM",flat=True).distinct()
        all_records=[]
        all_records.extend(all_names)
        all_records.extend(all_ram_types)
        all_records.extend(all_brand_types)

        if search_text:
            qs=qs.filter(Q(name__contains=search_text)|Q(brand__contains=search_text)|Q(RAM__contains=search_text))
        return render(request,self.template_name,{"data":qs,"records":all_records})

class MobileDetailsView(View):
    template_name="mobile_details.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Mobile.objects.get(id=id)
        return render(request,self.template_name,{"data":qs})

@method_decorator(signin_required,name="dispatch")

class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Mobile.objects.get(id=id).delete()
        messages.success(request,"mobile deleted successfully")
        return redirect('mobile-list')


@method_decorator(signin_required,name="dispatch")

class MobileUpdateView(View):
    template_name="mobile_edit.html"
    form_class=MobileUpdateForm

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")                                       
         
        mobile_object=get_object_or_404(Mobile,id=id)         
        form_instance=self.form_class(instance=mobile_object)  
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile_object=get_object_or_404(Mobile,id=id)         # id illa vehicle obj edth
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES,instance=mobile_object) #form_insta crete chyth form_data vech initialize cheyth,update work cheyyan instance kodth
        if form_instance.is_valid(): #error check
            form_instance.save()
            messages.success(request,"mobile uppdated successfully")

            return redirect("mobile-list")
        messages.error(request,"mobile failed update")

        return render(request,self.template_name,{"form":form_instance})

class SignUpView(View):
    template_name="register.html" 
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            User.objects.create_user(**data)
            return redirect("register")
        return render(request,self.template_name)

class SignInView(View):
    template_name="login.html"
    form_class=SignInForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:
                login(request,user_object)
                return redirect("mobile-list")
        return render(request,self.template_name,{"form":form_instance})


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
                