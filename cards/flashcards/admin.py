from django.contrib import admin
from .models import Card, UserProfile

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('original_word', 'translation', 'date_added')
    search_fields = ('original_word', 'translation')
    list_filter = ('date_added',)
    ordering = ('-date_added',)

admin.site.register(UserProfile)
