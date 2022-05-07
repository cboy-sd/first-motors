from django.contrib import admin
from .models import Team, Service, Company_Story, Dashboard, ContactUs, \
    Stories, Products



class TeamAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'job', 'id']
    search_fields = ['member_name']
    readonly_fields = ['id']


class Company_StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'p1', 'p2']
    search_fields = ['title', 'p1', 'p2']
    readonly_fields = ['id']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_info']
    readonly_fields = ['id']
    search_fields = ['service_name']


class DashboardAdmin(admin.ModelAdmin):
    list_display = ['clients', 'products', 'services', 'employees']
    readonly_fields = ['id']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'message']


class StoriesAdmin(admin.ModelAdmin):
    list_display = ['story_title', 'body']
    read_only = ['id']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    readonly_fields = ['id']



admin.site.register(Company_Story, Company_StoryAdmin)

admin.site.register(Team, TeamAdmin)

admin.site.register(Service, ServiceAdmin)

admin.site.register(ContactUs, ContactUsAdmin)

admin.site.register(Dashboard, DashboardAdmin)

admin.site.register(Stories, StoriesAdmin)

admin.site.register(Products, ProductsAdmin)
