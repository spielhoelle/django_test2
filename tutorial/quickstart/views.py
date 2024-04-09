import os
import json
import os.path
import logging
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@csrf_exempt
@parser_classes((JSONParser,))
def index(request):
	return JsonResponse({"message": "Hello, world!"})

