from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import Book
from django.urls import reverse_lazy
from .forms import CreateBookForm
# Create your views here.
class BookCreateView(TemplateView):
    model=Book
    form_class=CreateBookForm
    template_name = "createbook.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

class BookList(TemplateView):
    model=Book
    template_name = "listbooks.html"
    context={}
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)

class BookUpdate(TemplateView):
    model=Book
    form_class=CreateBookForm
    template_name = "updatebook.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=self.get_object(id)
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        form=self.form_class(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

class BookDetailView(TemplateView):
    model=Book
    template_name = "bookdetail.html"
    context={}

    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        self.context["book"]=book
        return render(request,self.template_name,self.context)

class BookDeleteView(TemplateView):
    model=Book
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        book.delete()
        return redirect("list")

class DBookCreate(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = "createbook.html"
    success_url = "dlist"
class DBookList(ListView):
    model = Book
    template_name = "listbooks.html"
    context_object_name = "books"
    success_url="dlist"
class DBookUpdate(UpdateView):
    model=Book
    form_class = CreateBookForm
    template_name ="updatebook.html"
    context_object_name = "form"
    success_url = "dlist"
class DBookDetail(DetailView):
    model = Book
    template_name = "bookdetail.html"
    context_object_name = "book"

class DBookDelete(DeleteView):
    model = Book
    template_name = "delete.html"
    success_url = reverse_lazy("list")




