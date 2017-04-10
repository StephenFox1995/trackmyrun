from django.shortcuts import render
from .models import Activity


def test_view(request):
    queryset = Activity.objects.all()
    return render(request, 'tracker/activity_list.html')





