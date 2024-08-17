document.addEventListener('DOMContentLoaded', function() {
    // Select necessary DOM elements for handling quantity and pricing
    const quantityContainer = document.querySelector('.quantity-container');
    const quantityInput = document.getElementById('quantity');
    const totalPriceSpan = document.getElementById('total-price');
    const basePrice = parseFloat(document.getElementById('product-price').dataset.basePrice);
    const decreaseBtn = quantityContainer.querySelector('.quantity-decrease');
    const increaseBtn = quantityContainer.querySelector('.quantity-increase');
    const addToCartForm = document.querySelector('.add-to-cart-form');
    const addToCartBtn = addToCartForm.querySelector('button[type="submit"]');

    /**
     * Updates the total price displayed on the page based on the current quantity.
     */
    function updateTotalPrice() {
        const quantity = parseInt(quantityInput.value);
        const total = (basePrice * quantity).toFixed(2);
        totalPriceSpan.textContent = total;
    }

    /**
     * Changes the quantity of the product and updates the total price accordingly.
     * 
     * @param {number} change - The amount to change the quantity by (+1 or -1).
     */
    function changeQuantity(change) {
        let newValue = parseInt(quantityInput.value) + change;
        // Ensure the new quantity is within allowed bounds ()
        if (newValue >= parseInt(quantityInput.min) && newValue <= parseInt(quantityInput.max)) {
            quantityInput.value = newValue;
            updateTotalPrice();
        }
    }

    /**
     * Updates the UI after a product has been successfully added to the cart.
     * 
     * @param {Object} data - The response data from the server after adding to the cart.
     */
    function updateUIAfterAddToCart(data) {
        // Disable quantity controls to prevent further changes
        decreaseBtn.disabled = true;
        increaseBtn.disabled = true;
        quantityInput.disabled = true;

        // Update the "Add to Cart" button to indicate the product is in the cart
        addToCartBtn.innerHTML = '<i class="fas fa-check"></i> Show in Cart';
        addToCartBtn.classList.replace('btn-primary', 'btn-success');
        addToCartBtn.type = 'button';
        addToCartBtn.onclick = () => window.location.href = '/cart/';

        // Update the displayed quantity if more of the product was added
        const newQuantity = parseInt(quantityInput.value) + (data.cart_quantity || 0);
        quantityInput.value = newQuantity;

        updateTotalPrice();

        // Update the cart count in the UI if the element is present
        const cartCountElement = document.querySelector('.cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = data.cart_count;
        }

        showMessage(data.message, 'success');
    }

    /**
     * Displays a message to the user, either using a toast or an alert.
     * This functions is made with reusability in mind.
     * 
     * @param {string} message - The message to display.
     * @param {string} type - The type of message ('success', 'error', etc.).
     */
    function showMessage(message, type) {
        // Use the toast if available, otherwise fallback to a simple alert
        if (typeof showToast === 'function') {
            showToast(message, type);
        } else {
            alert(message);
        }
    }

    // Event listeners for increasing or decreasing the quantity
    decreaseBtn.addEventListener('click', () => changeQuantity(-1));
    increaseBtn.addEventListener('click', () => changeQuantity(1));

    // Initial update of the total price when the page loads/refreshes
    updateTotalPrice();

    // Handle the add-to-cart form submission via AJAX
    addToCartForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Send the form data via AJAX to the server
        fetch(this.action, {
            method: 'POST',
            body: new FormData(this),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': this.querySelector('[name=csrfmiddlewaretoken]').value,
            },
        })
        .then(response => response.json())
        .then(data => {
            // Check if the server returned a success status
            if (data.status === 'success') {
                updateUIAfterAddToCart(data);
            } else {
                showMessage(data.message, 'error');
            }
        })
        .catch(error => {
            // Handle any errors during the fetch
            console.error('Error:', error);
            showMessage('An error occurred. Please try again.', 'error');
        });
    });
});
