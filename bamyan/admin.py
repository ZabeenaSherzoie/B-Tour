from django.contrib import admin
from .models import TourAgency, Season, Package, Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(TourAgency)
class TourAgencyAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')


@admin.register(Package)
class PackageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'duration', 'slug', 'group_size')
    search_fields = ('title', 'season')
    list_filter = ('season',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'note')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'package', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


admin.site.register(Season)