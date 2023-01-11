from rest_framework import serializers
from books.models import Books, Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comments
        fields = ('id', 'text')


class BookListingSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ('id', 'name', 'author_name', 'published_date', 'category', 'image', 'star_rate',)

        def get_category(self,instance):
            return instance.category.name




class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ('id', 'name', 'author_name', 'published_date', 'category', 'description', 'comments',  'star_rate',)

    def get_category(self,instance):
        return instance.category.name

    def get_comments(self,instance):
        comments = Comments.objects.filter(book_name=instance)
        serializer = CommentsSerializer(comments, many=True)

        return serializer.data



class DeleteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'is _deleted',)



class AddContentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id", 'book_name', 'text',)