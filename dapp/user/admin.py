from re import search
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from user.models import *


class ProfileModelInline(admin.StackedInline):
    model = ProfileModel
    can_delete = False
    verbose_name_plural = 'Профиль пользователя'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileModelInline,)


class LikeProdAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user')
    list_display_links = ('id', 'product', 'user')
    list_filter = ('user',)
    search_fields = ('user', 'product',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'grade', 'visible')
    list_display_links = ('id', 'product', 'user', 'grade',)
    list_editable = ('visible',)
    search_fields = ('user', 'product',)
    list_filter = ('user',)
    readonly_fields = ('product', 'user', 'grade', )


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id' , 'completed', 'city', 'uuid','person', 'theme',)
    list_display_links = ('id' , 'completed', 'person', 'theme',)
    search_fields = ('person', )
    list_filter = ('theme', )
    readonly_fields = ('person', 'theme', 'contact', 'text',)


class UserWatcherAdmin(admin.ModelAdmin):

    def parse_prods(self, instance):
        products = instance.prods
        data = render_to_string('admin_prods.html', {"viewed": products["viewed"], "comp": products["comp"], "like": products["like"], })
        return data
    
    parse_prods.short_description = 'Товары'


    list_display = ('id', )
    list_display_links = ('id', )
    readonly_fields = ('prods', 'parse_prods',)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(SubscriberModel)
admin.site.register(FeedBackModel, FeedBackAdmin)
admin.site.register(LikeProdModel, LikeProdAdmin)
admin.site.register(ProductReviewModel, ProductReviewAdmin)
admin.site.register(UserWatcherModel, UserWatcherAdmin)