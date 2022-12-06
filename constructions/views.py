from django.shortcuts import render, redirect
from . models import Construction, Tag, Earth, Concrete, Reinforcement, Others, MeasureUnit
from . forms import ConstructionForm, EarthForm, ConcreteForm, ReinforcementForm, OthersForm, AddMeasureUnitForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . utils import searchConstructions, searchEarth, searchConcrete, searchReinforcement, searchOthers, paginateConstructions, measureUnitName
from django.db.models import Sum, Q, Max


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

    earthSummary = Earth.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown').annotate(quantity=Sum('quantity')).order_by('custom_name')
    concreteSummary = Concrete.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown').annotate(quantity=Sum('quantity')).order_by('custom_name')
    reinforcementSummary = Reinforcement.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown').annotate(quantity=Sum('quantity')).order_by('custom_name')
    othersSummary = Others.objects.filter(Q(owner=constructionObj)).values('custom_name', 'measure_unit_dropdown').annotate(quantity=Sum('quantity')).order_by('custom_name')

    measureUnits = MeasureUnit.objects.all()

    context = {'construction':constructionObj,
    'earthSummary':earthSummary,
    'concreteSummary':concreteSummary, 
    'reinforcementSummary':reinforcementSummary,
    'othersSummary':othersSummary,
    'measureUnits':measureUnits,
    }

    measureUnitName(earthSummary)
    measureUnitName(concreteSummary)
    measureUnitName(reinforcementSummary)
    measureUnitName(othersSummary)
    
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