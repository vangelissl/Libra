from django.test import TestCase
from django.urls import reverse
from myapp.models import Book, Author
from datetime import date, datetime, timedelta


# Create your tests here.
class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class BookListViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Robert", last_name="Greene",
                                            birth_date=date(1959, 5, 14))
        self.book = Book.objects.create(title="23 laws of Lust", author=self.author,
                                        isbn='3423-2342-2344', pages=479)

    def test_book_list_view_status_code(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_context(self):
        response = self.client.get(reverse('book_list'))
        self.assertIn(self.book, response.context['books'])


class AuthorListTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Robert", last_name="Greene",
                                            birth_date=date(1959, 5, 14))

    def test_author_list_view_status_code(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)

    def test_author_list_view_context(self):
        response = self.client.get(reverse('author_list'))
        self.assertIn(self.author, response.context['authors'])