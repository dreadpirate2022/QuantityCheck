from rest_framework import serializers
from constructions.models import Construction, Tag, Earth, Concrete, Reinforcement, Others
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class EarthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earth
        fields = '__all__'

class ConcreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concrete
        fields = '__all__'

class ReinforcementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reinforcement
        fields = '__all__'

class OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others
        fields = '__all__'

class ConstructionSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    earth = serializers.SerializerMethodField()
    concrete = serializers.SerializerMethodField()
    reinforcement = serializers.SerializerMethodField()
    others = serializers.SerializerMethodField()

    class Meta:
        model = Construction
        fields = '__all__'

    def get_earth(self, obj):
        earth = obj.earth_set.all()
        searlizer = EarthSerializer(earth, many=True)
        return searlizer.data

    def get_concrete(self, obj):
        concrete = obj.concrete_set.all()
        searlizer = ConcreteSerializer(concrete, many=True)
        return searlizer.data

    def get_reinforcement(self, obj):
        reinforcement = obj.reinforcement_set.all()
        searlizer = ReinforcementSerializer(reinforcement, many=True)
        return searlizer.data

    def get_others(self, obj):
        others = obj.others_set.all()
        searlizer = OthersSerializer(others, many=True)
        return searlizer.data