# Django
from django.contrib import admin
from typing import Optional

# Local
from .models import (
    Artist,
    Band,
    Country,
    Song,
    Genre,
    Album
)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields: tuple[str, ...] = (
        'status',
    )

def get_readonly_fields(
        self,
        request,
        obj: Optional[Artist] = None
    ) -> tuple[str, ...]:
        if obj is None:
            return self.readonly_fields

        return self.readonly_fields + ('release_date',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    CountryAdmin admin.
    """
    readonly_fields = ()

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    """
    BandAdmin admin.
    """
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted'
    )

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """
    ArtistAdmin admin.
    """
    readonly_fields = (
        # 'datetime_created',
        # 'datetime_updated',
        # 'datetime_deleted'
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    readonly_fields: tuple[str, ...] = (
        'duration',
        'times_played'
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass




# class CountryAdmin(admin.ModelAdmin):
#     """
#     CountryAdmin admin.
#     """
#     readonly_fields = ()


# @admin.register(Band)
# class BandAdmin(admin.ModelAdmin):
#     """
#     BandAdmin admin.
#     """
#     readonly_fields = (
#         'datetime_created',
#         'datetime_updated',
#         'datetime_deleted'
#     )

# @admin.register(Artist)
# class ArtistAdmin(admin.ModelAdmin):
#     """
#     ArtistAdmin admin.
#     """
#     readonly_fields = (
#         # 'datetime_created',
#         # 'datetime_updated',
#         # 'datetime_deleted'
#     )


# @admin.register(Song)
# class SongAdmin(admin.ModelAdmin):
#     readonly_fields: tuple[str, ...] = (
#         'duration',
#         'times_played'
#     )


# @admin.register(Genre)
# class GenreAdmin(admin.ModelAdmin):
#     pass


# # admin.site.register(Country, CountryAdmin)
# # admin.site.register(Artist)
# # admin.site.register(Song, SongAdmin)
# # admin.site.register(Genre, GenreAdmin)