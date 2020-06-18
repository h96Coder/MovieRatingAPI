
from . import models as e
from django.contrib import admin


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'creator_id')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie_name','rating','rater_id')


admin.site.register(e.Rating,RatingAdmin)
admin.site.register(e.Movie,MovieAdmin)

# Register your models here.
