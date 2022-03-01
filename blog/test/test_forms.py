from django.test import SimpleTestCase 
from blog.forms import CommentForm, NewsLetterForm, ContactForm, TagForm

class TestForm(SimpleTestCase):
    
    def test_comment_form_with_valid_data(self):
        form = CommentForm(data={
            'author': 'mark angel',
            'body': 'this is a nice comment'
        })
        
        self.assertEqual(form.is_valid(),True)
        self.assertEqual(len(form.errors),0)
        
    def test_comment_form_with_empty_data(self):
        form = CommentForm(data={
            'author': '',
            'body': ''
        })
        
        self.assertEqual(form.is_valid(),False)
        self.assertEqual(len(form.errors),2)
        
    def test_newsletter_form_with_valid_email(self):
        form = NewsLetterForm(data={
            'email':'niceuser@correctuser.com'
        })
        
        self.assertEqual(form.is_valid(),True)
        self.assertEqual(len(form.errors),0)
        
    def test_newsletter_form_with_invalid_email(self):
        form = NewsLetterForm(data={
            'email':'niceuser@correctuser'
        })
        
        self.assertEqual(form.is_valid(),False)
        self.assertEqual(len(form.errors),1)
        
    def test_tag_form(self):
        form = TagForm(data={
           'name': 'this'
        })
        
        self.assertEqual(form.is_valid(),True)
        self.assertEqual(len(form.errors),0)