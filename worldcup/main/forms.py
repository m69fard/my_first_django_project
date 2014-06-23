from django.forms import ModelForm
from main.models import CommentOfNews, CommentOfMatch

from django.contrib.auth.models import User


class NewsCommentForm(ModelForm):
    class Meta:
        model = CommentOfNews
        fields = ['text']

    def save(self, commit=True, user=None, piece_news=None):
        if not self.instance.pk:
            self.instance.user = user
            self.instance.news = piece_news
        return super(NewsCommentForm, self).save(commit)


class MatchCommentForm(ModelForm):
    class Meta:
        model = CommentOfMatch
        fields = ['text']

    def save(self, commit=True, user=None, match=None):
        if not self.instance.pk:
            self.instance.user = user
            self.instance.match = match
        return super(MatchCommentForm, self).save(commit)
