# Green Local Veggies

## Online Fresh Produce Delivery Platform

Green Local Veggies is a Django-based e-commerce application designed to facilitate the online ordering and delivery of fresh, locally-sourced fruits and vegetables in Westerstede, Germany. This project aims to bridge the gap between local farmers and urban consumers, promoting sustainable food practices and supporting the local economy.

### Project Overview

The Green Local Veggies platform offers a user-friendly interface for customers to browse, select, and purchase fresh produce online. It incorporates a robust backend system for order management, user authentication, and a courier dashboard for efficient delivery logistics. The application is built with scalability and maintainability in mind, utilizing modern web technologies and following best practices in web development.

[Live Demo](https://p4-green-local-veggies-c5f2f4c33912.herokuapp.com/)

![Responsive Design Screenshot](static/images/placeholder-image.jpg)

### Key Features

- User authentication and profile management
- Product catalog with categories for fruits and vegetables
- Advanced search and filter capabilities
- Shopping cart functionality
- Secure checkout process with Stripe integration
- Order tracking for customers
- Staff dashboard for order management
- Courier dashboard for delivery management
- Responsive design for optimal viewing on various devices

### Target Audience

- Local residents of Westerstede seeking fresh, locally-sourced fruits and vegetables
- Health-conscious consumers interested in supporting local agriculture
- Busy professionals looking for convenient grocery shopping options
- Local farmers and produce suppliers seeking an online platform to reach customers

## Features

### Key Features Summary
    - Cookie consent banner for GDPR compliance saving the consent in the session;
    - Home page with product listings, search capabilities, pagination, and filtering options;
    - Product detail page with detailed information, quantity selector, product availability, and "Add to Cart" button;
    - User registration and login pages with form validation and error handling;
    - User session storage for persistent login and cart data;
    - User profile page with tabs for profile details, update profile, change password, and delete account;
    - Cart page with a comprehensive list of items, quantity adjustment, and subtotal calculation;
    - Checkout page with order summary, delivery instructions, delivery information, payment processing, and terms acceptance;
    - Order history page for users to view past transactions, order details, and cancel recent orders;
    - About page with company history, mission statement, and delivery information;
    - Contact page with a contact form and alternative contact methods;
    - Staff dashboard for order management, order status updates, user details, and courier assignments;
    - Courier dashboard for delivery management, delivery status updates, and navigation to delivery locations;
    - Django admin panel for superusers to manage users, orders, and products;
    - Customized error pages for 404 and 500 errors with user-friendly messages and navigation links;
    - Responsive design for optimal viewing on various devices, including desktops, tablets, and smartphones;

### Additional Features Summary
    - Toast notifications for feedback on all actions;
    - "Show in Cart" button on product cards for quick access to the cart once an item is added;
    - Quantity lock and "Current quantity in cart" for products already in the cart (on the product detail page);
    - Delivery instructions automatically selected upon editing;

Details about the features, their implementation, and the user experience can be found in the [Features](FEATURES.md) document.

## User Experience (UX)

### Project Goals

#### Site Owner Goals

- Establish an online presence for Green Local Veggies in Westerstede, Germany
- Create a platform that connects local farmers with urban consumers
- Promote sustainable food practices and support the local economy
- Provide a user-friendly interface for customers to browse and purchase fresh produce online
- Implement an efficient system for order management and delivery logistics
- Build a scalable and maintainable e-commerce solution
- Increase sales and customer base for local produce
- Offer a convenient alternative to traditional grocery shopping

#### User Goals

- Find and purchase fresh, locally-sourced fruits and vegetables conveniently online
- Support local farmers and sustainable agriculture practices
- Access detailed information about products, including origin and nutritional value
- Easily navigate through product categories and search for specific items
- Manage personal accounts, including order history and delivery preferences
- Experience a smooth and secure checkout process
- Receive timely updates on order status and delivery information
- Access the platform seamlessly across various devices (desktop, tablet, mobile)
- Provide feedback and communicate with the Green Local Veggies team
- Stay informed about seasonal offerings and special promotions

These project goals align with the overall mission of Green Local Veggies to bridge the gap between local farmers and urban consumers while promoting sustainable food practices. The site owner aims to create a robust, user-friendly platform that serves both the business objectives and the needs of the target audience, ultimately contributing to the local economy and encouraging healthier, more sustainable food choices.

### User Stories (in order of priority and relation to the project goals)
User stories are implemented in the project. The user stories are linked to the Github issues and the project board. When created, the user stories were prioritized based on their importance and relevance to the project goals using the MoSCoW method (Must have, Should have, Could have, Won't have). Story points were assigned to each user story to estimate the level of effort required for implementation. The user stories were then added to the project board and assigned to the appropriate project milestone for tracking progress.

[User Stories (Github issue)](https://github.com/zioan/pp4_GreenLocalVeggies/issues)
<br>
[Kanban Board (Github project)](https://github.com/users/zioan/projects/5)

#### 1. View Main Page with Products
As a Site User, I can view the main page displaying all products so that I can browse the available items.
##### Acceptance Criteria
- When a user visits the main page, a list of all available products is displayed.
- Each product listing includes a thumbnail image, name, price, and a brief description.
- The user can click on a product to view its detailed page.

#### 2. Search for Products
As a Site User, I can search for products so that I can quickly find items I am interested in.
##### Acceptance Criteria
- A search bar is available on the main page.
- When a user enters a search term, relevant products are displayed in the search results.
- The search results include product name, image, and price.

#### 3. Filer Products
As a Site User, I can filter products by category, price range, and availability so that I can easily find what I need.
##### Acceptance Criteria
- Filters for category and price range.
- When a filter is applied, the product listings update to show only the relevant products.

#### 4. View Product Details
As a Site User, I can click on a product so that I can read the full details.
##### Acceptance Criteria
- When a product title is clicked, a detailed view of the product is seen.
- The detailed view should include the product name, description, price, and available stock.
- The view should display an image of the product.
- The view should have an option to add the product to the cart.

#### 5. Account Registration
As a Site User, I can register an account so that I can place orders.
##### Acceptance Criteria
- Given an email, a user can register an account.
- Then the user can log in.
- When the user is logged in, they can place orders.

#### 6. User Profile Management
As a Site User, I can manage my profile so that I can update my personal information and view my order history.
##### Acceptance Criteria
- The user can update their personal information (name, email, address).
- The user can view their past orders and order details.

#### 7. Add to Cart
As a Site User, I can add products to my cart so that I can purchase them later.
##### Acceptance Criteria
- When a product is added to the cart, it appears in the cart with the correct quantity.
- The cart shows the total price of all added products.

#### 8. Product Recommendations
As a Site User, I can see product recommendations based on my browsing and purchase history so that I can discover new items.
##### Acceptance Criteria
- Recommendations are displayed on the product detail pages.

#### 9 Delivery Instructions
As a Customer, I can provide and save custom delivery instructions so that I can ensure my orders are delivered according to my preferences.
##### Acceptance Criteria:
- Customers can view (use), add, edit, and delete custom delivery instructions in their profile.
- Saved instructions can be selected during the checkout process.

#### 10. Checkout and Payment
As a Site User, I can checkout and make a payment so that I can complete my purchase.
##### Acceptance Criteria
- Given a filled cart, the user can proceed to checkout.
- The user can enter payment and shipping information.
- The user receives a confirmation message or some kind of notification upon successful payment.

#### 11. View Order History
As a Site User, I can view my order history so that I can keep track of my past purchases.
##### Acceptance Criteria
- Given a logged-in user, they can view a list of their past orders.
- Each order includes details such as order date, items purchased, total amount, and order status.

#### 12. Order Status Tracking
As a Customer, I can track the status of my order so that I know when to expect my delivery.
##### Acceptance Criteria:
- Customers can view the current status of their order (e.g., processing, delivered).

#### 13. Staff Member Dashboard
As a Staff Member, I can access a comprehensive dashboard so that I can manage orders.
##### Acceptance Criteria:
- Staff members can log in to a secure, role-specific dashboard.
- The dashboard provides an overview of current orders and their statuses.

#### 14. Courier Dashboard
As a Courier, I can access a dedicated dashboard so that I can manage and track my delivery tasks efficiently.
##### Acceptance Criteria:
- Couriers can log in to a secure, role-specific dashboard.
- The dashboard displays a list of pending deliveries assigned to the courier.
- Couriers can update the status of each delivery (e.g., delivered).
- The dashboard provides a map or navigation assistance for delivery routes.
- Couriers can view customer contact information for each delivery.

#### 15. Admin dashboard (Django Admin Panel)
As a Site Admin, I can access an admin dashboard so that I can manage products, orders, and users efficiently.
##### Acceptance Criteria
- The admin dashboard provides an overview (sales, orders).
- Admins can navigate to different sections to manage products and orders.

##### 16. Manage Products (Django Admin Panel - early implementation)
As a Site Admin, I can create, read, update, and delete products so that I can manage my inventory.
##### Acceptance Criteria
- Given a logged-in admin, full CRUD access and functionality over the products must be provided.

A complete list of user stories (including not implemented ones) can be found in the [Issues](https://github.com/zioan/pp4_GreenLocalVeggies/issues) section of the project repository.


### Design Choices
#### Color Scheme
The color scheme for Green Local Veggies has been carefully selected to reflect the natural, fresh, and organic qualities of the products.

![Color Scheme](placeholder.jpg)

#### Typography
Typography plays a crucial role in conveying the brand's personality and enhancing readability. The following fonts have been chosen for their modern, clean, and elegant qualities:

** remember to edit - MUST BE IMPLEMENTED **

Headings: Montserrat (Sans-serif)
Body Text: Lora (Serif)

#### Imagery
The imagery used throughout the Green Local Veggies website is carefully curated to showcase the product quality.
More info on the images used in the project can be found in the Credits section.


### Wireframes
To ensure a responsive and user-friendly design across various devices, wireframes were created for mobile and desktop views. These wireframes serve as a blueprint for the layout and structure of key pages in the Green Local Veggies e-commerce platform.

#### Mobile Design
The mobile design focuses on a streamlined, vertical layout that prioritizes essential information and easy navigation for users on smaller screens.

Key features of the mobile design include:

A hamburger menu for compact navigation
Large, touch-friendly product cards

#### Desktop Design
The desktop design offers the full experience, with a spacious layout that showcases products and allows for easy browsing and purchasing.

Desktop design features:

Full navigation menu
Three or four-column product grid

#### Key Pages Wireframed:

Home Page
![Home wireframe](readme_assets/images/wireframes/home.png)

![Home wireframe mobile](readme_assets/images/wireframes/home-mobile.png)

Product Detail Page
![Product Detail wireframe](readme_assets/images/wireframes/details.png)

![Product Detail wireframe mobile](readme_assets/images/wireframes/details-mobile.png)

Shopping Cart
![Shopping Cart wireframe](readme_assets/images/wireframes/cart.png)

![Shopping Cart wireframe mobile](readme_assets/images/wireframes/cart-mobile.png)

Checkout Page
![Checkout Page wireframe](readme_assets/images/wireframes/checkout.png)

![Checkout Page wireframe mobile](readme_assets/images/wireframes/checkout-mobile.png)

User Profile
![User Profile wireframe](readme_assets/images/wireframes/user.png)

![User Profile wireframe mobile](readme_assets/images/wireframes/user-mobile.png)

These wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/).

#### Wireframe to Implementation
As the project progresses, these wireframes serve as a guide for the development. However, it's important to note that the final implementation may vary slightly from these initial designs as I iterate and refine the user experience based on testing.


## Information Architecture
### Database Schema (ERD Diagram)
![ERD Diagram](readme_assets/images/erd.png)

### Data Models Description
#### PRODUCT
Represents the items available for purchase on the platform.

- ID: Primary key, unique identifier for each product
- Name: String, name of the product
- Description: Text, detailed description of the product
- Price: Decimal, price of the product
- Stock: Integer, current available quantity of the product
- Unit: String, unit of measurement for the product (e.g., kg, piece)
- Category: String, category of the product
- Image: String, path or URL to the product image
- Slug: String, URL-friendly version of the product name

#### CUSTOMERUSER
Represents registered users of the Green Local Veggies platform, including customers, staff, and couriers.

- ID: Primary key, unique identifier for each user
- FirstName: String, user's first name
- LastName: String, user's last name
- Street: String, street name of user's address
- HouseNumber: String, house number of user's address
- City: String, city of user's address
- ZipCode: String, zip code of user's address
- Email: String, user's email address
- PhoneNumber: String, user's contact number
- IsActive: Boolean, indicates if the user account is active
- IsStaff: Boolean, indicates if the user has staff privileges
- IsCourier: Boolean, indicates if the user is a courier
- DateJoined: DateTime, date and time when the user registered
- LastLogin: DateTime, date and time of the user's last login

#### ORDER
Represents a customer's order.

- ID: Primary key, unique identifier for each order
- User: Foreign key, references the CUSTOMERUSER who placed the order
- CreatedAt: DateTime, timestamp of when the order was created
- UpdatedAt: DateTime, timestamp of the last update to the order
- Paid: Boolean, indicates if the order has been paid for
- Status: String, current status of the order (e.g., "Pending", "Shipped", "Delivered")
- TotalPrice: Decimal, total cost of the order
- DeliveryInstruction: Text, custom instructions for order delivery

#### ORDERITEM
Represents individual items within an order.

- ID: Primary key, unique identifier for each order item
- Order: Foreign key, references the ORDER this item belongs to
- Product: Foreign key, references the PRODUCT in this order item
- Price: Decimal, price of the product at the time of order
- Quantity: Integer, quantity of the product in this order item

#### DELIVERYINSTRUCTION
Represents saved delivery instructions for a user.

- ID: Primary key, unique identifier for each delivery instruction
- User: Foreign key, references the CUSTOMERUSER who created the instruction
- Title: String, short title or name for the delivery instruction
- Instruction: Text, detailed delivery instructions
- CreatedAt: DateTime, timestamp of when the instruction was created
- UpdatedAt: DateTime, timestamp of the last update to the instruction

### Database Relationships

#### CUSTOMERUSER to ORDER: One-to-Many

A CUSTOMERUSER can place multiple ORDERs, but each ORDER belongs to only one CUSTOMERUSER.
This relationship is represented by the foreign key 'User' in the ORDER model.


#### CUSTOMERUSER to DELIVERYINSTRUCTION: One-to-Many

A CUSTOMERUSER can create multiple DELIVERYINSTRUCTIONs, but each DELIVERYINSTRUCTION belongs to only one CUSTOMERUSER.
This relationship is represented by the foreign key 'User' in the DELIVERYINSTRUCTION model.


#### ORDER to ORDERITEM: One-to-Many

An ORDER can contain multiple ORDERITEMs, but each ORDERITEM belongs to only one ORDER.
This relationship is represented by the foreign key 'Order' in the ORDERITEM model.


#### PRODUCT to ORDERITEM: One-to-Many

A PRODUCT can be included in multiple ORDERITEMs, but each ORDERITEM refers to only one PRODUCT.
This relationship is represented by the foreign key 'Product' in the ORDERITEM model.


This database schema provides a comprehensive structure for the Green Local Veggies e-commerce platform. It supports key functionalities such as:

- User management with different roles (customer, staff, courier)
- Product catalog with detailed product information
- Order processing with line items and delivery instructions
- Saved delivery instructions for repeat customers


## Technologies Used
### Languages
- HTML5
- CSS3
- JavaScript
- Python 3.8+

### Frameworks & Libraries
- Django 5.0.6 - High-level Python web framework that encourages rapid development and clean, pragmatic design;
- Bootstrap 5.2 - Front-end framework for developing responsive and mobile-first websites;
- Cloudinary 1.40.0 - Cloud service that offers a solution to a web application's entire image management pipeline;
- django-cloudinary-storage 0.3.0 - Django package that facilitates integration with Cloudinary;
- Gunicorn 22.0.0 - Python WSGI HTTP Server for UNIX, used to run Python web applications on Heroku;
- Pillow 10.4.0 - Python Imaging Library (PIL), adding image processing capabilities to Python interpreter;
- Whitenoise 6.7.0 - Allows Django apps to serve its own static files, making it self-contained and easier to deploy;
- Stripe 10.6.0 - Payment processing platform for online businesses.

### Databases
- SQLite (development) - Lightweight disk-based database that doesn't require a separate server process;
- PostgreSQL (production) - Powerful, open-source object-relational database system.

### Other Tools & Services
- Git - Version control system for tracking changes in source code during software development;
- GitHub - Internet hosting service for software development, version control using Git, user stories (Issues), and project management;
- Heroku - Cloud platform used to deploy the Green Local Veggies application;
- Stripe - Payment processing platform for online businesses;
- Cloudinary - Cloud-based image and video management service;
- Balsamiq - Wireframing tool for creating low-fidelity wireframes;
- Google Fonts - Library of free and open-source font families;
- Font Awesome - Icon toolkit for web development;
- dj-database-url 2.2.0 - Utility to help configure Django application database from the DATABASE_URL environment variable;
- psycopg2-binary 2.9.9 - PostgreSQL adapter for Python.


## Version Control

Throughout the development process, I used Git for version control, with Visual Studio Code as my primary development environment (MacOS 14.6.1). This setup allowed me to manage my code efficiently. Here's an overview of my workflow:

1. **Development in VS Code**: 
   I used VS Code as my main IDE for writing and editing Django code. The integrated terminal allowed me to run Django commands and manage my virtual environment easily.

2. **Leveraging VS Code's Source Control**:
   VS Code's Source Control panel was instrumental in managing changes across my complex Django project structure. After making significant changes involving multiple apps, views, and URL configurations, I used the Source Control panel to review all modifications in one place. This comprehensive view helped me logically group changes into meaningful commits, ensuring that each commit represented a coherent unit of work despite the intricate relationships in Django.

3. **Commit Strategy**:
   Given Django's interconnected nature, I often made changes across multiple files (e.g., models, views, templates, and URLs) for a single feature. VS Code's diff viewer allowed me to carefully review these changes, helping me create commits that encapsulated related modifications across different parts of the project. I aimed to create descriptive commit messages that explained the purpose of each set of changes, making it easier to understand the project's evolution and helping maintainability.

4. **Key Git Commands**:
   I frequently used the following Git commands:
   - `git add <file>` or `git add .`: To stage specific files or all changes.
   - `git commit -m "descriptive message"`: To create a commit with a meaningful message.
   - `git push`: To push changes to my remote repository.

5. **Syncing with Remote**:
   I regularly used `git pull` to keep my local repository up-to-date with the remote, especially after making changes in the project's GitHub repository (Kanban board) or Issues. This practice helped me avoid conflicts and stay aligned with the latest changes.

By leveraging VS Code's Git integration and following these practices, I maintained a clean and understandable version history throughout my project's development, even as I worked with Django's complex structure and interconnected components.


## Deployment

I deployed this Django application on Heroku, taking advantage of its integration with GitHub. Here's a step-by-step overview of my deployment process:

1. **Heroku App Creation**:
   I logged into my Heroku dashboard and clicked "New" > "Create new app". I chose a unique app name and selected the appropriate region.

2. **GitHub Integration**:
   In the app's "Deploy" tab, I selected GitHub as the deployment method. I connected to my GitHub account and selected the repository containing my Django app.

3. **Environment Configuration**:
   In the "Settings" tab, I clicked on "Reveal Config Vars" and added the necessary environment variables:

- `SECRET_KEY`: My Django secret key
- `DATABASE_URL`: The URL provided by Code Institute for the database
- `CLOUDINARY_URL`: The URL provided by Cloudinary for image storage
- `STRIPE_PUBLISHABLE_KEY`: My Stripe publishable key
- `STRIPE_SECRET_KEY`: My Stripe secret key

4. **Database Configuration**:
   Since my database is provided by Code Institute, I ensured the `DATABASE_URL` in Config Vars was correctly set to the provided database URL. In my Django settings, I made sure to use this environment variable to configure the database connection.

5. **Buildpack Configuration**:
   Still in the "Settings" tab, I scrolled to the "Buildpacks" section, clicked "Add buildpack", and selected "heroku/python".

6. **Deployment Configuration**:
   In the "Deploy" tab, under "Deployment method", I confirmed that GitHub was selected. In the "App connected to GitHub" section, I ensured my repository was selected.

7. **Manual Deploy**:
   I scrolled to the "Manual deploy" section, chose the `main` branch, and clicked "Deploy Branch".

8. **Verify Deployment**:
   Once the deployment was complete, I clicked "View" to open my app and verify it was working correctly.


## Forking and Local Setup

If you'd like to fork this repository and run it locally, follow these steps:

1. **Fork the Repository**:
   - Navigate to the GitHub repository: [Green Local Veggies repository](https://github.com/zioan/pp4_GreenLocalVeggies)
   - In the top-right corner of the page, click the "Fork" button.
   - This will create a copy of the repository in your GitHub account.

2. **Clone Your Fork**:
   - On your forked repository page, click the "Code" button and copy the URL.
   - Open your terminal and run:
     ```
     git clone [URL you just copied]
     ```
   - This creates a local copy of the repository on your machine.

3. **Set Up Virtual Environment**:
   - Navigate into the project directory:
     ```
     cd [project directory name]
     ```
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

4. **Install Dependencies**:
   - With your virtual environment activated, install the required packages:
     ```
     pip install -r requirements.txt
     ```

5. **Set Up Environment Variables**:
   - Create a `env.py` file in the root directory of the project.
   - Add the following variables (replace with your actual values):
     ```
     SECRET_KEY=your_secret_key
     DATABASE_URL=your_database_url
     CLOUDINARY_URL=your_cloudinary_url
     STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
     STRIPE_SECRET_KEY=your_stripe_secret_key
     DEBUG=True
     ```
    Important Notes: 
    - Make sure to set `DEBUG=True` for local development and testing in `env.py`. In `settings.py`, DEBUG mode will be automatically recognized for the development environment based on the presence of the `DEBUG` variable in `env.py`.
    - Remember to never commit the `env.py` file or any sensitive information to version control. If you plan to deploy your fork, make sure to set up the necessary environment variables in your deployment environment.

    Note on automated testing: Automated tests are present for all apps in the project. To run the tests run `python manage.py test` in the terminal.

6. **Apply Migrations**:
   - Run the following commands to apply database migrations:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

7. **Run the Development Server**:
   - Start the Django development server:
     ```
     python manage.py runserver
     ```
   - Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.


## Testing

Comprehensive testing has been conducted to ensure the functionality, usability, and reliability of this Django e-commerce application. My testing approach includes:

- User Story Testing: Verification of features against defined user stories
- Manual Testing: Thorough checks across various browsers
- Automated Testing: Automated tests for critical components

For detailed information on the testing procedures, results, and ongoing test plans, please refer to the [TESTING.md](TESTING.md) file. This document provides in-depth coverage of the testing methodologies, including specific test cases, browser compatibility results, and the outcomes of the automated test suites.