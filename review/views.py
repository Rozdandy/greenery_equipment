from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Avg

from .models import ProductReview
from .forms import ProductReviewForm
from products.models import Product
from profiles.models import UserProfile


def add_review(request, product_id):
    """
    Allow user to add a review and redirect them back to the
    item product item view
    """
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    review_form = ProductReviewForm()
    review_details = {
        'topic': request.POST['topic'],
        'body': request.POST['body'],
        'rate': request.POST['rate'],
    }
    review_form = ProductReviewForm(review_details)

    # If form is valid, add user and product and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.save()

        review = ProductReview.objects.filter(product=product)
        avg_rate = review.aggregate(Avg('rate'))['rate__avg']
        product.avg_rating = int(avg_rate)
        product.save()

        messages.success(request, 'Thank you! Your review was added')
    else:
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


def edit_review(request, review_id):
    """
    Saves review form edited by user
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    review_form = ProductReviewForm(request.POST, instance=review)
    product = Product.objects.get(name=review.product)
    if review_form.is_valid():
        review.save()

        reviews = ProductReview.objects.filter(product=product)
        avg_rate = reviews.aggregate(Avg('rate'))['rate__avg']
        product.avg_rate = int(avg_rate)
        product.save()

        # Success message if added
        messages.success(request, 'Thank You! Your review was edited')
    else:
        # Error message if form was invalid
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_detail', args=(review.product.id,)))


def delete_review(request, review_id):
    """
    Deletes user's review
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = Product.objects.get(name=review.product)

    try:
        review.delete()

        reviews = ProductReview.objects.filter(product=product)
        avg_rate = reviews.aggregate(Avg('rate'))['rate__avg']
        if avg_rate:
            product.avg_rate = int(avg_rate)
        else:
            product.avg_rate = 0

        product.save()
        messages.success(request, 'Your review was deleted')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" eroor:{e} occured. Try again later.")

    return redirect(reverse('product_detail', args=(review.product.id,)))
