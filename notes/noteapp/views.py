from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Author, Quote


def main(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "noteapp/index.html", context={"title": "Deep quote", "quotes": quotes, "page_obj": page_obj})


class AddTagView(View):
    form_class = TagForm
    template_name = "noteapp/tag.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.user = request.user
            new_tag.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})


class AddAuthorView(View):
    form_class = AuthorForm
    template_name = "noteapp/add_author.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.user = request.user
            new_author.save()
            return redirect(to="noteapp:main")
        else:
            return render(request, "noteapp/add_author.html", {"form": form})


class AddQuoteView(View):
    form_class = QuoteForm
    template_name = "noteapp/add_quote.html"

    tags = Tag.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"tags": self.tags, "form": self.form_class()})

    def post(self, request, *args, **kwargs):
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))

            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to="noteapp:main")
        else:
            return render(request, "noteapp/add_quote.html", {"form": form})


class QuoteView(View):
    template_name = "noteapp/quote.html"

    def get(self, request, quote_id):
        quote = get_object_or_404(Quote, pk=quote_id)
        return render(request, self.template_name, {"quote": quote})


class AuthorView(View):
    template_name = "noteapp/author.html"

    def get(self, request, full_name):
        author = get_object_or_404(Author, full_name=full_name)
        return render(request, self.template_name, {"author": author})

