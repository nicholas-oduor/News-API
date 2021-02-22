class Source:
    
    '''
    News class to define News Source Objects
    '''
    all_source = []

    def __init__(self,title,image,description,date,article):
        self.title = title
        self.image = image
        self.description = description
        self.date = date
        self.article = article

    def save_source(self):
        Source.all_source.append(self)

    @classmethod
    def clear_source(cls):
        Source.sources.clear()

    @classmethod
    def get_source(cls,title):

        response = []

        for source in cls.all_source:
            if source.title == title:
                response.append(source)

        return response
        

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
    
    @classmethod
    def clear_articles(cls):
        article.all_articles.clear()
    
    @classmethod
    def get_articles(cls,title):

        response = []

        for article in cls.all_articles:
            if article.title == title:
                response.append(article)

        return response


