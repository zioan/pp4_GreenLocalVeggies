document.addEventListener('DOMContentLoaded', function() {
    const addToCartForms = document.querySelectorAll('.add-to-cart-form');

    addToCartForms.forEach(form => {
        const button = form.querySelector('button[type="submit"]') || form.querySelector('button');
        
        if (button) {
            // Check if the button has the 'btn-success' class indicating the product is already in the cart
            if (button.classList.contains('btn-success')) {
                button.type = 'button';
                button.addEventListener('click', redirectToCart);
            } else {
                form.addEventListener('submit', handleAddToCart);
            }
        } else {
            return;
        }
    });

    /**
     * Handles the form submission for adding a product to the cart.
     * 
     * @param {Event} e - The submit event object
     */
    function handleAddToCart(e) {
        e.preventDefault();
        
        const form = e.target;
        const button = form.querySelector('button[type="submit"]') || form.querySelector('button');
        const productId = button.getAttribute('data-product-id');
        
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateCartCount(data.cart_count);
                updateAddToCartButton(productId);
                showToast(data.message, 'success');
            } else {
                showToast(data.message, 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showToast('An error occurred. Please try again.', 'danger');
        });
    }

    /**
     * Updates the cart count displayed on the page.
     * 
     * @param {number} count - The new cart item count
     */
    function updateCartCount(count) {
        document.querySelectorAll('.cart-count').forEach(el => {
            el.textContent = count;
        });
    }

    /**
     * Updates the add-to-cart button to show that the product is in the cart.
     * 
     * @param {string} productId - The ID of the product that was added to the cart
     */
    function updateAddToCartButton(productId) {
        document.querySelectorAll(`button.btn-primary[data-product-id="${productId}"]`).forEach(button => {
            button.innerHTML = '<i class="fas fa-check"></i> Show in Cart';
            button.classList.remove('btn-primary');
            button.classList.add('btn-success');
            button.type = 'button';
            button.removeEventListener('click', handleAddToCart);
            button.addEventListener('click', redirectToCart);
        });
    }

    /**
     * Redirects the user to the cart page.
     */
    function redirectToCart() {
        window.location.href = '/cart/';
    }
});
