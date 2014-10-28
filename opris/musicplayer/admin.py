from django.contrib import admin
from musicplayer.models import *
# Register your models here.


class CompositorAdmin(admin.ModelAdmin):
    list_display = ["name"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MusicCompositionAdmin(admin.ModelAdmin):
    list_display = ["compositor", "name", "genre", "duration", "rating_listen", "rating_user"]


admin.site.site_header = "Music player"
admin.site.site_title = "Music player"
admin.site.register(Compositor, CompositorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MusicComposition, MusicCompositionAdmin)
admin.site.register(Playlist)
admin.site.register(Comment)