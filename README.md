# Django E-commerce.

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/PayPal-000144?logo=paypal&logoColor=white" />
</p>


<hr class="dotted">
It is an E-commerce system built in Django. It contains all the essentials for adding products and use PayPal and Stripe as payment systems.

## About this Project:

It is an E-commerce system built in Django. It contains all the essentials for adding products and use PayPal and Stripe as payment systems.

The repository is a start point for most of my professional projects; for this, I'm using as a part of my portfolio, feel free to use wherever you want. I'll be happy if you provide any feedback or code improvements or suggestions.

Connect with me at:

<p align='center'>
    
  <a href="https://www.linkedin.com/in/fl4viooliveira/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://stackoverflow.com/users/13045151/">
    <img src="https://img.shields.io/badge/stackoverflow-%23E4405F.svg?&style=for-the-badge&logo=stackoverflow&logoColor=white" />        
  </a>&nbsp;&nbsp;
  
</p>

<p align='center'>
  📫 How to reach me: <a href='mailto:fl4viooliveira@gmail.com'>fl4viooliveira@gmail.com</a>
</p>
<p align='center'>
  <a href="#"><img src="https://badges.pufler.dev/visits/fl4viooliveira/django_ecommerce"></a> 
</p>

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

📫Email-me: <a href='mailto:fl4viooliveira@gmail.com'>fl4viooliveira@gmail.com</a>

 <a href="https://www.linkedin.com/in/fl4viooliveira/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;&nbsp;

Thank you!

## License

<a href="https://github.com/fl4viooliveira/django_ecommerce/blob/master/LICENSE">
    <img alt="NPM" src="https://img.shields.io/npm/l/license?style=for-the-badge">
</a>&nbsp;&nbsp;

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fl4viooliveira/django_ecommerce/blob/master/LICENSE) file for details.