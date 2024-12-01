from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews,
    })


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
    })