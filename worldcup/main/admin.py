from django.contrib import admin

# Register your models here.
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from main.models import Team, Player, Coach, Match, News, Tag, CommentOfNews, CommentOfMatch


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent', 'coach', 'world_ranking', 'flag')
    search_fields = ('name', 'continent')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'position', 'club')
    #
    '''
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    raw_id_fields = ('publisher',)
    '''


class CoachAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'Country')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('first_team', 'first_team_goals', 'second_team', 'second_team_goals', 'date', 'time')
    filter_horizontal = ('like',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('head_line', 'date')
    date_hierarchy = 'date'
    filter_horizontal = ('tags', 'like')


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CommentOfNews)
admin.site.register(CommentOfMatch)
admin.site.register(Tag)