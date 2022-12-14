from django.shortcuts import render, redirect
from . models import Construction, Tag, Earth, Concrete, Reinforcement, Others, MeasureUnit
from . forms import ConstructionForm, EarthForm, ConcreteForm, ReinforcementForm, OthersForm, AddMeasureUnitForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . utils import searchConstructions, searchEarth, searchConcrete, searchReinforcement, searchOthers, paginateConstructions
from django.db.models import Sum, Q, Max
from django.http import HttpResponse
from datetime import datetime
import xlwt



# Constructions
def constructions(request):
    constructions, search_query = searchConstructions(request)   
    custom_range, constructions = paginateConstructions(request, constructions, 6)

    context = {'constructions': constructions, 'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'constructions/constructions.html', context)

def construction(request, pk):
    constructionObj = Construction.objects.get(id=pk)
   
    context = {
        'construction':constructionObj,
    }
    
    return render(request, 'constructions/single-construction.html', context)

@login_required(login_url='users:login')
def createConstruction(request):
    profile = request.user.profile
    form = ConstructionForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()

        form = ConstructionForm(request.POST, request.FILES)
        if form.is_valid():
            construction = form.save(commit=False)
            construction.owner = profile
            construction.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                construction.tags.add(tag)
                
            messages.success(request, 'Construction was added')
            return redirect('constructions:constructions')

    context = {
        'form':form,
    }
    return render(request, 'constructions/construction_form.html', context)

@login_required(login_url='users:login')
def updateConstruction(request, pk):
    profile = request.user.profile
    construction = profile.construction_set.get(id=pk)
    form = ConstructionForm(instance=construction)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
       
        form = ConstructionForm(request.POST, request.FILES, instance=construction)
        if form.is_valid():
            construction = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                construction.tags.add(tag)

            messages.success(request, 'Construction was updated')
            return redirect('users:account')

    context = {
        'form':form,
        'construction':construction,
    }
    return render(request, 'constructions/construction_form.html', context)

@login_required(login_url='users:login')
def deleteConstruction(request, pk):
    profile = request.user.profile
    construction = profile.construction_set.get(id=pk)
    if request.method == 'POST':
        construction.delete()
        messages.success(request, 'Construction was deleted')
        return redirect('constructions:constructions')
    context = {
        'object':construction,
    }
    return render(request, 'constructions/delete_template.html', context)

# Positions
def earthPositions(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    quantities = searchEarth(request)

    context = {'construction':constructionObj, 'quantities':quantities}
    return render(request, 'constructions/earth_positions.html', context)

def concretePositions(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    quantities = searchConcrete(request)

    context = {'construction':constructionObj, 'quantities':quantities}
    return render(request, 'constructions/concrete_positions.html', context)

def reinforcementPositions(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    quantities = searchReinforcement(request)

    context = {'construction':constructionObj, 'quantities':quantities}
    return render(request, 'constructions/reinforcement_positions.html', context)

def othersPositions(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    quantities = searchOthers(request)

    context = {'construction':constructionObj, 'quantities':quantities}
    return render(request, 'constructions/others_positions.html', context)

def summaryPositions(request, pk):
    constructionObj = Construction.objects.get(id=pk)

    earthSummary = Earth.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown__name').annotate(quantity=Sum('quantity')).order_by('custom_name')
    concreteSummary = Concrete.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown__name').annotate(quantity=Sum('quantity')).order_by('custom_name')
    reinforcementSummary = Reinforcement.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown__name').annotate(quantity=Sum('quantity')).order_by('custom_name')
    othersSummary = Others.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown__name').annotate(quantity=Sum('quantity')).order_by('custom_name')

    context = {'construction':constructionObj,
    'earthSummary':earthSummary,
    'concreteSummary':concreteSummary, 
    'reinforcementSummary':reinforcementSummary,
    'othersSummary':othersSummary,
    }

    return render(request, 'constructions/summary_positions.html', context)

# Earth operations
@login_required(login_url='users:login')
def addEarthQuantity(request, pk):
    constructionObj = Construction.objects.get(id=pk)    
    form = EarthForm()
       
    if request.method == 'POST':
        form = EarthForm(request.POST)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.owner = constructionObj
            quantity.save()

            messages.success(request, 'Quantity was added')
            pre_url = '/earth-positions/{id}'.format(id=pk)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')
def updateEarthQuantity(request, pk):
    quantity = Earth.objects.get(id=pk)    
    constructionObj = quantity.owner

    form = EarthForm(instance=quantity)

    if request.method == 'POST':
        form = EarthForm(request.POST, instance=quantity)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.save()
            messages.success(request, 'Quantity was updated')            
            pre_url = '/earth-positions/{id}'.format(id=quantity.owner.id)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')

def deleteEarthQuantity(request, pk):
    quantity = Earth.objects.get(id=pk)

    if request.method == 'POST':
        quantity.delete()
        messages.success(request, 'Quantity was deleted')
        pre_url = '/earth-positions/{id}'.format(id=quantity.owner.id)
        return redirect(pre_url)

    context = {
        'object':quantity,
    }
    
    return render(request, 'constructions/delete_template.html', context)

# Concrete operations
@login_required(login_url='users:login')
def addConcreteQuantity(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    form = ConcreteForm()

    if request.method == 'POST':
        form = ConcreteForm(request.POST)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.owner = constructionObj
            quantity.save()
            messages.success(request, 'Quantity was added')
            pre_url = '/concrete-positions/{id}'.format(id=pk)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')
def updateConcreteQuantity(request, pk):
    quantity = Concrete.objects.get(id=pk)    
    constructionObj = quantity.owner

    form = ConcreteForm(instance=quantity)

    if request.method == 'POST':
        form = ConcreteForm(request.POST, instance=quantity)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.save()
            messages.success(request, 'Quantity was updated')            
            pre_url = '/concrete-positions/{id}'.format(id=quantity.owner.id)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')

def deleteConcreteQuantity(request, pk):
    quantity = Concrete.objects.get(id=pk)

    if request.method == 'POST':
        quantity.delete()
        messages.success(request, 'Quantity was deleted')
        pre_url = '/concrete-positions/{id}'.format(id=quantity.owner.id)
        return redirect(pre_url)

    context = {
        'object':quantity,
    }
    
    return render(request, 'constructions/delete_template.html', context)

# Reinforcement operations
@login_required(login_url='users:login')
def addReinforcementQuantity(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    form = ReinforcementForm()

    if request.method == 'POST':
        form = ReinforcementForm(request.POST)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.owner = constructionObj
            quantity.save()
            messages.success(request, 'Quantity was added')
            pre_url = '/reinforcement-positions/{id}'.format(id=pk)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')
def updateReinforcementQuantity(request, pk):
    quantity = Reinforcement.objects.get(id=pk)    
    constructionObj = quantity.owner

    form = ReinforcementForm(instance=quantity)

    if request.method == 'POST':
        form = ReinforcementForm(request.POST, instance=quantity)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.save()
            messages.success(request, 'Quantity was updated')            
            pre_url = '/reinforcement-positions/{id}'.format(id=quantity.owner.id)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')

def deleteReinforcementQuantity(request, pk):
    quantity = Reinforcement.objects.get(id=pk)

    if request.method == 'POST':
        quantity.delete()
        messages.success(request, 'Quantity was deleted')
        pre_url = '/reinforcement-positions/{id}'.format(id=quantity.owner.id)
        return redirect(pre_url)

    context = {
        'object':quantity,
    }
    
    return render(request, 'constructions/delete_template.html', context)

# Others operations
@login_required(login_url='users:login')
def addOthersQuantity(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    form = OthersForm()

    if request.method == 'POST':
        form = OthersForm(request.POST)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.owner = constructionObj
            quantity.save()
            messages.success(request, 'Quantity was added')
            pre_url = '/others-positions/{id}'.format(id=pk)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')
def updateOthersQuantity(request, pk):
    quantity = Others.objects.get(id=pk)    
    constructionObj = quantity.owner

    form = OthersForm(instance=quantity)

    if request.method == 'POST':
        form = OthersForm(request.POST, instance=quantity)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity.save()
            messages.success(request, 'Quantity was updated')            
            pre_url = '/others-positions/{id}'.format(id=quantity.owner.id)
            return redirect(pre_url)

    context = {'form':form, 'construction':constructionObj}
    return render(request, 'constructions/add_quantity.html', context)

@login_required(login_url='users:login')

def deleteOthersQuantity(request, pk):
    quantity = Others.objects.get(id=pk)

    if request.method == 'POST':
        quantity.delete()
        messages.success(request, 'Quantity was deleted')
        pre_url = '/others-positions/{id}'.format(id=quantity.owner.id)
        return redirect(pre_url)

    context = {
        'object':quantity,
    }
    
    return render(request, 'constructions/delete_template.html', context)

def addMeasureUnit(request):
    form = AddMeasureUnitForm()

    if request.method == 'POST':
        form = AddMeasureUnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.owner = request.POST['name']
            unit.save()
            messages.success(request, 'Measure unit was added')
            return redirect('users:account')

    context = {'form':form,}  
    return render(request, 'constructions/add_measure_unit.html', context)

def removeMeasureUnit(request):
    measureUnits = MeasureUnit.objects.all()

    if request.method == 'POST':
        unit = MeasureUnit.objects.get(name=request.POST['units'])
        unit.delete()
        messages.success(request, 'Measure unit was deleted')
        
        return redirect('users:account')

    context = {'units':measureUnits}  
    return render(request, 'constructions/remove_measure_unit.html', context)

def exportExcel(request, pk):
    constructionObj = Construction.objects.get(id=pk)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={Construction}'.format(Construction=constructionObj) + '-' + \
        str(datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Quantities')
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write_merge(0, 0, 0, 5, "{Construction}".format(Construction=constructionObj), font_style)

    columns = ['Created', 'Date', 'Name', 'Custom Name', 'Quantity', 'Measure Unit'] 

    for col_num in range(len(columns)):
        ws.write(row_num - 1, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows_earth = Earth.objects.filter(Q(owner=constructionObj)).values_list('created', 'date', 'name', 'custom_name', 'quantity', 'measure_unit_dropdown__name')
    rows_concrete = Concrete.objects.filter(Q(owner=constructionObj)).values_list('created', 'date', 'name', 'custom_name', 'quantity', 'measure_unit_dropdown__name')
    rows_reinforcement = Reinforcement.objects.filter(Q(owner=constructionObj)).values_list('created', 'date', 'name', 'custom_name', 'quantity', 'measure_unit_dropdown__name')
    rows_others = Others.objects.filter(Q(owner=constructionObj)).values_list('created', 'date', 'name', 'custom_name', 'quantity', 'measure_unit_dropdown__name')
    
    ws.write_merge(row_num, row_num, 0, 5, "Earth Quantities")
    for row in rows_earth:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                ws.write(row_num, col_num, (row[col_num]).strftime("%d-%m-%Y %H:%M:%S"), font_style)
            else:    
                ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 1
    ws.write_merge(row_num, row_num, 0, 5, "Concrete Quantities")

    for row in rows_concrete:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                ws.write(row_num, col_num, (row[col_num]).strftime("%d-%m-%Y %H:%M:%S"), font_style)
            else:    
                ws.write(row_num, col_num, str(row[col_num]), font_style)   

    row_num += 1
    ws.write_merge(row_num, row_num, 0, 5, "Reinforcement Quantities")

    for row in rows_reinforcement:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                ws.write(row_num, col_num, (row[col_num]).strftime("%d-%m-%Y %H:%M:%S"), font_style)
            else:    
                ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 1
    ws.write_merge(row_num, row_num, 0, 5, "Others Quantities")

    for row in rows_others:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                ws.write(row_num, col_num, (row[col_num]).strftime("%d-%m-%Y %H:%M:%S"), font_style)
            else:    
                ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response