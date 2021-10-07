from django.urls import reverse,reverse_lazy
class ExceptionCount:
    def __init__(self,get_response):
        self.get_response=get_response
        self.msgs="welcome" #this message we want to render to the template after the view function
        # self.count=0
        self.entry=0
    def __call__(self,request):
        print("hello")
        response=self.get_response(request)#calling the Next View Function/Middleware
        return response #returning the response
    #case:-1
    #---------
    def process_template_response(self,request,response):
        response.context_data["msgs"]=self.msgs
        # return response.render( request,"ProcessOptionalFunctionMiddlewareApp/index.html",{"msgs":self.msgs})
        #adding the Message to the Context while Processing
        #returning the response
        return response
    #case:-2
    #------------
    # def process_exception(self,request,exception):
    #     self.count=self.count+1
    #     print(self.count)
    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     self.entry=self.entry+1
    #     print(f"Number of request is:{self.entry}")


