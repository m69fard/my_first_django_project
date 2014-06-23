from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    Position = (('GK', 'Goal Keeper'), ('D', 'Defender'), ('M', 'Midfielder'), ('F', 'Forward'),)
    position = models.CharField(max_length=2, choices=Position, null=True, blank=True)
    country = models.ForeignKey('Team',related_name='players')
    in_team = models.BooleanField(verbose_name='In Team')
    club = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['last_name']

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Coach(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    Country = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
        ordering = ['last_name']

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Team(models.Model):
    name = models.CharField(max_length=30)
    continent = models.CharField(max_length=30)
    world_ranking = models.IntegerField(max_length=100, null=True, blank=True)
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='teams')
    flag = models.ImageField(blank=True, null=True, upload_to='image/flag')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']

    def __str__(self):
        return self.name


class Match(models.Model):
    first_team = models.ForeignKey(Team, related_name='matches_as_first_team')
    first_team_goals = models.IntegerField(max_length=1, null=True, blank=True)
    second_team = models.ForeignKey(Team, related_name='matches_as_second_team')
    second_team_goals = models.IntegerField(max_length=1, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    like = models.ManyToManyField(User, related_name='like_matches', null=True, blank=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return '%s %s-%s %s' % (self.first_team, self.first_team_goals, self.second_team_goals, self.second_team)

    def likes(self, user):
        return user in self.like.all()

    def like_count(self):
        return self.like.all().count()


class News(models.Model):
    head_line = models.TextField(max_length=50)
    summary = models.TextField(max_length=200)
    text = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, null=True, upload_to='image/news')
    date = models.DateField()
    tags = models.ManyToManyField('Tag', null=True, blank=True, related_name='news')
    like = models.ManyToManyField(User, null=True, blank=True, related_name='like_news')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.head_line

    def likes(self, user):
        return user in self.like.all()

    def like_count(self):
        return self.like.all().count()


class CommentOfMatch(models.Model):
    text = models.TextField(max_length=200, verbose_name='Comment')
    user = models.ForeignKey(User, related_name='comments_match')
    match = models.ForeignKey(Match, related_name='comments')
    like = models.ManyToManyField(User, null=True, blank=True, related_name='like_comments_match')


class CommentOfNews(models.Model):
    text = models.TextField(max_length=200, verbose_name='Comment')
    user = models.ForeignKey(User, related_name='comments_news')
    news = models.ForeignKey(News, related_name='comments')
    like = models.ManyToManyField(User, null=True, blank=True, related_name='like_comments_news')


class Tag(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name
