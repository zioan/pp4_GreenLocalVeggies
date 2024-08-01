document.addEventListener('DOMContentLoaded', function() {
    const quantityContainers = document.querySelectorAll('.quantity-container');

    quantityContainers.forEach(container => {
        const input = container.querySelector('.quantity-input');
        const decreaseBtn = container.querySelector('.quantity-decrease');
        const increaseBtn = container.querySelector('.quantity-increase');

        decreaseBtn.addEventListener('click', () => changeQuantity(input, -1));
        increaseBtn.addEventListener('click', () => changeQuantity(input, 1));
    });
});

function changeQuantity(input, change) {
    let newValue = parseInt(input.value) + change;
    if (newValue >= parseInt(input.min) && newValue <= parseInt(input.max)) {
        input.value = newValue;
        updateQuantity(input);
    }
}

function updateQuantity(input) {
    const productId = input.getAttribute('data-product-id');
    const quantity = input.value;
    const cartItem = input.closest('.cart-item');

    updateCart(productId, quantity, cartItem);
}

function updateCart(productId, quantity, cartItem) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

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
            document.getElementById('cart-total').textContent = data.cart_total;
            const priceElement = cartItem.querySelector('.text-end.nowrap p:first-child');
            const pricePerUnit = parseFloat(priceElement.textContent.replace('€', '').trim());
            const newTotal = (quantity * pricePerUnit).toFixed(2);
            cartItem.querySelector('.item-total').textContent = newTotal;
        }
    })
    .catch(error => console.error('Error:', error));
}