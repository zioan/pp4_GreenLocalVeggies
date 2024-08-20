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
