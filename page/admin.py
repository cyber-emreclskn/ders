from django.contrib import admin
from .models import Carousel, Page



class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'status',
    )
    list_editable = (
        'title',
        'status',
    )


class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'cover_image',
        'status',
    ]
    list_filter = ['status', ]
    list_editable = list_filter

admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)