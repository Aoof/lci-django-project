import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msabdulrahman.settings')
django.setup()

from product.models import Product

# Clear existing products
Product.objects.all().delete()

# Sample data based on original hardcoded products
products = [
    {
        'name': 'tommy helfinger bar',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 5.0,
        'price': '5$-300$',
        'category': 'resturent',
        'ratings_count': 10,
    },
    {
        'name': 'swim and dine resort',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 4.5,
        'price': '50$-500$',
        'category': 'hotel',
        'ratings_count': 8,
    },
    {
        'name': 'europe tour',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 5.0,
        'price': '5k$-10k$',
        'category': 'destination',
        'ratings_count': 15,
    },
    {
        'name': 'banglow with swiming pool',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 5.0,
        'price': '10k$-15k$',
        'category': 'real estate',
        'ratings_count': 10,
    },
    {
        'name': 'vintage car expo',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 4.2,
        'price': '500$-1200$',
        'category': 'automotion',
        'ratings_count': 8,
    },
    {
        'name': 'thailand tour',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incid ut labore et dolore magna aliqua....',
        'rating': 5.0,
        'price': '5k$-10k$',
        'category': 'destination',
        'ratings_count': 15,
    },
]

for product_data in products:
    product = Product.objects.create(**product_data)
    print(f"Created product: {product.name}")

print("Sample data populated successfully!")