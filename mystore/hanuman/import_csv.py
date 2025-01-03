# management/commands/import_csv.py

import csv
from django.core.management.base import BaseCommand
from yourapp.models import Product

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Product.objects.create(
                    name=row['name'],
                    price=row['price'],
                    # Add other fields here
                )
/* Reset default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Global styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    color: #333;
}

.container {
    width: 80%;
    margin: 0 auto;
    padding:20px;
}

header {
    background-color: #4CAF50;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    font-size: 2em;
    margin-left: 20px;
}

nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

nav ul li a:hover {
    text-decoration: underline;
}

section {
    padding: 40px 0;
}

section h2 {
    font-size: 1.5em;
    margin-bottom: 20px;
    color: #4CAF50;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

.owl-carousel .owl-item img {
    display: block;
    width: 100%;
    height: auto;
}

/* Unique styles */
#price {
    background-color: #fff;
}

#features {
    background-color: #f9f9f9;
}

#features .owl-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 100%;
}

#features .owl-prev {
    left: 10px;
}

#features .owl-next {
    right: 10px;
}

#other-features {
    background-color: #fff;
}
