from django.urls import path
from .views import ViewProducts, ViewSearchProducts, update_catalog, adm, index

urlpatterns = [
    path('', ViewProducts.as_view(), name='index'),
    path('adm', adm, name='adm'),
    path('category/<int:id>', ViewProducts.as_view(), name='sab_category'),
    path('search_prod', ViewSearchProducts.as_view(), {'search': 'search'}, name='search_prod'),
    path('update_catalog/', update_catalog, name='update_catalog'),
]
