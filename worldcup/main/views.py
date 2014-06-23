from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .models import Team, Match, News, Tag
from .forms import NewsCommentForm, MatchCommentForm


def home(request):
    teams = Team.objects.all()
    news = News.objects.all()
    matches = Match.objects.all()
    context = {'teams': teams, 'news': news, 'matches': matches}
    return render(request, 'home.html', context)


def team_detail(request, name):
    team = get_object_or_404(Team, name=name)
    news = News.objects.all()
    matches = Match.objects.all()
    goalkeepers = team.players.all().filter(position='GK')
    defenders = team.players.all().filter(position='D')
    midfielders = team.players.all().filter(position='M')
    forwards = team.players.all().filter(position='F')
    context = {'team': team, 'news': news, 'matches': matches, 'goalkeepers': goalkeepers,
               'defenders': defenders, 'midfielders': midfielders, 'forwards': forwards}
    return render(request, 'main/team_detail.html', context)


def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    comments = match.comments.all()
    news = News.objects.all()
    matches = Match.objects.all()
    first_team = match.first_team
    second_team = match.second_team
    likes = match.likes(request.user)
    if request.method == 'POST':
        form = MatchCommentForm(data=request.POST)
        if form.is_valid():
            form.save(user=request.user, match=Match.objects.get(id=match_id))
            return redirect('main_match_detail', match_id)
    else:
        form = MatchCommentForm()
    context = {'match': match, 'news': news, 'first_team': first_team, 'second_team': second_team,
               'matches': matches, 'form': form, 'comments': comments, 'likes': likes}
    return render(request, 'main/match_detail.html', context)


def news_detail(request, news_id):
    piece_news = get_object_or_404(News, id=news_id)
    comments = piece_news.comments.all()
    news = News.objects.all()
    matches = Match.objects.all()
    likes = piece_news.likes(request.user)
    tags = piece_news.tags.all()
    if request.method == 'POST':
        form = NewsCommentForm(data=request.POST)
        if form.is_valid():
            form.save(user=request.user, piece_news=News.objects.get(id=news_id))
            return redirect('main_news_detail', news_id)
    else:
        form = NewsCommentForm()
    context = {'piece_news': piece_news, 'comments': comments, 'news': news,
               'matches': matches, 'form': form, 'likes': likes, 'tags': tags}
    return render(request, 'main/news_detail.html', context)


def news_tag(request, tag):
    t = get_object_or_404(Tag, name=tag)
    news = t.news.all()
    context = {'news': news, 'tag': t}
    return render(request, 'main/news_tag.html', context)


def like_news(request, news_id):
    piece_news = get_object_or_404(News, id=news_id)
    if piece_news.likes(request.user):
        piece_news.like.remove(request.user)
    else:
        piece_news.like.add(request.user)
    return redirect("main_news_detail", news_id=news_id)


def like_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if match.likes(request.user):
        match.like.remove(request.user)
    else:
        match.like.add(request.user)
    return redirect('main_match_detail', match_id=match_id)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form,})

