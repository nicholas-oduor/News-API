import unittest
from app.models import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_article = Article("title","https://image.tmdb.org/t/ptfukyy","article",'2021','news')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Article.all_articles = []

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.title,'title')
        self.assertEquals(self.new_article.image,"https://image.tmdb.org/t/ptfukyy")
        self.assertEquals(self.new_article.description,'article')
        self.assertEquals(self.new_article.date,'2020')
        self.assertEquals(self.new_article.article,'news')


    def test_save_article(self):
        '''
        test_save_article test case to test if the article object is saved into
         the article list
        '''
        self.new_article.save_article() # saving the new article
        self.assertEqual(len(Article.all_articles),1)