import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name, genre', [['Игра престолов', 'Фантастика'], ['Робинзон Крузо', 'Мультфильмы']])
    def test_set_book_genre_set_genre_two_books_shows_genres_by_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_new_book_with_too_long_name_not_in_books_genres(self):
        collector = BooksCollector()
        name_42_symbols = 'энтерогематогепатогематопульмоэнтерального'
        collector.add_new_book(name_42_symbols)
        assert name_42_symbols not in collector.books_genre

    def test_get_book_genre_for_non_existing_book_shows_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre("NonExistingBook") is None

    def test_get_books_with_specific_genre_book_with_genre_shows_book_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Три мушкетера")
        collector.set_book_genre("Три мушкетера", "Мультфильмы")
        assert collector.get_books_with_specific_genre("Мультфильмы") == ["Три мушкетера"]

    def test_get_books_genre_add_book_with_genre_get_books_genre(self):
        expected_result = {"Тестовая книга": "Фантастика"}
        collector = BooksCollector()
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", "Фантастика")
        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_add_adult_book_no_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_existing_book_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        assert collector.get_list_of_favorites_books() == ["Властелин колец"]

    def test_delete_book_from_favorites_existing_book_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        collector.delete_book_from_favorites("Властелин колец")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_add_two_of_three_books_in_favorites_shows_two_added_books(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_new_book("Три мушкетера")
        collector.add_new_book("Игра престолов")
        collector.add_book_in_favorites("Властелин колец")
        collector.add_book_in_favorites("Игра престолов")
        assert collector.get_list_of_favorites_books() == ["Властелин колец", "Игра престолов"]
