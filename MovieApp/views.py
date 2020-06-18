from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Rating
from rest_framework.response import Response

@csrf_exempt
@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def RaterView(request):

    rate = request.data.get('rating')
    movie = request.data.get('movie')

    if int(rate)>5 or int(rate)<1 :
        return Response(status=400,data={"error":"You can't provide rating greater than 5 or less than 1"})
    try:
        movie = Movie.objects.get(movie_name=movie)
    except Movie.DoesNotExist as e:
        return Response(status=400, data={"error":"Movie doesn't exist"})

    if movie.creator == request.user:
        return HttpResponse(status=400, content="You can not rate your own movie")

    ratings, created = Rating.objects.get_or_create(movie_name=movie, rater=request.user)
    if not created:
        return HttpResponse(status=400, content="You've already rated this movie")

    ratings.rating=rate
    ratings.save()
    return HttpResponse(content="Rated successfully!!!")


@csrf_exempt
@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def MoviesAdd(request):
    movie=request.data.get('movie')
    try:
        movie, created = Movie.objects.get_or_create(movie_name=movie, creator=request.user)
    except:
        return HttpResponse(status=400, content="Same movie is already created by another user. ")

    if not created:
        return HttpResponse(status=200, content="Movie already present..")

    return HttpResponse("Movie Added Successfully")

