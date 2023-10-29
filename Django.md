# Django
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
```bash
python manage.py shell -i ipython
```
## Django queryset hacks
```python
>>> Article.objects.all().values("title")
[{'title': 'Article 0'}, {'title': 'Article 1'}, {'title': 'Article 2'}]
    
>>> Entry.objects.values_list('id').order_by('id')
[(1,), (2,), (3,), ...]
>>> Entry.objects.values_list('id', flat=True).order_by('id')
[1, 2, 3, ...]
```
### lookups
- exact , iexact (case insensitive)
- contains , icontains
- lt , lte , gt , gte
- startswith , istartswith , endswith , iendswith
- in
### aggregations
```python
>>> from django.db.models import Avg, Sum, Max, Min
>>> User.objects.aggregate(Avg('score'))
{'score__avg': 9.8}
>>> User.objects.aggregate(average_score=Avg('score'))
{'average_score': 9.8}
```
#### aggregation vs annotation
```python
>>> from django.db.models import FloatField
>>> Book.objects.aggregate(
...     price_diff=Max("price", output_field=FloatField()) - Avg("price")
... )
{'price_diff': 46.85}

# All the following queries involve traversing the Book<->Publisher
# foreign key relationship backwards.

# Each publisher, each with a count of books as a "num_books" attribute.
>>> from django.db.models import Count
>>> pubs = Publisher.objects.annotate(num_books=Count("book"))
>>> pubs
<QuerySet [<Publisher: BaloneyPress>, <Publisher: SalamiPress>, ...]>
>>> pubs[0].num_books
73
```
## Coalesce
return first not null value
```python
>>> from django.db.models.functions import Coalesce
>>> Author.objects.create(name="Margaret Smith", goes_by="Maggie")
>>> author = Author.objects.annotate(screen_name=Coalesce("alias", "goes_by", "name")).get()
>>> print(author.screen_name)
Maggie
```
### F objects [using for representing a column]
```python
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
```
### Q objects [using for logical operations in query]
```python
>>> conditions = Q(math_score__gte=10) | Q(physics_score__gte=10)
>>> Student.objects.filter(conditions)
<QuerySet [...]>
```
- & : and
- | : or
- ~ : not
#### equivalent queries
```python
>>> Student.objects.exclude(math_score__in=[10, 13])
<QuerySet [...]>
>>> Student.objects.filter(~Q(math_score=10) & ~Q(math_score=13))
<QuerySet [...]>
>>> Student.objects.exclude(math_score=10).exclude(math_score=13)
<QuerySet [...]>
```
## Django Manager
```python
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
```
## Django filter
```python
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
```
## Django templates
base template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Home{% endblock %}</title>
    <link rel="stylesheet" href="base.css">
</head>

<body>
    <div id="navigation">
        {% block navigation %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/">Contact</a></li>
            <li><a href="/">About us</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```
child template
```html
{% extends "base.html" %}

{% block title %}Book List{% endblock %}

{% block content %}
{% for book in book_list %}
    <h2>{{ book.title }}</h2>
    <h3>{{ book.author }}</h3>
{% endfor %}
{% endblock %}
```
## Django template filters
    {{ value|lower }}
    {{ value|length }} 
    {{ value|filesizeformat }} 235.3MB
    {{ value|truncatewords:2 }}  word1 word2 ...
    {{ value|default:"empty" }}
    {{ value|lower|truncatewords:2 }}
## Django Extend User + search manytomany field
- models.py
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    interests = models.ManyToManyField("user_data.Interest",blank=True)
```
- admin.py
```python
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    

@admin.register(User)
class UserAdminExtended(UserAdmin):
    autocomplete_fields = ['interests']
    fieldsets = (
        (None, {"fields": ("username", "password","interests")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
```
- settings.py
```python
AUTH_USER_MODEL = 'user_data.User'
```
## Unit testing
### upchecking
some_app/tests.py
```python
from django.test import TestCase

class UP_RUNNING(TestCase):
    def test_homepage(self):
        # url = reverse("whatever.views.whatever")
        res = self.client.get("/")
        self.assertEqual(res.status_code,200)
```
### CSRF in test?
```python
django doesn't enforce (by default) csrf checking with tests. to enforce csrftoken check:
```python
from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)
```
###
### SetUp and tearsDown
```python
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setUpSth(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownSth(cls):
        cls._connection.destroy()
```
## ModelForm
```python
from django import forms
from .models import User

class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email',)
```
## Generic Views
```python
from django.views.generic import DetailView


class BookDetailView(DetailView):
    queryset = Book.objects.filter(is_published=True)
```
## Custom Permission on model
```python
class Task(models.Model):
    ...

    class Meta:
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]
```
### Middlewares
- CommonMiddleware:  APPEND_SLASH , PREPEND_WWW
- SecurityMiddleware: HSTS , ... https://docs.djangoproject.com/en/3.1/ref/middleware/#module-django.middleware.security
- SessionMiddleware: https://docs.djangoproject.com/en/3.1/topics/http/sessions/
- CsrfViewMIddleware: handle csrftoken
## Django rest framework
### api_view
```python
@api_view(['POST'])
def create_product(request):
    product = Product.objects.create(name=request.data['name'], price=request.data['price'])
    return Response({
        "message": "new product added successfully",
        "product": {
            "name": product.name,
            "price": product.price
        }
    }, status=status.HTTP_201_CREATED)
```
### APIView
```python

class AddCarAPIView(APIView):
    def post(self, request):
        car_serializer = CarSerializer(data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({'message': 'Car added successfully!'})

        return Response({'message': car_serializer.errors})
```
### ModelSerializer
```python
from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'minimum_price', 'maximum_price', 'country')

    def validate(self, data):
        if data.get('minimum_price', 0) > data.get('maximum_price', 0):
            error = 'Maximum should be greater than minimum'
            raise serializers.ValidationError(error)

        return data

    def validate_minimum_price(self ,value):
        if value < 0 :
            raise serializers.ValidationError('Minimum price must be postive')

        return value
```
### GET Simple Token
```python
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Other urls
    path('login/', view=obtain_auth_token),
]
```
### GenericAPIView
```python
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


class HelloAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response(data={'message': f"Hello {request.user.username}!"})
```
### Permission class
- IsAdminUser
- IsAuthenticated
- IsAuthenticatedOrReadOnly: Authenticated or GET OPTIONS HEAD methods
- AllowAny
- DjangoModelPermissions
#### DjangoModelPermissions
```python
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
```
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ]
}
```
#### BasePermission
```python
from rest_framework.permissions import BasePermission

from security.models import Blacklist


class Blacklisted(BasePermission):

    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        in_blacklist = Blacklist.objects.filter(ip=ip_address).exists()

        return not in_blacklist
```
### tests
#### ViewSet Tests
```python
class ViewSetTest(TestCase):
    def test_view_set(self):
        factory = APIRequestFactory()
        view = CatViewSet.as_view(actions={'get': 'retrieve'}) # <-- Changed line
        cat = Cat(name="bob")
        cat.save()

        request = factory.get(reverse('cat-detail', args=(cat.pk,)))
        response = view(request)
```

