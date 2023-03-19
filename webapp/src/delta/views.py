from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.views import generic
from django.core.cache import cache
from .category_def import *
from .proucts_def import *
from .forms import *
from . import tasks


def index(request):
    context = {'title': 'Main page', 'description': 'Some Description'}
    return render(request, 'main/index.html', context)


def adm(request):
    visitors = Visitors.objects.all()
    total_visits = 0
    for vis in visitors:
        total_visits += vis.count
    count = visitors.count
    context = {'title': 'Admin Page', 'ip': get_client_ip(request), 'visitors': visitors, 'count': count, 'total_visits': total_visits}
    return render(request, 'main/adm.html', context)

@permission_required('delta.add_caregory')
def update_catalog(request):
    '''Обнавляем список категорий'''

    get_catalogs_wb_for_db()
    context = {'title': 'Category Update', 'description': "Обнавляем список категорий"}
    return render(request, 'main/index.html', context)

def update_products(request):
    '''Обнавляем список Products'''

    pr = Product.objects.all().only('category', 'categorys')
    for prod in pr:
        c = prod.category.split(', ')
        ls = []
        for cc in c:
            try:
                ls.append(int(cc[1:]))
            except:
                pass
        prod.category.add(*ls)
    context = {'title': 'Product Update', 'description': "Обнавляем список товаров"}
    return render(request, 'main/index.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ViewProducts(generic.ListView):
    model = Product
    paginate_by = PAGINATE
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Delta'
        context["form"] = SearchForm()
        if ("id" in self.kwargs) and (self.kwargs["id"] != 0):
            cat_id = self.kwargs["id"]
            base_category = Category.objects.get(id=cat_id)
            context["base_cat"] = base_category
            context["category"] = Category.objects.filter(parent_cat_id=cat_id).order_by('-total_views').only('id', 'name')

            if base_category.parent_cat:
                context["parent_cat"] = Category.objects.get(id=base_category.parent_cat_id).name

            context["title"] = base_category.name
        else:
            # Добавляем счетчик посетителей ###################################
            ip = get_client_ip(self.request)
            tasks.task_visit_counter.delay(ip=ip)
            # Сохраняем констнты ##############################################
            try:
                MIN_SALE = Constants.objects.first().sale  # размер минимальной скидки отображаемого товара на странице
                PAGINATE = Constants.objects.first().paginate  # количество товара на одной странице
                CAT_PAGES = Constants.objects.first().pages  # количество страниц поиска товаров на Wildberries
                CACHE_TIME = Constants.objects.first().cache_time  # время кэширования в секундах
            except Exception as ex:
                MIN_SALE = 15
                PAGINATE = 20
                CAT_PAGES = 4
                CACHE_TIME = 60
            ##################################################################
            context["category"] = cache.get_or_set('all_category',
                    Category.objects.filter(parent_cat=None).order_by('-total_views').only('id', 'name'), CACHE_TIME)
            # print(context)
        return context

    def get_queryset(self, **kwargs):
        if ("id" in self.kwargs) and (self.kwargs["id"] != 0):  # prefetch_related('category').
            cat_id = self.kwargs["id"]
            q_set = Product.objects.filter(category=cat_id, sale__gte=MIN_SALE).order_by('-sale').only('url', 'name',
                                                                                                'sale_price', 'sale')
            cat = Category.objects.get(id=cat_id)
            cat.counter()
            pora_obnovlyat = (datetime.now().timestamp() > (cat.updated_at + (60 * 60 * 24)))  # Раз в сутки
            if pora_obnovlyat:
                # Start Task ################
                tasks.task_get_product_for_db.delay(shard=cat.shard, query=cat.query, cat=self.kwargs["id"])
                #############################
        else:
            q_set = cache.get_or_set('q_set', Product.objects.filter(sale__gte=MIN_SALE).order_by('-sale').only('url',
                                                                            'name', 'sale_price', 'sale'), CACHE_TIME)
        return q_set


class ViewSearchProducts(generic.ListView):
    model = Product
    paginate_by = PAGINATE
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')  #.lower()

        if search:
            q_set = Product.objects.filter(name__icontains=search,
                sale__gte=MIN_SALE).order_by('-sale').only('url', 'name', 'sale_price', 'sale')
        else:
            q_set = cache.get_or_set('q_set',
                Product.objects.filter(sale__gte=MIN_SALE).order_by('-sale').only('url', 'name', 'sale_price', 'sale'),
                                                                                                            CACHE_TIME)
        return q_set

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = 'Delta'
        context["form"] = SearchForm(self.request.GET)
        context["category"] = cache.get_or_set('all_category',
                            Category.objects.filter(parent_cat=None).order_by('-total_views').only('id', 'name'), CACHE_TIME)
        return context










