import unittest
from app import db
from app.models import Comment, User, Blog

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_juliet = User(username = 'juliet', password = 'billions', email = 'juliet@ms.com')
        self.new_pitch = Blog(id = 1, pitch_title = 'Test', pitch_content = 'This is a test pitch', category = 'interview', user = self.user_juliet)
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_juliet, pitch_id = self.new_pitch)