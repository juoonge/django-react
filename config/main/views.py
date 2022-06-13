from msilib.schema import ServiceInstall
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import ReviewSerializer
from .models import Review

# Create your views here.

# ReviewList-> Review 전체 목록 보여줌
# ReviewDetail-> Review의 세부사항 보여줌

# APIView-> 오버 라이딩 시 메소드 명이 각 HTTP요청의 메소드 명과 똑같다

class ReviewList(APIView):
    def get(self,request):
        reviews=Review.objects.all()

        serializer=ReviewSerializer(reviews,many=True) # 객체 여러개 serialize하려면 many=True
        return Response(serializer.data)

    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):
    def get_object(self,pk): # Review 객체 가져오기
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None): # Review detail 보기
        review=self.get_object(pk)
        serializer=ReviewSerializer(review)
        return Response(serializer.data)

    def put(self,request,pk,format=None): # Review 수정하기
        review=self.get_object(pk)
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None): # Review 삭제하기
        review=self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)