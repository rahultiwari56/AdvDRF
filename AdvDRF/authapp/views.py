import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted Successfully'}
            return JsonResponse(res)

        return JsonResponse(serializer.errors)