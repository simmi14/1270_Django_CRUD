from django.contrib import admin

# Register your models here.

from .models import EmpDetails,Album,Song


# class EmpDetailsAdmin(admin.ModelAdmin):
#     list_display = ('emp_name', 'emp_city', 'emp_company', 'emp_code')
#
#     list_display_links = ('emp_name', 'emp_city', 'emp_company')
#
#     list_filter = ('emp_name', 'emp_city', 'emp_company')
#
#     # search by
#
#     search_fields = ('emp_name__startswith', 'emp_city',)
#
#     # exclude input form field
#
#     # exclude = ('emp_name', )
#
#     @admin.display(description="EMP CODE")
#     def emp_code(self, obj):
#         return f"{obj.emp_name}-----{obj.emp_city}"

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist','song_lyrics')

    list_display_links = ('title', 'artist')

    list_filter = ('title', 'artist')

    # search by
    search_fields = ('title', 'artist',)

    # exclude input form field
    exclude = ('title', )

    @admin.display(description="lyrics")
    def song_lyrics(self, obj):
        return f"{obj.title}-----{obj.artist}"




admin.site.register(EmpDetails)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)
