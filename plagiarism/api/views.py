from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from models import Key


class SubmitView(APIView):
    def post(self, request):
        content = request.data.get("data")
        keywords = str(content).split()
        for key in keywords:
            if len(key) > 3:
                try:
                    k = Key(key=key.lower().strip(".,;'"))
                    k.save()
                except:
                    pass
        return Response({"status": "Plagiarism text is added."})


class TestView(APIView):
    def post(self, request):
        content = request.data.get("data")
        keywords = str(content).split()
        total, plag = 0, 0
        words = []
        plag_keys = [str(key.key) for key in Key.objects.all()]
        for key in keywords:
            if len(key) > 3:
                total += 1
                if key.lower().strip(".,;'") in plag_keys:
                    plag += 1
                    if key not in words:
                        words.append(key.strip(".,;'"))
        result = (plag/float(total))*100
        return Response({"Plagiarism words": "{}".format(",".join(words)),
                         "Result": "{}% Plagiarism detected".format(round(result, 2))})
