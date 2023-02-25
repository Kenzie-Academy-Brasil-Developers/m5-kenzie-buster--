from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieOrderSerializer
from .permissions import MoviesPermission, MoviesDetailsPermission
from .models import Movie
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, MoviesPermission]

    def get(self, request: Request) -> Response:
        select_movies = Movie.objects.all()
        result_page = self.paginate_queryset(select_movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user_id=request.user.id)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class MoviesOrderViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user_id=request.user.id, movie_id=movie_id)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MoviesDetailViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, MoviesDetailsPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        get_movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(get_movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id) -> Response:
        delete_movie = get_object_or_404(Movie, id=movie_id)

        delete_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



