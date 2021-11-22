from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import VPost


class VPostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )
        test_user.save()

        test_post = VPost.objects.create(
            author=test_user, title="Title of Blog",v_url="test URL", body="Words about the blog"
        )
        test_post.save()
    
    def test_blog_content(self):
        post = VPost.objects.get(id=1)
        
        self.assertEqual(str(post.author), "tester")
        self.assertEqual(post.title, "Title of Blog")
        self.assertEqual(post.body, "Words about the blog")



