# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render

# Local
from .models import (
    Album,
    Artist
)


def index(request: WSGIRequest) -> HttpResponse:
    """index."""

    albums: QuerySet[Album] = Album.objects.all()
    context: dict[str, QuerySet[Any]] = {
        'albums': albums
    }
    return render(
        request,
        'main/index.html',
        context
    )


def detail(
    request: WSGIRequest,
    album_id: int
) -> HttpResponse:
    """detail."""

    user: User = request.user
    album: QuerySet[Album] = Album.objects.get(
        id=album_id
    )
    context: dict[str, QuerySet[Any]] = {
        'album': album,
        'user': user
    }
    return render(
        request,
        'main/detail.html',
        context
    )