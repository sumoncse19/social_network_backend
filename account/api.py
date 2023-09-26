from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm

@api_view(['GET'])
def me(request):
  print('Request', request.data)
  result = {
    'id': request.user.id,
    'email' : request.user.email,
    'name' : request.user.name,
    'phone' : request.user.phone
  }
  return JsonResponse(result)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
  print(request.data, 'here request from backend')
  data=request.data
  message='success'
  
  form = SignupForm({
    'email': data.get('email'),
    'name': data.get('name'),
    'phone': data.get('phone'),
    'password1': data.get('password1'),
    'password2': data.get('password2'),
  })
  
  if form.is_valid():
    form.save()
    
    # send verification email later
    
  else:
    message='User form is invalid!'
  
  result = {'status': message}
  
  return JsonResponse(result)