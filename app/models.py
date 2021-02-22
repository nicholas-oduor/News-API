class Article:

    all_articles = []

    def __init__(self,title,image,description,date,article):
        self.title = title
        self.image = image
        self.description = description
        self.date = date
        self.article = article

    def save_article(self):
        Article.all_articles.append(self)