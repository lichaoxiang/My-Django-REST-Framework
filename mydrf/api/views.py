# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
#
# from snippets.models import Snippet
# from api.serializers import SnippetSerializer
#
#
# class JSONResponse(HttpResponse):
#     '''
#     An HttpResponse that renders its content into JSON.
#     '''
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def snippet_list(request):
#     '''
#     列出所有的 `Snippet`，或创建一个新的 `Snippet`
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     '''
#     获取、更新或删除一个 `Snippet`
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)







# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from snippets.models import Snippet
# from api.serializers import SnippetSerializer
#
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     '''
#     列出所有的 `Snippet`，或者创建一个新的 `Snippet`
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     '''
#     获取，更新或删除一个 `Snippet` 实例
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# from snippets.models import Snippet
# from api.serializers import SnippetSerializer
#
#
# class SnippetList(APIView):
#     '''
#     列出所有的 `Snippet` 或者创建一个新的 `Snippet`
#     '''
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     '''
#     检索，更新或删除一个 `Snippet` 示例
#     '''
#     def get_object(self, pk):
#     # 重写 get_obj 方法，根据 pk 查找文章分类
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)   # 获取对象
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# from rest_framework import generics
#
# from snippets.models import Snippet
# from api.serializers import SnippetSerializer
#
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer







# from rest_framework import generics
#
# from .serializers import SnippetSerializer
# from .permissions import IsOwnerOrReadOnly
# from snippets.models import Snippet
#
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsOwnerOrReadOnly, )  # 注意这里是元祖
#
#     def perform_create(self, serializer):
#         '''
#         重写 perform_create 方法，在保存模型实例时，会自动将录入用户写入模型实例
#         '''
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsOwnerOrReadOnly, )







# from rest_framework import generics
#
# from .serializers import SnippetSerializer
# from .permissions import IsAdminUserOrReadOnly
# from snippets.models import Snippet
#
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsAdminUserOrReadOnly, )
#     def perform_create(self, serializer):
#         '''
#         重写 perform_create 方法，在保存模型实例时，会自动将录入用户写入模型实例
#         '''
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsAdminUserOrReadOnly, )







from rest_framework import viewsets, permissions

from .serializers import SnippetSerializer
from .permissions import IsAdminUserOrReadOnly
from snippets.models import Snippet


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAdminUserOrReadOnly, )   # 系统级权限

    def perform_create(self, serializer):
        '''
        重写 perform_create 方法，在保存模型实例时，会自动将录入用户写入模型实例
        '''
        serializer.save(owner=self.request.user)