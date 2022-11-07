from rest_framework import serializers
from .models import Book,BookNumber,Character,Author

#one to one relation
class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id','isbn_10','isbn_13']
        
#one to many relation
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id','name']
        
#many to many relation
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','surname']

#main serialization
class BookSerializer(serializers.ModelSerializer):     
    number = BookNumberSerializer(many=False) #one to one
    characters = CharacterSerializer(many=True) #one to many
    authors = AuthorSerializer(many=True) #many to many
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'price','published', 'is_published', 'number', 'characters','authors']

#mini book serializer
class BookMiniSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Book
        fields = ['id','title']

