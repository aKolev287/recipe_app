from django.shortcuts import render, HttpResponse
from spice_swap.recipes.models import Recipe, Tag
from django.db.models import Count
from django.core.mail import send_mail
from .forms import FeedbackForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required

def index(request):
    highest_rated_recipes = Recipe.objects.annotate(num_likes=Count('like')).order_by('-num_likes')[:5]
    newest_recipes = Recipe.objects.order_by('-date')[:5]
    context = {
        'highest_rated_recipes': highest_rated_recipes,
        'newest_recipes': newest_recipes,
    }
    return render(request, 'common/index.html', context)

def breakfast_recipes(request):
    tag = Tag.objects.get(name='Breakfast')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/breakfast.html', context)

def lunch_recipes(request):
    tag = Tag.objects.get(name='Lunch')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/lunch.html', context)

def dinner_recipes(request):
    tag = Tag.objects.get(name='Dinner')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/dinner.html', context)

def snacks_recipes(request):
    tag = Tag.objects.get(name='Snacks')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/snacks.html', context)


def main_dish_recipes(request):
    tag = Tag.objects.get(name='Main Dish')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/main_dish.html', context)

def desserts(request):
    tag = Tag.objects.get(name='Desserts')
    recipes = Recipe.objects.filter(tags=tag)
    context = {
      'recipes': recipes,
    }
    return render(request, 'common/desserts.html', context)

def send_subscription_email(email):
    subject = 'Thank You for Subscribing to SpiceSwap'
    message = 'Thank you for subscribing to SpiceSwap!'
    from_email = 'akolev287@gmail.com'
    recipient_list = [email]

    # Load the HTML content of the email template
    html_message = render_to_string('common/subscription_email.html', {'email': email})

    # Create a plain text version of the email
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        send_subscription_email(email)
        return render(request, 'common/subscribe.html')
    return render(request, 'common/subscribe.html')

def feedback_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            send_mail('User Feedback', feedback, 'akolev287@gmail.com', ['alecto800@gmail.com'])
            return HttpResponse('Thank you for your feedback!')
    else:
        form = FeedbackForm()
    return render(request, 'common/feedback_page.html', {'form': form})