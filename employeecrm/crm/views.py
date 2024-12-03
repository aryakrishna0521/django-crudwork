from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import EmployeeForm

# Create your views here.
class EmployeeCreateView(View):
    template_name="employee.html"
    form_class=EmployeeForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():
            form_instance.save()

            return redirect('emp-add')

        return render(request,self.template_name,{"form":form_instance})