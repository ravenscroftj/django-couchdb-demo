from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from papers.models import Paper, SERVER
from papers.serializers import PaperSerializer


db = SERVER['papers']

@api_view(['POST'])
def create_paper(request):
    """Take JSON post and create paper record"""
    data = JSONParser().parse(request)

    serializer = PaperSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET'])
def paper_detail(request, paper_id):
    """Show details for given paper"""
    paper = Paper.load(db, paper_id)
    serializer = PaperSerializer(paper)
    return Response(serializer.data)
