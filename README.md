# 🛒 Django Storefront Backend

This project is a comprehensive backend for an e-commerce storefront, developed while following Mosh Hamedani's **Ultimate Django Series (Part 1 & 2)**. It features a robust product catalog, user authentication, and cart/order handling using Django REST Framework.

⚠️ **Note:** This project is backend-only and does not include a frontend UI.

## 🧱 Features

- 🔐 **User Authentication** using Djoser (Token & JWT-based)
- 🗃️ **Product Management** with collections, promotions, inventory control
- 🛍️ **Shopping Cart** with support for multiple items per cart
- 🧾 **Order Handling** and status tracking
- ✍️ **Product Reviews** with timestamps
- 📦 **Customer Profiles** with tiered membership support
- 🏢 **Admin Dashboard** customization
- 🧮 **Django ORM** for efficient query building and model relations

## 🛠️ Technologies

- Python 3
- Django
- Django REST Framework (DRF)
- Djoser (for authentication)
- JWT & Token Authentication
- MySQL
- Django Admin Customization

## ⚙️ Installation

```bash
git clone https://github.com/your-username/django-storefront.git
cd django-storefront
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
