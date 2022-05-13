from django.contrib import admin
from .models import Algos, Square, SquareRoot, Factorial, Fibonacci, History

# Register your models here.
admin.site.register(Algos)
admin.site.register(Square)
admin.site.register(SquareRoot)
admin.site.register(Factorial)
admin.site.register(Fibonacci)
admin.site.register(History)
