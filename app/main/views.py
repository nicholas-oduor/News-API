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