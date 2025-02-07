from django.shortcuts import render
from auth_mine.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect
import jwt, datetime
from django.http import HttpRequest
import json

SECRET_KEY = 'secret_key' #change it to something better for more security 

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Load JSON data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if User.objects.filter(username = username).exists():
            return JsonResponse({"error":"username should be unique"})
        if User.objects.filter(email = email).exists():
            return JsonResponse({"error":"email should be unique"})
    
        user = User(username = username,email  = email,password = password)
        user.save()
        return JsonResponse({"message":"success"})

@csrf_exempt
def login(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)  # Load JSON data
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            user = User.objects.filter(username=username).first()
            if password == user.password:
                payload = {
                    'id': user.custom_id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                    'iat': datetime.datetime.utcnow(),
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

                response = JsonResponse({"message": "success"})
                response.set_cookie('token', token, max_age=3600)
                return response
            else:
                return JsonResponse({"error": "wrong password"})
        else:
            return JsonResponse({"error": "user doesn't exist"})
        
@csrf_exempt
def check_auth(request:HttpRequest):
    data = request.POST
    token = data.get('token')
    if token is None:
        return JsonResponse({"error":"user unauth"})
    else:
        try:
            decoded_token = jwt.decode(token,"SECRET_KEY",algorithms = ["HS256"])

            return JsonResponse({"success":"user auth"})
        except:
            return JsonResponse({"error":"user unauth"})

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload  # Return the payload if verification is successful
    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Token has expired"}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Invalid token"}, status=401)
