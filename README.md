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
### lookups
- exact , iexact (case insensitive)
- contains , icontains
- lt , lte , gt , gte
- startswith , istartswith , endswith , iendswith
- in
### aggregations
    >>> from django.db.models import Avg, Sum, Max, Min
    >>> User.objects.aggregate(Avg('score'))
    {'score__avg': 9.8}
    >>> User.objects.aggregate(average_score=Avg('score'))
    {'average_score': 9.8}
### F objects and Q objects
    from django.db import models

    class Student(models.Model):
        name = models.CharField(max_length=10)
        math_score = models.IntegerField()
        physics_score = models.IntegerField()
    
    >>> from django.db.models import F
    >>> Student.objects.filter(math_score__gt=F('physics_score')) # or 
    #>>> physics_score = F('physics_score')
    #>>> Student.objects.filter(math_score__gt=physics_score)
    <QuerySet [...]>
