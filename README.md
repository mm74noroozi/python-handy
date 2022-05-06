# python-handy
## Django dynamic url types
- str
- int
- slug
- uuid
- path
## Django mock data
Need some mock data to test your app? Mockaroo lets you generate up to 1,000 rows of realistic test data in CSV, JSON, SQL, and Excel formats.
with alot of!!! data types first name lastname ....
https://www.mockaroo.com/
## Django create bash profile
    python manage.py shell -i ipython
## Django queryset hacks
    >>> Article.objects.all().values("title")
    [{'title': 'Article 0'}, {'title': 'Article 1'}, {'title': 'Article 2'}]
    
    >>> Entry.objects.values_list('id').order_by('id')
    [(1,), (2,), (3,), ...]
    >>> Entry.objects.values_list('id', flat=True).order_by('id')
    [1, 2, 3, ...]
