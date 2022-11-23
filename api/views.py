from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ConstructionSerializer
from constructions.models import Construction, Earth, Concrete, Reinforcement, Others, Tag

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api/constructions'},
        {'GET':'/api/constructions/id'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes) 

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getConstructions(request):
    constructions = Construction.objects.all()
    serializer = ConstructionSerializer(constructions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getConstruction(request, pk):
    construction = Construction.objects.get(id=pk)
    serializer = ConstructionSerializer(construction, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEarth(request, pk):
    construction = Construction.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    earth = Earth.objects.create(
        owner=construction,
    )

    earth.name = data['name']
    earth.custom_name = data['custom_name']
    earth.quantity = data['quantity']
    earth.measure_unit = data['measure_unit']
    earth.save()

    serializer = ConstructionSerializer(construction, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addConcrete(request, pk):
    construction = Construction.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    concrete = Concrete.objects.create(
        owner=construction,
    )

    concrete.name = data['name']
    concrete.custom_name = data['custom_name']
    concrete.quantity = data['quantity']
    concrete.measure_unit = data['measure_unit']
    concrete.save()

    serializer = ConstructionSerializer(construction, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addReinforcement(request, pk):
    construction = Construction.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    reinforcement = Reinforcement.objects.create(
        owner=construction,
    )

    reinforcement.name = data['name']
    reinforcement.custom_name = data['custom_name']
    reinforcement.quantity = data['quantity']
    reinforcement.measure_unit = data['measure_unit']
    reinforcement.save()

    serializer = ConstructionSerializer(construction, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOthers(request, pk):
    construction = Construction.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    others = Others.objects.create(
        owner=construction,
    )

    others.name = data['name']
    others.custom_name = data['custom_name']
    others.quantity = data['quantity']
    others.measure_unit = data['measure_unit']
    others.save()

    serializer = ConstructionSerializer(construction, many=False)
    return Response(serializer.data)

# Remove tag (not delete)
@api_view(['DELETE'])
def removeTag(request):
    tagID = request.data['tag']
    constructionId = request.data['construction']

    construction = Construction.objects.get(id=constructionId)
    tag = Tag.objects.get(id=tagID)

    construction.tags.remove(tag)
    return Response('Tag was deleted!')