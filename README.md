# Django E_commerce.

It is an E-commerce system built in Django. It contains all the essentials for adding products and use PayPal and Stripe as payment systems.

## About this Project:

It is an E-commerce system built in Django. It contains all the essentials for adding products and use PayPal and Stripe as payment systems.

The repository is a start point for most of my professional projects; for this, I'm using as a part of my portfolio, feel free to use wherever you want. I'll be happy if you provide any feedback or code improvements or suggestions.

Email-me: fl4viooliveira@gmail.com

Connect with me at [LinkedIn](https://www.linkedin.com/in/flavio-oliveira-4293641aa/)

## Some technical information:

- Django - 3.1.1
- Django Allauth - 0.42.0
- Django Crispy Forms - 1.9.2
- Django Environ - 0.4.5
- Stripe - 2.51.0

## To Install:

Cloning the Repository:

```
$ git clone https://github.com/fl4viooliveira/django_ecommerce.git

$ cd django_ecommerce 

```

Installing the environment control:

```
$ pip install virtualenv

$ virtualenv env

```

Activating the environment:

on Windows:
```
env\Scripts\activate

```
on Mac OS / Linux:
```
$ source env/bin/activate

```

Installing dependencies:

```
$ pip install -r requirements.txt

```

Create a .env file on ecom folder (/ecom/.env) setting all requirements without using space after "=". 

Copy and paste on our .env file:

```
DEBUG=
SECRET_KEY=
DEFAULT_FROM_EMAIL=
NOTIFY_EMAIL=
PAYPAL_SANDBOX_CLIENT_ID=
PAYPAL_SANDBOX_SECRET_KEY=
PAYPAL_LIVE_CLIENT_ID=
PAYPAL_LIVE_SECRET_KEY=
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

```

Last commands to start:

```
$ python manage.py makemigrations

$ python manage.py migrate

```
Create a super user:

```
$ python manage.py createsuperuser admin-name

```

Finishing running server:

```
$ python manage.py runserver

```

## Contributing

You can send how many PR's do you want, I'll be glad to analyse and accept them! And if you have any question about the project...

Email-me: fl4viooliveira@gmail.com

Connect with me at [LinkedIn](https://www.linkedin.com/in/flavio-oliveira-4293641aa/)

Thank you!
