# Green Local Veggies - Testing

## Manual Testing

### User Story Testing

| User Story | Test Performed | Result | Pass/Fail |
|------------|----------------|--------|-----------|
| As a Site User, I can view the main page displaying all products so that I can browse the available items | Navigate to the main page and check for product listings | The main page displays a list of all available products with thumbnail images, names, prices, and brief descriptions | Pass |
| As a Site User, I can search for products so that I can quickly find items I am interested in | Use the search bar on the main page to search for a specific product | Relevant products are displayed in the search results, including product name, image, and price | Pass |
| As a Site User, I can filter products by category, price range, and availability so that I can easily find what I need | Apply filters for category, price range, and availability | Product listings update to show only the relevant products based on the applied filters | Pass |
| As a Site User, I can click on a product so that I can read the full details | Click on a product card to view its detailed page | A detailed view of the product is displayed, showing the product name, description, price, available stock, image, and an option to add to cart | Pass |
| As a Site User, I can register an account so that I can place orders | Attempt to register an account with an email address | User is able to register, log in, and place orders when logged in | Pass |
| As a Site User, I can manage my profile so that I can update my personal information and view my order history | Log in and navigate to the profile management section | User can update personal information and view past orders with details | Pass |
| As a Site User, I can add products to my cart so that I can purchase them later | Add a product to the cart and check the cart contents | The product appears in the cart with the correct quantity, and the total price is displayed | Pass |
| As a Site User, I can see product recommendations so that I can discover new items | View a product detail page and check for recommendations | Product recommendations are displayed on the product detail pages | Pass |
| As a Customer, I can provide and save custom delivery instructions so that I can ensure my orders are delivered according to my preferences | Add, edit, and delete custom delivery instructions during checkout | Custom delivery instructions can be managed and selected during checkout | Pass |
| As a Site User, I can checkout and make a payment so that I can complete my purchase | Proceed to checkout with a filled cart and complete the payment process | User can enter payment and shipping information, and receives a confirmation message upon successful payment | Pass |
| As a Site User, I can view my order history so that I can keep track of my past purchases | Log in and navigate to the order history section | A list of past orders is displayed | Pass |
| As a Customer, I can track the status of my order so that I know when to expect my delivery | View the status of a placed order | The current status of the order (e.g., processing, delivered) is visible to the customer | Pass |
| As a Staff Member, I can access a comprehensive dashboard so that I can manage orders | Log in as a staff member and access the dashboard | A secure, role-specific dashboard is available, providing an overview of current orders and their statuses | Pass |
| As a Courier, I can access a dedicated dashboard so that I can manage and track my delivery tasks efficiently | Log in as a courier and access the dashboard | A secure, role-specific dashboard displays pending deliveries, allows status updates, provides navigation assistance, and shows customer contact information | Pass |
| As a Site Admin, I can access an admin dashboard so that I can manage products, orders, and users efficiently | Log in as an admin and access the admin dashboard | The admin dashboard provides an overview and options to manage all mentioned categories | Pass |
| As a Site Admin, I can create, read, update, and delete products so that I can manage my inventory | Log in as an admin and attempt CRUD operations on products | Full CRUD functionality is available for managing products in the inventory | Pass |


### Feature Testing

| Feature Area | Test Cases |
|--------------|------------|
| Navigation and Footer | 3 |
| Home Page | 5 |
| Product Detail Page | 4 |
| User Authentication | 3 |
| User Profile | 4 |
| Shopping Cart | 4 |
| Checkout Process | 4 |
| Order History | 2 |
| Staff and Courier Dashboards | 2 |
| Responsive Design | 2 |

#### Navigation and Footer

1. Test all navigation links
   - Click each link in the navigation bar
   - Verify that each link leads to the correct page
   - Confirm that the active page is highlighted in the navigation

2. Test responsiveness of navigation
   - Resize browser window to different widths
   - Verify that navigation collapses into a hamburger menu on smaller screens
   - Test functionality of hamburger menu

3. Test footer links and information
   - Click all links in the footer
   - Verify that links open correct pages or external sites in new tabs
   - Confirm that contact information and business hours are displayed correctly

#### Home Page

1. Test product listing
   - Verify that products are displayed in a grid layout
   - Confirm that product images, names, and prices are visible

2. Test pagination
   - Navigate through different pages of products
   - Verify that the correct number of products is displayed per page

3. Test sorting functionality
   - Sort products by different criteria (e.g., price, availability)
   - Confirm that products are reordered correctly

4. Test category filtering
   - Apply different category filters
   - Verify that only products from the selected category are displayed

5. Test search functionality
   - Enter various search terms in the search bar
   - Confirm that search results are relevant and accurate

#### Product Detail Page

1. Test product information display
   - Verify that all product details (name, price, description, availability) are correct

2. Test quantity selector
   - Increase and decrease quantity
   - Verify that quantity cannot go below 1 or above available stock

3. Test "Add to Cart" functionality
   - Add different quantities of the product to the cart
   - Verify that the cart updates correctly

4. Test "Show in Cart" button
   - Add a product to the cart
   - Confirm that the button changes to "Show in Cart"
   - Click the button and verify it leads to the cart page

#### User Authentication

1. Test registration process
   - Complete registration form with valid data
   - Verify that account is created
   - Test form validation for invalid inputs

2. Test login process
   - Log in with valid credentials
   - Attempt login with invalid credentials and verify error messages

3. Test logout process
   - Click logout button
   - Verify that user is logged out and redirected appropriately

#### User Profile

1. Test profile information display
   - Verify that user details are correctly displayed

2. Test profile update functionality
   - Update profile information
   - Confirm that changes are saved and reflected in the profile

3. Test password change
   - Change password using correct current password
   - Attempt to change password with incorrect current password
   - Verify that password is updated successfully

4. Test account deletion
   - Initiate account deletion process
   - Confirm that account is properly deleted and user is logged out

#### Shopping Cart

1. Test add to cart functionality
   - Add various products to the cart
   - Verify that cart icon updates with correct item count

2. Test cart page display
   - Confirm that all added items are listed with correct details

3. Test quantity adjustment in cart
   - Increase and decrease quantities of items
   - Verify that subtotal and total are updated correctly

4. Test remove item from cart
   - Remove items from the cart
   - Confirm that cart updates and reflects the changes

#### Checkout Process

1. Test checkout form
   - Fill out all required fields
   - Test form validation for missing or invalid inputs

2. Test delivery instructions
   - Add, edit, and delete delivery instructions
   - Verify that instructions are saved with the order

3. Test terms and conditions checkbox
   - Attempt to proceed without checking the box
   - Confirm that proceeding is not possible until terms are accepted

4. Test payment processing
   - Enter valid payment details
   - Attempt payment with invalid details
   - Verify that order is created upon successful payment

#### Order History

1. Test order listing
   - Verify that all past orders are displayed
   - Confirm that order details are accurate

2. Test order cancellation
   - Attempt to cancel a recent order
   - Verify that cancellation is processed correctly

#### Staff and Courier Dashboards

1. Test staff order management
   - Update order statuses
   - Assign orders to couriers
   - Verify that changes are reflected in the system

2. Test courier delivery management
   - Update delivery statuses
   - Test navigation to delivery addresses
   - Confirm that updates are saved and visible to customers

#### Responsive Design Testing

1. Test on various devices and screen sizes
   - Use Chrome DevTools to emulate different devices
   - Verify layout and functionality on mobile, tablet, and desktop views

2. Test on different browsers
   - Check functionality and appearance on Chrome, Firefox, Safari, and Edge


### Summary

Manual testing was conducted across all major features and user stories of the Green Local Veggies application. The testing process covered functionality, usability, responsiveness, and cross-browser compatibility. All tests were performed on the following browsers:

| Browser | Version | Result |
|---------|---------|--------|
| Google Chrome | 127.0.6533.120 | Pass |
| Mozilla Firefox | 128.0.3 | Pass |
| Safari | 17.6 | Pass |
| Microsoft Edge | 127.0.2651.105 | Pass |

All features functioned as expected across these browsers, with no bugs or issues detected. The application demonstrated consistent behavior and appearance across different devices and screen sizes.

Key areas tested include:
- User authentication and account management
- Product browsing and searching
- Shopping cart functionality
- Checkout process
- Order management and history
- Staff and courier dashboards
- Responsive design and layout

The manual testing process confirmed that the Green Local Veggies application meets its design specifications and user requirements. The user interface is intuitive and responsive, providing a seamless experience across desktop and mobile devices.


## Automated Testing

Automated testing plays a crucial role in ensuring the reliability and functionality of Green Local Veggies application. I implemented a series of unit tests to verify that individual components of the system work as expected. These tests cover models, forms, and views.

All automated tests have passed successfully, demonstrating the robustness of the codebase. Below, you can find detailed information about each test file, including the purpose of each test and its outcome.

### Shop App Tests

The shop app tests cover the core functionality of the e-commerce platform, including product display, search, filtering, and cart operations. These tests ensure that users can browse products, search for specific items, filter results, and add products to their cart effectively.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_index_view` | Tests the main shop page | Verifies correct template and product display |
| `test_product_details_view` | Tests individual product page | Checks correct template and product information |
| `test_add_to_cart` | Tests adding a product to the cart | Verifies correct JSON response and cart update |
| `test_about_view` | Tests the about page | Ensures correct template is used |
| `test_contact_view` | Tests the contact page | Checks correct template is used |
| `test_search_results` | Tests product search functionality | Verifies correct search results are displayed |
| `test_empty_search` | Tests search with empty query | Ensures all products are displayed |
| `test_category_filter` | Tests filtering products by category | Verifies correct products are displayed for a category |
| `test_price_sorting` | Tests sorting products by price | Checks products are sorted correctly by price |
| `test_availability_filter` | Tests filtering by product availability | Ensures only in-stock items are displayed when filtered |

These tests thoroughly cover the main features of the shop application:

1. **Product Display**: Ensures that the main shop page and individual product pages correctly display product information.

2. **Cart Operations**: Verifies that products can be added to the cart with the correct response and cart update.

3. **Search Functionality**: Tests the search feature to ensure it returns correct results and handles empty queries appropriately.

4. **Filtering and Sorting**: Validates the category filter, price sorting, and availability filter to ensure users can effectively narrow down product selections.

5. **Static Pages**: Checks that informational pages like 'About' and 'Contact' are correctly rendered.

The test suite includes mocking of Cloudinary uploads to simulate image handling without actually uploading files during tests. This approach ensures that tests can run quickly and don't depend on external services.

By covering these key areas, the tests help maintain the reliability and functionality of the core shopping experience, ensuring that users can easily find, view, and select products for purchase.

### Cart App Tests

The cart app tests focus on validating the functionality of the shopping cart, including adding products, updating quantities, removing items, and calculating totals. These tests ensure that the cart behaves correctly under various scenarios.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_add_product_to_cart` | Adds a product to the cart | Verifies the cart length and quantity |
| `test_add_product_exceeding_stock` | Attempts to add a product with quantity exceeding stock | Expects a ValidationError |
| `test_add_out_of_stock_product` | Tries to add an out-of-stock product | Expects a ValidationError |
| `test_update_product_quantity` | Updates the quantity of a product in the cart | Checks if the quantity is updated correctly |
| `test_remove_product_from_cart` | Removes a product from the cart | Verifies the cart is empty after removal |
| `test_get_total_price` | Calculates the total price of the cart | Compares with expected total |
| `test_clear_cart` | Clears all items from the cart | Checks if the cart is empty after clearing |
| `test_get_item_quantity` | Retrieves the quantity of a specific item | Verifies the correct quantity is returned |
| `test_get_items` | Gets all items in the cart | Checks the items' details are correct |
| `test_add_to_cart_view` | Tests the add_to_cart view | Verifies JSON response and cart status |
| `test_add_to_cart_view_invalid_quantity` | Tests add_to_cart view with invalid quantity | Checks for error response |
| `test_update_cart_view` | Tests the update_cart view | Verifies JSON response and updated cart total |
| `test_remove_from_cart_view` | Tests the remove_from_cart view | Checks for correct redirect |
| `test_cart_detail_view` | Tests the cart_detail view | Verifies content of cart detail page |
| `test_cart_detail_view_empty_cart` | Tests cart_detail view with empty cart | Checks for empty cart message |

These tests cover a wide range of scenarios for the cart functionality, ensuring that the cart behaves correctly under various conditions, including edge cases like attempting to add out-of-stock items or exceeding available stock. The tests also validate the cart-related views, checking both successful operations and error handling.

### Delivery Instructions App Tests

The delivery instructions app tests cover the functionality related to creating, updating, deleting, and retrieving delivery instructions. These tests ensure that users can manage their delivery preferences securely and effectively.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_delivery_instruction_creation` | Tests creation of a DeliveryInstruction instance | Verifies correct attributes of created instance |
| `test_delivery_instruction_str_representation` | Tests string representation of DeliveryInstruction | Checks correct string output |
| `test_delivery_instruction_form_valid_data` | Tests DeliveryInstructionForm with valid data | Ensures form validity with correct data |
| `test_delivery_instruction_form_invalid_data` | Tests DeliveryInstructionForm with invalid data | Verifies form invalidity with incorrect data |
| `test_instruction_create_view` | Tests creation of a new DeliveryInstruction via view | Checks successful creation and response |
| `test_instruction_update_view` | Tests updating an existing DeliveryInstruction | Verifies successful update and database reflection |
| `test_instruction_delete_view` | Tests deletion of a DeliveryInstruction | Ensures instruction is removed from database |
| `test_instruction_detail_view` | Tests retrieval of DeliveryInstruction details | Checks correct JSON response with instruction details |

These tests thoroughly cover the delivery instructions functionality, including model operations, form validations, and view behaviors. They ensure that users can create, update, delete, and view their delivery instructions securely.

The test suite includes checks for both valid and invalid data scenarios in form submissions, ensuring robust data validation. View tests cover all CRUD operations (Create, Read, Update, Delete) for delivery instructions, verifying that each operation performs as expected and maintains data integrity.

### Orders App Tests

The orders app tests cover the functionality related to order management, including order creation, order item management, form validation, and various order-related views. These tests ensure that the ordering process works correctly and securely.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_order_creation` | Tests creation of an Order instance | Verifies correct attributes and string representation |
| `test_order_status_choices` | Tests order status choices | Ensures status is a valid choice |
| `test_order_cancel` | Tests order cancellation functionality | Verifies status change and cancellation timestamp |
| `test_order_item_creation` | Tests creation of an OrderItem instance | Checks correct attributes and string representation |
| `test_form_fields` | Tests OrderCreateForm fields | Verifies presence of 'saved_instruction' field |
| `test_checkout_view` | Tests the checkout view | Checks for correct response or redirection |
| `test_order_history_view` | Tests the order history view | Verifies correct template use and response |
| `test_order_detail_view` | Tests the order detail view | Ensures correct template use and response |
| `test_cancel_order_view` | Tests the cancel order view | Verifies order status change and redirection |

These tests thoroughly cover the orders functionality, including model operations, form validations, and view behaviors. They ensure that users can create orders, manage order items, view order history, and cancel orders securely.

The test suite includes checks for both authenticated and unauthenticated user scenarios, ensuring that access controls are properly implemented. It also verifies that order cancellation correctly updates the order status and timestamp.

By testing various aspects of the ordering process, these tests help maintain the integrity and reliability of the e-commerce functionality within the application.

### Customer App Tests

The customer app tests cover the functionality related to customer user management, including user creation, authentication, registration, login, and profile management. These tests ensure that customer-related features work correctly and securely.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_create_user` | Tests creation of a regular user | Verifies user attributes and non-staff status |
| `test_create_superuser` | Tests creation of a superuser | Checks superuser attributes and permissions |
| `test_register_view_GET` | Tests GET request to register view | Verifies correct template and form |
| `test_register_view_POST_valid` | Tests POST request to register with valid data | Checks successful user creation and redirect |
| `test_register_view_POST_invalid` | Tests POST request to register with invalid data | Ensures user is not created with invalid data |
| `test_login_view_GET` | Tests GET request to login view | Verifies correct template and form |
| `test_login_view_POST_valid` | Tests POST request to login with valid credentials | Checks successful login and redirect |
| `test_profile_view_authenticated` | Tests profile view access for authenticated users | Verifies correct template use |
| `test_profile_view_unauthenticated` | Tests profile view access for unauthenticated users | Ensures redirection to login |
| `test_customer_registration_form_valid` | Tests registration form with valid data | Verifies form validity |
| `test_customer_registration_form_passwords_dont_match` | Tests registration form with mismatched passwords | Checks for appropriate form error |
| `test_customer_profile_form_valid` | Tests profile form with valid data | Verifies form validity |
| `test_customer_profile_form_invalid_email` | Tests profile form with invalid email | Checks for appropriate form error |

These tests comprehensively cover the customer-related functionality, including model operations, view behaviors, and form validations. They ensure that users can register, log in, and manage their profiles securely, while also verifying that the system correctly handles both valid and invalid inputs.

The test suite includes checks for both authenticated and unauthenticated user scenarios, ensuring that access controls are properly implemented. Form validation tests cover various scenarios, including password matching and email format validation, to ensure data integrity and user-friendly error handling.

### Staff Dashboard App Tests

The staff dashboard app tests cover the functionality related to the staff-only area of the application. These tests ensure that staff members can effectively manage orders, update order statuses, and assign couriers to orders.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_staff_dashboard_access` | Tests access control for staff dashboard | Verifies staff can access and non-staff are redirected |
| `test_order_list_view` | Tests the order list view in staff dashboard | Checks correct template use and order display |
| `test_order_detail_view` | Tests the order detail view | Verifies correct template and order information display |
| `test_update_order_status` | Tests updating an order's status | Ensures order status is updated correctly |
| `test_filter_orders` | Tests filtering orders by status | Verifies correct filtering of orders |
| `test_assign_courier` | Tests assigning a courier to an order | Checks correct courier assignment and status update |

These tests thoroughly cover the main features of the staff dashboard:

1. **Access Control**: Ensures that only staff members can access the dashboard, while non-staff users are redirected.

2. **Order Management**: Verifies that staff can view lists of orders and access detailed information about each order.

3. **Order Status Updates**: Tests the functionality to update the status of orders, ensuring changes are correctly saved.

4. **Order Filtering**: Validates the ability to filter orders by status, helping staff manage orders more efficiently.

5. **Courier Assignment**: Checks the functionality to assign couriers to orders, an important feature for order fulfillment.

The test suite includes setup methods to create necessary test data, including staff and non-staff users, test products, and orders. This approach ensures a consistent testing environment across all tests in the suite.

By covering these key areas, the tests help maintain the reliability and functionality of the staff dashboard, ensuring that staff members can effectively manage the e-commerce operations. The tests also indirectly validate the security of the application by checking that non-staff users cannot access restricted areas.

### Courier App Tests

The courier app tests focus on validating the functionality related to courier operations, including accessing the courier dashboard, viewing order details, and marking orders as delivered. These tests ensure that courier-specific features work correctly and are properly secured.

| Test Name | Description | Assertion |
|-----------|-------------|-----------|
| `test_courier_dashboard_view` | Tests access to the courier dashboard | Verifies correct template use and context data |
| `test_order_detail_view` | Tests courier access to order details | Checks correct template and order context |
| `test_mark_delivered_view` | Tests marking an order as delivered | Verifies order status update and courier assignment |
| `test_non_courier_access` | Tests non-courier access to courier views | Ensures redirection to login page |

These tests cover the main functionalities of the courier app, ensuring that couriers can access their dashboard, view order details, and mark orders as delivered. The tests also verify that non-courier users are properly restricted from accessing courier-specific views, maintaining the security of the courier operations.

Each test case uses a setup method to create necessary test data, including courier and customer users, and a sample order. This approach ensures a consistent testing environment across all tests in the suite.