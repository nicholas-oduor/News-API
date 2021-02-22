from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_article,get_category
# from .forms import ReviewForm


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting news sources
    popularity = get_news('popularity')
    bitcoin = get_news('bitcoin')
    business = get_news('business')
    techcrunch = get_news('techcrunch')
    wall_street = get_news('wsj')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', category_name = search_news))
    else:
        return render_template('index.html', title = title, popularity = popularity, bitcoin = bitcoin, business = business, techcrunch = techcrunch, wall_street = wall_street )

@main.route('/article/')
def article():

    '''
    View article page function that returns the news articles details page and its data
    '''
    news = get_article(article)
    title = f'{news.title}'
    article = Article.get_article(news.url)

    return render_template('article.html',title = title,news = news,article = article)

@main.route('/categories/<category_name>')
def category(category_name):
    '''
    method that returns the categories page
    '''
    category = get_category(category_name)
    title = f'{category_name}'
    
    return render_template('categories.html', title = title, category = category)

@main.route('/categories/technology')
def technology():
    '''
    method that returns the categories page
    '''
    technology = get_category('technology')
    title = 'TECHNOLOGY'
    
    return render_template('categories.html', title = title, technology = technology)

@main.route('/categories/sport')
def sports():
    '''
    method that returns the categories page
    '''
    sports = get_category('sports')
    title = 'SPORTS'
    
    return render_template('categories.html', title = title, sports = sports)

@main.route('/categories/entertainment')
def entertainment():
    '''
    method that returns the categories page
    '''
    sports = get_category('entertainment')
    title = 'ENTERTAINMENT'
    
    return render_template('categories.html', title = title, entertainment = entertainment)

@main.route('/categories/business')
def business():
    '''
    method that returns the categories page
    '''
    business = get_category('business')
    title = 'BUSINESS'
    
    return render_template('categories.html', title = title, business = business)


@main.route('/search/<category_name>')
def search(category_name):
    '''
    View function to display the search results
    '''
    category_list = category.split(" ")
    category_format = "+".join(category_list)
    searched_news = search_movie(category_format)
    title = f'search results for {category_name}'
    return render_template('search.html',news = searched_news)