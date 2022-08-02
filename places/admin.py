from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):

    model = Image

    fields = [
        'img_file',
        'image_preview',
        'index'
    ]

    readonly_fields = ['image_preview', ]

    def image_preview(self, obj):
        headshot_height = 200
        return format_html('<img src="{url}" height={height} />'.format(
                           url=obj.img_file.url,
                           height=headshot_height)
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
