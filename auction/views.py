from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ProductUpdateForm, ProductCreateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Products

@login_required
def home(request):
    # current_time = datetime.datetime.now()
    current_time = datetime.datetime.now()
    print(current_time)
    live_products = Product.objects.filter(live_until__gte=current_time)
    for product in live_products:
        print(product.live_until)
    context = {
        'posts': live_products
    }
    return render(request, 'auction/home.html', context)

def about(request):
    return render(request, 'auction/about.html', {'title': 'About'})

class ItemListView(ListView):
    model = Products
    template_name = 'auction/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        current_time = timezone.now()
        
        # Create separate querysets for live and expired products
        live_products = Products.objects.filter(live_until__gte=current_time)
        expired_products = Products.objects.filter(live_until__lt=current_time)
        
        # Add live and expired products to the context
        context['live_products'] = live_products
        context['expired_products'] = expired_products
        
        return context


        
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductCreateForm  # Use the custom form
    template_name = 'auction/product_form.html'  # Replace with the actual template name

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Products

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Products
    form_class = ProductUpdateForm
    template_name = 'auction/product_bid.html'
    def form_valid(self, form):
        form.instance.highest_bidder = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user != post.seller:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.seller:
            return True
        return False