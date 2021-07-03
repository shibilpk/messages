from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import authentication, permissions

from texts.models import Tag, TextSnippet
from .serializers import TagSerializer, TextSnippetSerializer


class TagList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        snippets = Tag.objects.all()
        serializer = TagSerializer(snippets, many=True)

        response_data = {
            "StatusCode": 6000,
            "data":  {
                "data": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class TagDetail(APIView):

    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TagSerializer(snippet)

        response_data = {
            "StatusCode": 6000,
            "data":  {
                "data": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class TextSnippetList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        snippets = TextSnippet.objects.all()
        serializer = TextSnippetSerializer(snippets, many=True, context={"request": request})

        response_data = {
            "StatusCode": 6000,
            "data":  {
                "data": serializer.data,
                "total_count": snippets.count()
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class TextSnippetCreate(APIView):
    def post(self, request, format=None):
        serializer = TextSnippetSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            tag, created = Tag.objects.get_or_create(tag=request.data['title'].lower())
            serializer.save(creator=request.user, tag=tag)

            response_data = {
                "StatusCode": 6000,
                "data":  {
                    "data": serializer.data,
                }
            }
        else:

            response_data = {
                "StatusCode": 6001,
                "data":  {
                    "data": serializer.errors,
                }
            }
        return Response(response_data, status=status.HTTP_200_OK)


class TextSnippeSnippetDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return TextSnippet.objects.get(pk=pk)
        except TextSnippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TextSnippetSerializer(snippet, context={"request": request})

        response_data = {
            "StatusCode": 6000,
            "data":  {
                "data": serializer.data,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)


class TextSnippetUpdate(APIView):
    def get_object(self, pk):
        try:
            return TextSnippet.objects.get(pk=pk)
        except TextSnippet.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TextSnippetSerializer(snippet, data=request.data, context={"request": request})
        if serializer.is_valid():
            tag, created = Tag.objects.get_or_create(tag=request.data['title'].lower())
            serializer.save(tag=tag)

            response_data = {
                "StatusCode": 6000,
                "data":  {
                    "data": serializer.data,
                }
            }
        else:

            response_data = {
                "StatusCode": 6001,
                "data":  {
                    "data": serializer.errors,
                }
            }
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()

        response_data = {
            "StatusCode": 6001,
            "data":  {
                "message": "Successfully deleted",
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
