document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    
    quantityInputs.forEach(input => {
        const container = input.closest('.quantity-container');
        container.setAttribute('data-unit', input.getAttribute('data-unit'));

        input.addEventListener('change', function() {
            const productId = this.getAttribute('data-product-id');
            const quantity = this.value;
            const row = this.closest('tr');

            updateCart(productId, quantity, row);
        });
    });
});

function updateCart(productId, quantity, row) {
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
            const pricePerUnit = parseFloat(row.querySelector('td:nth-child(3)').textContent.substring(1));
            const newTotal = (quantity * pricePerUnit).toFixed(2);
            row.querySelector('.item-total').textContent = '€' + newTotal;
        }
    })
    .catch(error => console.error('Error:', error));
}