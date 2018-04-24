from django.contrib import admin
from .models import Cargos
from .models import Propietario
from .models import Pagos
from .models import PagosPropietario
from .models import Gastos
from .models import EntregasDinero
from .models import DevolucionesDinero
admin.site.register(Cargos)
admin.site.register(Propietario)
admin.site.register(Pagos)
admin.site.register(PagosPropietario)
admin.site.register(Gastos)
admin.site.register(EntregasDinero)
admin.site.register(DevolucionesDinero)