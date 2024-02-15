from django.shortcuts import render, redirect
from .models import Car, Brand, Comment
from .forms import CommentForm
from django.views.generic import DetailView



def home(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()  # Retrieve all Brand objects

    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        cars = cars.filter(brand=brand)

    return render(request, 'home.html', {'data': cars, 'brands': brands})


class DetailCarView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def car(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context