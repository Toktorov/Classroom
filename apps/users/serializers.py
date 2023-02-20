from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'last_login', 'username',
                'first_name', 'last_name', 'email',
                'date_joined', 'profile_image')
        
class UserDetailSerializer(serializers.ModelSerializer):
    # #posts - посты пользователя
    # users_post = PostSerializer(read_only=True, many=True)
    # count_posts = serializers.SerializerMethodField(read_only=True)
    # #favorites - избранные пользователя
    # favorites = PostFavoritesSerializer(read_only=True, many=True)
    # count_favorites = serializers.SerializerMethodField(read_only=True)
    # #work_experience - опыт работы
    # users_work_experience = WorkExperienceSerializer(read_only=True, many=True)
    # #education - образование
    # users_education = EducationSerializer(read_only=True, many=True)
    # #skills - навыки
    # users_skill = SkillsSerializer(read_only=True, many=True)

    class Meta:
        model = User 
        fields = ('id', 'last_login', 'username',
                'first_name', 'last_name', 'email',
                'date_joined', 'profile_image')

    # def get_count_posts(self, instance):
    #     return instance.users_post.all().count()

    # def get_count_favorites(self, instance):
    #     return instance.favorites.all().count()

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, write_only=True
    )
    email = serializers.CharField(
        max_length=255, write_only=True
    )
    phone_number = serializers.CharField(
        max_length=255, write_only=True
    )
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            user_or_organization=validated_data['user_or_organization']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(
        max_length=255, required=True
    )
    new_password = serializers.CharField(
        max_length=255, required=True
    )