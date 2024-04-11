from django.contrib import admin
from .models import App01Book
from .models import App01Rent
from .models import App01HousePrice
from .models import App01UserInformation
from .models import App01Check
# Register your models here.

admin.site.register(App01Rent)
admin.site.register(App01UserInformation)
admin.site.register(App01Book)
admin.site.register(App01HousePrice)
admin.site.register(App01Check)
