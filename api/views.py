from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer
from django.shortcuts import get_object_or_404

class ReportListView(APIView):
    """
    GET: すべての報告書を取得
    POST: 新しい報告書を作成
    """
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDetailView(APIView):
    """
    GET: 特定の報告書を取得
    PUT: 特定の報告書を更新
    DELETE: 特定の報告書を削除
    """
    def get(self, request, id):
        report = get_object_or_404(Report, id=id)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, id):
        report = get_object_or_404(Report, id=id)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        report = get_object_or_404(Report, id=id)
        report.delete()
        return Response({"message": "削除しました"}, status=status.HTTP_204_NO_CONTENT)