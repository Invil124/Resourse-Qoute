from django.forms import ModelForm, CharField, TextInput, DateTimeField, Textarea, DateTimeInput, ModelChoiceField
from .models import Tag, Author, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']
        exclude = ["user"]


class AuthorForm(ModelForm):
    full_name = CharField(max_length=100, required=True, widget=TextInput())
    born_date = DateTimeField(required=True, widget=DateTimeInput())
    born_location = CharField(max_length=100, required=True, widget=TextInput())
    description = CharField(max_length=2000, required=True, widget=Textarea())

    class Meta:
        model = Author
        fields = ["full_name", "born_date", "born_location", "description"]
        exclude = ["user"]


class QuoteForm(ModelForm):
    quote = CharField(max_length=280, min_length=10, widget=Textarea())
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ["quote", "author"]
        exclude = ["tags", "user"]

