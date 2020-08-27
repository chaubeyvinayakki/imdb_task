from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from app.serializers import MovieDetailSerializer, AdminMovieSerializer
from app.response import SuccessResponse
from app.models import MovieDetail


class Admin(APIView):
    """
        class used to handle the admin request, only admin user can access to this class
    """
    permission_classes = (IsAdminUser,)
    serializer_class = AdminMovieSerializer

    def post(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = MovieDetailSerializer(instance)
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :param pk:
        :return:
        """
        movie_id = request.query_params.get('pk')
        if not movie_id:
            return SuccessResponse({"data": "Movie id is required."}, status=status.HTTP_400_BAD_REQUEST)
        movie_instance = MovieDetail.objects.filter(id=movie_id).first()
        if not movie_instance:
            return SuccessResponse({"data": "Invalid movie id."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data, instance=movie_instance)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = MovieDetailSerializer(instance)
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :return:
        """
        movie_id = request.query_params.get('pk')
        if not movie_id:
            return SuccessResponse({"data": "Movie id is required."}, status=status.HTTP_400_BAD_REQUEST)
        movie_instance = MovieDetail.objects.filter(id=movie_id).first()
        if not movie_instance:
            return SuccessResponse({"data": "Invalid movie id."}, status=status.HTTP_400_BAD_REQUEST)
        movie_instance.delete()
        return SuccessResponse({"data": "Movie Deleted successfully."}, status=status.HTTP_201_CREATED)


class User(APIView):
    """
        User class used to handle unauthenticated request, this api is accessed by any one.
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        movie_id = request.query_params.get('pk')
        if not movie_id:
            return SuccessResponse({"data": "Movie id is required."}, status=status.HTTP_400_BAD_REQUEST)
        movie_instance = MovieDetail.objects.filter(id=movie_id)
        serializer = MovieDetailSerializer(movie_instance, many=True)
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)


class SearchMovie(APIView):
    """
        SearchMovie api view to handle the movie search
    """
    serializer_class = MovieDetailSerializer

    def get(self, request):
        queryset = MovieDetail.objects.all()
        # if query params have name, then search by name
        name = request.query_params.get('name', None)
        # if query params have director, then search by director name
        director = request.query_params.get('director', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)
        serializer = self.serializer_class(queryset, many=True)
        return SuccessResponse(serializer.data, status=status.HTTP_200_OK)


