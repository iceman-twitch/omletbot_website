from django.contrib import admin

# Register your models here.
# from .models import List
from .models import Bots
from .models import Count
from .models import Proxies
from .models import Queue
admin.site.register(Bots)
admin.site.register(Count)
admin.site.register(Proxies)
admin.site.register(Queue)