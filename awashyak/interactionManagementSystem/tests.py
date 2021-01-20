from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostSlugTest(TestCase):
    
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        Post.objects.create(title='Hello World',body='Nice body content',user=self.user)
        Post.objects.create(title='Hello World',body='Nice body content',user=self.user)


    def test_check_slugs(self):
        objectOne = Post.objects.get(pk=1)
        objectTwo = Post.objects.get(pk=2)

        self.assertEqual(objectOne.slug, 'hello-world')
        self.assertEqual(objectTwo.slug, 'hello-world-2')
        



class ForumTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(title='A good title',body='Nice body content',user=self.user,)


    def test_string_representation(self):
        post = Post(title='A sample tile')
        self.assertEqual(str(post),post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.user}','testuser')
        self.assertEqual(f'{self.post.body}','Nice body content')

    def test_post_create_view(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.user}','testuser')
        self.assertEqual(f'{self.post.body}','Nice body content')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit',args='1'),{
            'title':'Update title',
            'body': 'Update text',
        })
        self.assertEqual(response.status_code,403)


    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code,403)