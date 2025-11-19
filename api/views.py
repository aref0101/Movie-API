from rest_framework import viewsets, filters
from .serializers import MovieSerializer, UserRegisterSerializer
from .models import Movie
from .permission import IsAdminOrReadOnly
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset= Movie.objects.all().order_by('-created_at')
    serializer_class= MovieSerializer
    permission_classes= [IsAdminOrReadOnly]
    filter_backends= [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class= MovieFilter
    search_fields= ['title']
    ordering_fields= ['created_at', 'imdb']

    @action(detail= True, methods= ['post'], permission_classes= [IsAuthenticated])
    def bookmark(self, request, pk= None, version= True):
        user= request.user
        target= self.get_object()
        if target.bookmarked_by.filter(pk= user.pk):
            target.bookmarked_by.remove(user)
            return Response({'detail': 'unbookmarked'}, status= status.HTTP_200_OK)
        else:
            target.bookmarked_by.add(user)
            return Response({'detail': 'bookmarked'}, status= status.HTTP_201_CREATED)


class RegisterGenerics(generics.CreateAPIView):
    serializer_class= UserRegisterSerializer


class BookmarkAPIView(generics.ListAPIView, generics.RetrieveAPIView):
    serializer_class= MovieSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(bookmarked_by= self.request.user)