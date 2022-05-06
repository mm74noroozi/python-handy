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
### F objects [using for representing a column]
    from django.db import models

    class Student(models.Model):
        name = models.CharField(max_length=10)
        math_score = models.IntegerField()
        physics_score = models.IntegerField()
    
    >>> from django.db.models import F
    >>> physics_score = F('physics_score')
    >>> Student.objects.filter(math_score__gt=physics_score)
    <QuerySet [...]>
    >>> Student.objects.filter(math_score__gt=F('physics_score')*2)
    <QuerySet [...]>
### Q objects [using for logical operations in query]
    >>> conditions = Q(math_score__gte=10) | Q(physics_score__gte=10)
    >>> Student.objects.filter(conditions)
    <QuerySet [...]>
- & : and
- | : or
- ~ : not
#### equivalent queries
    >>> Student.objects.exclude(math_score__in=[10, 13])
    <QuerySet [...]>
    >>> Student.objects.filter(~Q(math_score=10) & ~Q(math_score=13))
    <QuerySet [...]>
    >>> Student.objects.exclude(math_score=10).exclude(math_score=13)
    <QuerySet [...]>
## Django Manager
    class Mobile(models.Model):
        price = models.PositiveIntegerField(default=1000)
        mobiles = models.Manager()

    >>> Mobile.mobiles.all()
    <QuerySet [<Mobile: some_mobile>, ...]>

    >>> Mobile.objects.all()
    ...
    AttributeError: type object 'Mobile' has no attribute 'objects'
    
    
    class MobileManager(models.Manager):
    def most_popular_mobiles(self):
        return self.filter(
            condition1=..., 
            condition2=..., 
            condition3=..., 
            condition4=..., 
            condition5=..., 
            ...
        )

    class Mobile(models.Model):
        price = models.PositiveIntegerField(default=1000)
        objects = MobileManager()
## Django filter
    # views.py
    from django.http import HttpResponse
    from .models import Book

    def index(request):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        books = Book.objects.filter(
            price__gte=min_price, price__lte=max_price
        ).values_list('name', flat=True)
        return HttpResponse('\n'.join(map(str, books)))


