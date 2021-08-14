from django.contrib import admin

from  .models import Article, Project, Cv, Picture, Comment, About
admin.site.register(Article)
admin.site.register(Project)
admin.site.register(Cv)
admin.site.register(Picture)
admin.site.register(About)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)