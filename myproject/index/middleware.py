
from django.http import JsonResponse
class indexMiddleware:
    def __init__(self,get_response):
          self.get_response=get_response
    def __call__(self,request):
         print(request,"hello")
         if(request.path=="/student/"):
           print(request.method,"method")
           print(request.path)
         elif(request.path=="/sum"):
            print(request.method,"method")
            print(request.path)
         elif(request.path=="/sample1"):
             print(request.method,"method")
             print(request.path)
         elif(request.path=="/sampleinfo"):
             print(request.method,"method")
             print(request.path)
             
         response=self.get_response(request)
         return response
    

    

# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,requset):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob=data.get("dob")
#         psasword=data.get("pswd")

class SscMiddleware:
    def __init__(self,get_response):
          self.get_response=get_response
    def __call__(self,request):
        if(request.path in["job1/","job2/"]):
            ssc_result=(request.GET.get("ssc"))
            print(ssc_result)
            if(not ssc_result):
                return JsonResponse({"error":"u should qulify atleats ssc for applying this job"},status=400)
        return self.get_response(request)

class MedicalFitMiddleware:
    def __init__(self,get_response):
          self.get_response=get_response
    def __call__(self,request):
        if(request.path=="job1/"):
            meddical_fit_result=(request.GET.get("midically_fit"))
            if(meddical_fit_result!='True'):
                return JsonResponse({"error":"u  not medically fit to apply for this job rule "},status=400)
        return self.get_response(request) 
class AgeMiddleware:
    def __init__(self,get_response):
          self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["job1/","job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if((Age_checker>25 and Age_checker<18)):
                return JsonResponse({"error":"age must be in b/w 18 and 25"},status=400)
        return self.get_response(request) 
