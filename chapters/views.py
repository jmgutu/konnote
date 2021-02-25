# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from chapters.models import Chapter

# Create your views here.


def chapters(request):
    all_chapters = Chapter.objects.all()
    my_list = [1, 2, 3, 4, 5]
    args = {
        'day': 'Tuesday',
        'time': 'Night',
        'my_list': my_list,
        'all_chapters': all_chapters
    }
    return render(request, 'home.html', args)
