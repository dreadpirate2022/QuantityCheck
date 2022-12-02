from django.urls import path
from . import views

app_name = 'constructions'

urlpatterns = [
    path('', views.constructions, name='constructions'),
    path('construction/<str:pk>', views.construction, name='construction'),
    path('create-construction/', views.createConstruction, name='create-construction'),
    path('update-construction/<str:pk>', views.updateConstruction, name='update-construction'),
    path('delete-construction/<str:pk>', views.deleteConstruction, name='delete-construction'),

    path('earth-positions/<str:pk>', views.earthPositions, name='earth-positions'),
    path('concrete-positions/<str:pk>', views.concretePositions, name='concrete-positions'),
    path('reinforcement-positions/<str:pk>', views.reinforcementPositions, name='reinforcement-positions'),
    path('others-positions/<str:pk>', views.othersPositions, name='others-positions'),

    path('add-earth-quantity/<str:pk>', views.addEarthQuantity, name='add-earth-quantity'),
    path('update-earth-quantity/<str:pk>', views.updateEarthQuantity, name='update-earth-quantity'),
    path('delete-earth-quantity/<str:pk>', views.deleteEarthQuantity, name='delete-earth-quantity'),

    path('add-concrete-quantity/<str:pk>', views.addConcreteQuantity, name='add-concrete-quantity'),
    path('update-concrete-quantity/<str:pk>', views.updateConcreteQuantity, name='update-concrete-quantity'),
    path('delete-concrete-quantity/<str:pk>', views.deleteConcreteQuantity, name='delete-concrete-quantity'),

    path('add-reinforcement-quantity/<str:pk>', views.addReinforcementQuantity, name='add-reinforcement-quantity'),
    path('update-reinforcement-quantity/<str:pk>', views.updateReinforcementQuantity, name='update-reinforcement-quantity'),
    path('delete-reinforcement-quantity/<str:pk>', views.deleteReinforcementQuantity, name='delete-reinforcement-quantity'),

    path('add-others-quantity/<str:pk>', views.addOthersQuantity, name='add-others-quantity'),
    path('update-others-quantity/<str:pk>', views.updateOthersQuantity, name='update-others-quantity'),
    path('delete-others-quantity/<str:pk>', views.deleteOthersQuantity, name='delete-others-quantity'),

    path('add-measure-unit/', views.addMeasureUnit, name='add-measure-unit'),
    path('remove-measure-unit/', views.removeMeasureUnit, name='remove-measure-unit'),
]
