import json

from mongoengine import errors

from models import Author, Quote

if __name__ == '__main__':
    with open('authors.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except errors.NotUniqueError:
                print(f"Author exists {el.get('fullname')}")

    with open('quotes.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            author = Author.objects(fullname=el.get('author')).first()
            if author:
                quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
                quote.save()
            else:
                print(f"Author not found: {el.get('author')}")
