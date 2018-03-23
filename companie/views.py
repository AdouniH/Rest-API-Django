# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import response
from .models import Stock
from.serializers import StockSerializer
# Create your views here.

class StockList(APIView):
    def get(self):
        pass

    def post(self):
        pass
