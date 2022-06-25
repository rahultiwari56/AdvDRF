from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# # Create your views here.
# def index(request):
#     return HttpResponse('Welcome to the Index page')

# Model Object - Single Student Data
def student_details(requet, pk):
    stu_obj = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu_obj)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

#Query Set - All Student Data
def student_list(requet):
    stu_obj = Student.objects.all()
    serializer = StudentSerializer(stu_obj, many=True)
    return JsonResponse(serializer.data)