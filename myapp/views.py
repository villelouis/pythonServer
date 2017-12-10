from django.shortcuts import render

#Чтобы вернуть строку
from django.http import JsonResponse
import json
from django.utils import timezone
from django.core import serializers
# from .models import Post

# Create your views here.
def post_list(request):
	#	Запрос к БД
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# posts_serialized = serializers.serialize('json', posts)
	# return JsonResponse(posts_serialized, safe=False)
	pass
 
def post_list2(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'myapp/post_list.html', {'posts': posts})
	pass
  
    