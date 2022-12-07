from . models import Construction, Tag, Earth, Concrete, Reinforcement, Others, MeasureUnit
from django.db.models import Q
from  django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchConstructions(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    constructions = Construction.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) | 
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return constructions, search_query

def searchEarth(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    quantities = Earth.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(custom_name__icontains=search_query) |       
        Q(quantity__icontains=search_query) |       
        Q(measure_unit_dropdown__name=search_query) |       
        Q(created__icontains=search_query) |      
        Q(date__icontains=search_query)      
    )

    return quantities

def searchConcrete(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    quantities = Concrete.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(custom_name__icontains=search_query) |       
        Q(quantity__icontains=search_query) |       
        Q(measure_unit_dropdown__name=search_query) |       
        Q(created__icontains=search_query) |      
        Q(date__icontains=search_query)      
    )

    return quantities

def searchReinforcement(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    quantities = Reinforcement.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(custom_name__icontains=search_query) |       
        Q(quantity__icontains=search_query) |       
        Q(measure_unit_dropdown__name=search_query) |       
        Q(created__icontains=search_query) |      
        Q(date__icontains=search_query)            
    )

    return quantities

def searchOthers(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    quantities = Others.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(custom_name__icontains=search_query) |       
        Q(quantity__icontains=search_query) |       
        Q(measure_unit_dropdown__name=search_query) |       
        Q(created__icontains=search_query) |      
        Q(date__icontains=search_query)            
    )

    return quantities

def paginateConstructions(request, constructions, results):
    page = request.GET.get('page')

    paginator = Paginator(constructions, results)

    try:
        constructions = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        constructions = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        constructions = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, constructions

def measureUnitName(queryset):
    for query in queryset:
        unit = MeasureUnit.objects.get(pk=query['measure_unit_dropdown'])
        query['measure_unit_dropdown'] = unit

