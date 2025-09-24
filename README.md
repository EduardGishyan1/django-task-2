# ChildProfile Demo – Front-End & API Endpoints

This Django project provides:

* **User Authentication** (JWT via `authapp`)
* **Children Management** (create/list child profiles)
* **Categories & Products** (products can belong to a category)
* **Wishlist** (each user can add/remove products to their wishlist)

It includes **HTML templates (front end)** using plain HTML/JS/CSS and **REST API endpoints** built with Django REST Framework.

---

```bash

source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# migrate database
python manage.py migrate

# create a superuser (optional)
python manage.py createsuperuser

# run server
python manage.py runserver

Front-End Pages
Page / Template	URL	Description
Register / Login	/auth/register, /auth/login, 	User sign-up / sign-in (JWT).
Children – List	/children/list-page, 	View all children of the logged-in user.
Children – Add	/children/add-page, 	Add a child profile.
Children  /children/select-page.  Front-end page to select a child by ID
Category – Create	/categories/page, 	Create a new category.
Product – List	/products/list-page, 	View all products (with optional search).
Product – Add	/products/add-page,	Create a new product and assign a category.
Wishlist – List	/wishlist/page,	View the current user’s wishlist.
Wishlist – Add	/wishlist/add-page/,	Add a product to the current user’s wishlist.