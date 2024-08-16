// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Select all quantity container elements
    const quantityContainers = document.querySelectorAll('.quantity-container');

    // Iterate over each quantity container
    quantityContainers.forEach(container => {
        // Get the input and button elements for this container
        const input = container.querySelector('.quantity-input');
        const decreaseBtn = container.querySelector('.quantity-decrease');
        const increaseBtn = container.querySelector('.quantity-increase');

        // Add click event listeners to the decrease and increase buttons
        decreaseBtn.addEventListener('click', () => changeQuantity(input, -1));
        increaseBtn.addEventListener('click', () => changeQuantity(input, 1));
    });
});

/**
 * Changes the quantity value and updates the cart if within allowed range.
 * @param {HTMLInputElement} input - The quantity input element.
 * @param {number} change - The amount to change the quantity by.
 */
function changeQuantity(input, change) {
    let newValue = parseInt(input.value) + change;
    // Check if the new value is within the allowed range
    if (newValue >= parseInt(input.min) && newValue <= parseInt(input.max)) {
        input.value = newValue;
        updateQuantity(input);
    }
}

/**
 * Updates the quantity in the cart.
 * @param {HTMLInputElement} input - The quantity input element.
 */
function updateQuantity(input) {
    const productId = input.getAttribute('data-product-id');
    const quantity = input.value;
    const cartItem = input.closest('.cart-item');

    updateCart(productId, quantity, cartItem);
}

/**
 * Sends an AJAX request to update the cart and updates the UI.
 * @param {string} productId - The ID of the product to update.
 * @param {string} quantity - The new quantity of the product.
 * @param {HTMLElement} cartItem - The cart item element to update.
 */
function updateCart(productId, quantity, cartItem) {
    // Get the CSRF token for the request
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send a POST request to update the cart
    fetch(`/cart/update/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `quantity=${quantity}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Update the cart total
            document.getElementById('cart-total').textContent = data.cart_total;
            // Calculate and update the new item total
            const priceElement = cartItem.querySelector('.text-end.nowrap p:first-child');
            const pricePerUnit = parseFloat(priceElement.textContent.replace('€', '').trim());
            const newTotal = (quantity * pricePerUnit).toFixed(2);
            cartItem.querySelector('.item-total').textContent = newTotal;
        }
    })
    .catch(error => console.error('Error:', error));
}