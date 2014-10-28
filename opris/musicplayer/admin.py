from django.contrib import admin
from musicplayer.models import *
# Register your models here.


class CompositorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class MusicCompositionAdmin(admin.ModelAdmin):
    list_display = ["name", "compositor", "genre", "duration", "rating_listen", "rating_user"]
    search_fields = ["compositor", "name", "genre"]


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    search_fields = ["user", "name"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "rating", "user", "music_composition"]
    search_fields = ["user", "music_composition", "text"]


admin.site.site_header = "Music player"
admin.site.site_title = "Music player"
admin.site.register(Compositor, CompositorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MusicComposition, MusicCompositionAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Comment, CommentAdmin)