from django.shortcuts import render

# Create your views here.
from .workbb import myfuncbb,workbb
from .formBB import ContractFormBB
from django.views import View
class HomeView(View):
    def get(self,request):
        print("get request")
        form_obj=ContractFormBB()
        return render(request,"frgtbb/homey.html",{"frm": form_obj})

    
    def post(self,request):
        print("post baby")    
        form_obj=ContractFormBB(request.POST)
        if form_obj.is_valid():
            lst_nm=form_obj.cleaned_data["namey"]
            st_nm=form_obj.cleaned_data["starting_number"]
            end_nm=form_obj.cleaned_data["ending_number"]
            st_nm=int(st_nm)
            end_nm=int(end_nm)

            print(lst_nm,st_nm,end_nm)
            length_msg=myfuncbb(lst_nm,st_nm,end_nm)
            print("msg baby",length_msg)
            print("msg baby",type(length_msg))
            # return render(request,"frgtbb/homey.html",{"frm": form_obj})
            return render(request,"frgtbb/homey.html",{"frm": form_obj,'response_bb':True,"lengthybb":length_msg})
        else:
            return render(request,'myappz/homey.html',{"frm": form_obj,'error_bb':True})
        # messages.success(request,"Account created baby")            # bOTH SAME .....most of the people  use it  
            
        # from django.http import HttpResponse
        # return  HttpResponse("done")

        # return HttpResponseRedirect("/")




    

