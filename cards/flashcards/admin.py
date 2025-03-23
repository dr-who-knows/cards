from django.contrib import admin
from .models import Card, UserProfile

class CardAdmin(admin.ModelAdmin):
    list_display = ('original_word', 'translation', 'date_added')
    search_fields = ('original_word', 'translation')
    list_filter = ('date_added',)
    ordering = ('-date_added',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'canvas_translate_x', 'canvas_translate_y', 'canvas_scale')
    search_fields = ('user__username', 'user__email')
    list_filter = ('canvas_scale',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Canvas Position', {
            'fields': ('canvas_translate_x', 'canvas_translate_y', 'canvas_scale'),
            'description': 'These values control the canvas view position for this user'
        }),
    )

admin.site.register(Card, CardAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
