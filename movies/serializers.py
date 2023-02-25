from rest_framework import serializers
from accounts.models import User
from .models import Movie, MovieOrder, RatingChoices


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(max_length=150, allow_null=True, default=None)
    rating = serializers.ChoiceField( 
        allow_null=True,
        choices=RatingChoices.choices,
        default=RatingChoices.DEFAULT
    )
    duration = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj: Movie) -> str:
        get_user = User.objects.get(id=obj.user_id)
        return get_user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_buyed_by(self, obj: MovieOrder) -> str:
        get_user = User.objects.get(id=obj.user_id)
        return get_user.email
    
    def get_title(self, obj: MovieOrder) -> str:
        get_movie = Movie.objects.get(id=obj.movie_id)
        return get_movie.title

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
