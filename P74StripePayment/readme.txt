# implment Stripe payment Gateway
project : P74StripePayment

1. Creating a Django Project
   django-admin startproject projectname
   After creating the project, create a new app named payments.
   cd projectname
   python manage.py startapp payments
   Add payments app to settings.py in the list of INSTALLED_APPS.

2. Create Stripe Account
   create a account name or bussines verify(for live)
   get Stripe API Key
   Configuring stripe : pip install stripe    

3. Add in settings.py :
    if DEBUG:
    STRIPE_PUBLISHABLE_KEY = 'test_publishable_key'
    STRIPE_SECRET_KEY = 'test_secret_key'
    # Uncomment these lines if you have a live keys
    # else:
    #     STRIPE_PUBLISHABLE_KEY = 'production_publishable_key'
    #     STRIPE_SECRET_KEY = 'production_secret_key'  
    
    
4. Create Product Model   (products/models.py)  
   This will create a table named Products in the database with id, name, description, and price columns.
   Commit the changes to the database using:
   python manage.py makemigrations
   python manage.py migrate

5. Create Views 
    ProductCreateView - To create a new Product.
    ProductListView - This is the home page of our application. We'll display a list of products in the database here.
    ProductDetailView - As the name indicates, this view will be used to display the details of a product. We'll integrate Stripe Payment Gateway to this page.
    create_checkout_session - This view serves as an API to initialize the payment gateway.
    PaymentSuccessView - This is that page that users will be redirected to after successful payment.
    PaymentFailedView - This is that page that users will be redirected to if the payment failed.
    OrderHistoryView - All previous orders and status will be displayed on this page.

6. Templates
    Create a new folder named payments in the templates folder of payments and add 
    base.html, navbar.html, product_list.html, product_create.html, product_detail.html, payment_success.html, payment_failed.html, and order_history.html
    files to the folder.


7. projectname/urls.py    

8. payments/urls.py (app):
9. payments/templates/payments/base.html
9. payments/templates/payments/navbar.html
10. ProductCreate View :Let us write the code to create products and save them to the database.and write code  product_create.html 
11. ProductList View :In this page, we'll display the products from the database. andwrite code for product_list.html

**Run the project using python manage.py runserver and some products to the database.

12. Integrating Stripe Payment to Product Detail Page
    This is the most important page of our project. In the page, we'll display the details of a selected product along with a checkout button to purchase the product. We will also integrate the Stripe payment gateway on this page.

    Modify the code of ProductDetailPage and add code for  product_detail.html


13. The OrderDetails Model : After creating the checkout session id, we will store it in the database along with the order details to the database. For that, add a new model to the database.   
products/models.py

14. Creating Stripe Checkout Session (function based)
    In this view, we are performing three main actions.

    Creating a Stripr checkout session using the Stripe Library.
    Saving the order details along with the payment intent obtained from stripe session. You can consider payment intent as a unique identifier for each payments.
    Return the session ID as JSON data.

15. Redirecting the user
    In the client side, we should add the Stripe JavaScript SDK and redirect the user to a payment page.  
    add code to the end of product_detail.html  : This code will make an AJAX request to create_checkout_session view and collect the checkout session id. After obtaining the id, the user will be redirected to a Stripe hosted payment page.

16. Handling Successful Payments : payments/views.py
    In the get handler of PaymentSuccessView, we are using the session_id obtained from the URL to mark the Order as completed.    
    
17. Payment Failure Page : payments/views.py & payment_failed.html
18. Order History Page : In this page, we can view the payment history.
    payments/views.py  &  order_history.html



***  This is how we can integrate Stripe Payment Gateway with our Django Application.    ***


Detailed Description  : https://www.geekinsta.com/integrate-stripe-with-django/
    
