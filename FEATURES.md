# Green Local Veggies - Features

### Navigation Bar

The navigation bar is a crucial component, providing easy access to key areas of the site. It has been designed with user experience in mind, ensuring that visitors can quickly find what they're looking for.

![Navigation Bar mobile](readme_assets/images/features/navigation-mobile.png)

![Navigation Bar](readme_assets/images/features/navigation.png)



### Footer
The footer serves as an informational and navigational element at the bottom of each page, providing additional resources and links to enhance the user experience.

![Footer mobile](readme_assets/images/features/footer-mobile.png)

![Footer](readme_assets/images/features/footer.png)


### Home Page

The Home page serves as the welcoming gateway to Green Local Veggies, immediately immersing visitors in locally-sourced products that instantly communicates the site's purpose.

The page utilizes a clean, grid-based layout that allows for easy scanning and browsing of the product range. Each product is represented by a card that includes a image, the product name, price, and a conveniently placed "Add to Cart" button.

To enhance the shopping experience, the page includes robust filtering and sorting capabilities. Users can filter products by category, such as fruits or vegetables, allowing them to quickly narrow down their search to items of interest. The sorting feature enables users to order products by price and availability. These tools make it easy for customers to find exactly what they're looking for or discover new products that meet their preferences.

The page also includes a search bar, allowing users to quickly find specific items by name.

The page implements pagination to ensure fast loading times and a manageable browsing experience. Users can easily navigate through multiple pages of products, with clear indicators of their current page and the total number of pages available.

![Home Page mobile](readme_assets/images/features/home-mobile.png)

![Home Page](readme_assets/images/features/home.png)


### Product Detail Page

The Product Detail page provides an in-depth look at a specific product, offering all the information a customer needs to make an informed purchase decision. The page is dominated by a large, high-quality image of the product, allowing customers to see the product in detail.

Accompanying the image is a comprehensive product description. The page clearly displays the product's price and availability status. A quantity selector allows customers to easily choose how much of the product they wish to purchase, with clear indicators of any minimum or maximum order quantities. The prominent "Add to Cart" button makes it simple for customers to proceed with their purchase.

To provide additional value and encourage exploration of the product range, the page includes a "Related Products" section. This showcases items that are similar to the current product, helping customers discover new products and potentially increasing order values.

![Product Detail Page mobile](readme_assets/images/features/detail-mobile.png)

![Product Detail Page](readme_assets/images/features/detail.png)


### Register Page

The Register page is designed to provide a smooth and welcoming onboarding experience for new customers of Green Local Veggies. This page is crucial in converting visitors into registered users, allowing them to enjoy the full benefits of the platform such as order status tracking, saved delivery information, and personalized shopping experiences.

The page features a clean and intuitive registration form. The form requests essential information such as the user's first name and last name, complete address fields, email address, which will serve as their username, a password, and confirmation of that password. Since the platform is focused on local delivery, the city and zip code fields are presented as select dropdowns to ensure accurate address information.

To ensure data integrity and security, the form incorporates real-time validation. As users fill out the fields, immediate feedback is provided if any information is entered incorrectly or if required fields are left blank. This helps prevent submission errors and frustration for the user.

![Register Page mobile](readme_assets/images/features/register-mobile.png)

![Register Page](readme_assets/images/features/register.png)


### Login Page

The Login page provides registered users with secure access to their Green Local Veggies accounts. This page is designed to be straightforward and user-friendly, ensuring a quick and hassle-free login process while maintaining robust security measures.

The page features a simple, clean login form prominently displayed. This form consists of two main fields: one for the user's email address (which serves as their username) and another for their password.

For those who don't yet have an account, the login page includes a prominent link directing them to the registration page. This encourages new visitors to create an account and engage more deeply with Green Local Veggies.

![Login Page mobile](readme_assets/images/features/login-mobile.png)
![Login Page](readme_assets/images/features/login.png)


### User Profile Page

The User Profile page utilizes a tabular layout for easy navigation between different sections of the profile. Here's a breakdown of each tab:

#### Profile Details Tab

This tab displays the user's basic information. Users can view their personal details here.

![Profile tab mobile](readme_assets/images/features/profile-mobile.png)

![Profile tab](readme_assets/images/features/profile.png)

#### Update Profile Tab

This tab allows users to update their profile information, similar to the registration form.

![Profile update tab mobile](readme_assets/images/features/update-profile-mobile.png)

![Profile update tab](readme_assets/images/features/update-profile.png)

#### Change Password Tab

Users can update their account password in this section.

![Update password tab mobile](readme_assets/images/features/change-password-mobile.png)

![Update password tab](readme_assets/images/features/change-password.png)

#### Delete Account Tab

This tab offers users the option to delete their account from Green Local Veggies.

![Delete account tab mobile](readme_assets/images/features/delete-account-mobile.png)

![Delete account tab](readme_assets/images/features/delete-account.png)


### Cart Page

The Cart page serves as a crucial intermediary step in the purchasing process, allowing customers to review and modify their selections before proceeding to checkout. The page displays a comprehensive list of all items added to the cart, with each item shown with its image, name, price per unit, quantity, and subtotal.

Users have the flexibility to adjust quantities directly from this page, with intuitive increment and decrement buttons next to each item. There's also an option to remove items entirely from the cart, giving customers full control over their order composition. As changes are made, the page dynamically updates to reflect the new quantities and totals, providing immediate feedback to the user.

To encourage continued shopping, the Cart page includes a "Continue Shopping" button that takes users back to the product listings. For those ready to complete their purchase, a clear and prominent Checkout" button is provided, guiding users to the next step in the purchasing process.

![Cart Page mobile](readme_assets/images/features/cart-mobile.png)

![Cart Page](readme_assets/images/features/cart.png)


### Checkout Page

The Checkout page is designed to facilitate a smooth and secure transaction process, instilling confidence in the customer as they complete their purchase. The page is structured to guide the user through each step of the checkout process in a logical and intuitive manner.

At the top of the page, an order summary is presented, listing all items in the cart with their quantities and prices. This allows customers to perform a final review of their order before committing to the purchase.

After the order summary, the page prompts users to enter their delivery instructions. This is a complete CRUD operation where users can view, add, edit, and delete delivery instructions. This feature allows customers to provide specific details about their delivery preferences, such as preferred delivery times or special instructions for the order or the courier. For convenience, the instructions can be reused for future orders. A key feature on this implementation is that the delivery instruction is saved in the order itself when the order is placed, ensuring that later updates to the delivery instruction do not affect an order already placed.

The page then presents a section with delivery information. This is pre-populated with customer's saved address information, streamlining the process. From this section, the customer can go to their profile page to update their address or any other detail if needed.

In order to proceed to the payment step, customers must accept the terms and conditions of the purchase. A checkbox and a link to the terms and conditions are provided for this purpose. This ensures that users are aware of the site's policies and agree to them before finalizing their order.

The payment section of the page is integrated with Stripe for secure payment processing. Customers can enter their credit card details directly on the page, with clear indicators of the site's security measures to reassure users about the safety of their financial information.

Throughout the checkout process, clear error messages and form validation ensure that all necessary information is correctly provided before the order can be submitted. A final "Pay Now" button at the bottom of the page allows customers to complete their purchase.

![Checkout Page mobile](readme_assets/images/features/checkout-mobile.png)

![Checkout Page](readme_assets/images/features/checkout.png)


### Order History Page

The Order History page provides users with a detailed record of their past transactions with Green Local Veggies. This page is crucial for building trust and transparency, allowing customers to track their spending and easily reference past purchases.

Upon landing on the Order History page, users are presented with a chronological list of their orders, with the most recent orders displayed first. Each order entry in the list includes key information at a glance: the order number, date of purchase, total amount, and current status (e.g., processing, shipped, delivered).

For each order, a 'View' link allows users to access more comprehensive information regarding the order in it's own page. This page reveals the itemized list of products purchased in that order, including product names, quantities, and individual prices. This level of detail helps users recall exactly what they bought and when, which can be particularly useful for tracking seasonal purchases or planning future orders.

The detail order page also includes functionality for recent orders that haven't yet been processed, to be canceled.

![Order History Page mobile](readme_assets/images/features/history-mobile.png)

![Order History Page](readme_assets/images/features/history.png)


### Staff Dashboard

The Staff Dashboard is a restricted area accessible only to users with staff privileges. It provides a dashboard where staff members can manage orders, set order statuses, view user details, and assign deliveries to couriers.

Future development would include product management, customer support, settings for application appearance and functionality, and other administrative tasks.

![Staff Dashboard mobile](readme_assets/images/features/staff-mobile.png)

![Staff Dashboard Detail mobile](readme_assets/images/features/staff-detail-mobile.png)

![Staff Dashboard](readme_assets/images/features/staff.png)

![Staff Dashboard Detail](readme_assets/images/features/staff-detail.png)


### Courier Dashboard

The Courier Dashboard is designed for delivery personnel to manage and track their deliveries. It includes features that help couriers organize their routes, update delivery statuses, and view essential information about each delivery. A convenient mobile-friendly interface ensures that couriers can access the dashboard on the go, while the "Go to address" button provides quick navigation to the delivery location using Google Maps.

![Courier Dashboard mobile](readme_assets/images/features/courier-mobile.png)

![Courier Dashboard](readme_assets/images/features/courier.png)


### About Page

The About page serves as a window into the heart and soul of Green Local Veggies, offering visitors insight into the company's history, mission, and values. This page plays a crucial role in building trust with potential customers.

The page opens with a compelling narrative about the company's origins. This story helps to humanize the brand and create an emotional connection with visitors.

Following the origin story, the page elaborates on Green Local Veggies' mission statement. This section clearly articulates the company's commitment to providing high-quality, fresh produce while supporting local agriculture and promoting sustainable food.

The last section of the page highlights the company's delivery and working hours. This information is essential for customers to understand when they can expect their orders to arrive and the best times to place orders for timely delivery.

![About Page mobile](readme_assets/images/features/about-mobile.png)

![About Page](readme_assets/images/features/about.png)


### Contact Page

The Contact page serves as a vital communication bridge between Green Local Veggies and its customers.

A prominent feature of the page is the contact form. This form allows users to send messages directly through the website, without the need to open their email client. The form includes fields for the user's name, email address, subject of inquiry, and a message box. After the message is submitted, users are redirected to a "Thank You" page to confirm that their message has been received. The message is stored in the database for superadmin interaction.

Due to time limitation, this is the only implementation of the contact form and message storage. Future development would include a notification system for the Staff members with a system to reply to the messages and a record of the conversation.

In addition to the contact form, the page displays Green Local Veggies' customer business hours. This information sets clear expectations for when customers can anticipate a response, contributing to a transparent and trustworthy customer service experience.

The page also lists alternative contact methods. This includes a support service email address and phone number for those who prefer these communication channels.

![Contact Page mobile](readme_assets/images/features/contact-mobile.png)

![Contact Page](readme_assets/images/features/contact.png)


### Django Admin Panel (/admin/)

The Django Admin Panel is a powerful tool provided by Django for superusers to manage all aspects of the application.

![Admin Dashboard](readme_assets/images/features/admin-dashboard.png)

#### User Management (CUSTOMER)

- Comprehensive control over user accounts, including creation, modification, and deletion.
- Ability to assign different roles (staff, courier, superuser) and permissions.

Note on accounts and roles:
- Users registering through the regular registration form are automatically considered customers.
- Staff and couriers must register trough the regular registration form, and then be assigned their roles by a superuser in the admin panel.
- Superusers have full access to all areas of the application, but not to Courier Dashboard features by default (this can be customized in the admin panel by editing the user's permissions).
- All users have access to all public pages of the application, including the Profile page and its functionalities for easy account management.
- Staff and Courier Dashboards are restricted areas accessible only to users with the corresponding roles.

Notes on Customer messages:
- Messages sent through the Contact page are stored in the database for superadmin interaction and accessible in this section.
- Due to time limitation during the development of this project, there is no notification system for the Staff members with a system to reply to the messages and a record of the conversation. This is a feature that would be implemented in future development.
- The ability to edit or delete messages is not restricted.

#### Product Catalog Management (SHOP)

- Full CRUD (Create, Read, Update, Delete) operations for products.

#### Order Management (ORDERS)

- Detailed view and edit capabilities for all orders in the system.
- Advanced filtering and search options to find specific orders quickly.

#### Delivery Instructions

- Full CRUD operations available for the customer trough the Checkout page.
- This feature allows customers to provide specific details about their delivery preferences, such as preferred delivery times or special instructions for the order or the courier.
- A good use case for this feature (future development), would be the implementation of a customer support system where staff members can view and edit delivery instructions on behalf of the customer, or filtering inappropriate instructions.

[Go to README.md](README.md)