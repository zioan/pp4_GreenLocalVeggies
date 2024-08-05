document.addEventListener('DOMContentLoaded', function() {
    const quantityContainer = document.querySelector('.quantity-container');
    const quantityInput = document.getElementById('quantity');
    const totalPriceSpan = document.getElementById('total-price');
    const basePrice = parseFloat(document.getElementById('product-price').dataset.basePrice);
    const decreaseBtn = quantityContainer.querySelector('.quantity-decrease');
    const increaseBtn = quantityContainer.querySelector('.quantity-increase');
    const addToCartForm = document.querySelector('.add-to-cart-form');
    const addToCartBtn = addToCartForm.querySelector('button[type="submit"]');

    function updateTotalPrice() {
        const quantity = parseInt(quantityInput.value);
        const total = (basePrice * quantity).toFixed(2);
        totalPriceSpan.textContent = total;
    }

    function changeQuantity(change) {
        let newValue = parseInt(quantityInput.value) + change;
        if (newValue >= parseInt(quantityInput.min) && newValue <= parseInt(quantityInput.max)) {
            quantityInput.value = newValue;
            updateTotalPrice();
        }
    }

    function updateUIAfterAddToCart(data) {
        decreaseBtn.disabled = true;
        increaseBtn.disabled = true;
        quantityInput.disabled = true;

        addToCartBtn.innerHTML = '<i class="fas fa-check"></i> Show in Cart';
        addToCartBtn.classList.replace('btn-primary', 'btn-success');
        addToCartBtn.type = 'button';
        addToCartBtn.onclick = () => window.location.href = '/cart/';

        const newQuantity = parseInt(quantityInput.value) + (data.cart_quantity || 0);
        quantityInput.value = newQuantity;

        updateTotalPrice();

        const cartCountElement = document.querySelector('.cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = data.cart_count;
        }

        showMessage(data.message, 'success');
    }

    function showMessage(message, type) {
        if (typeof showToast === 'function') {
            showToast(message, type);
        } else {
            alert(message);
        }
    }

    decreaseBtn.addEventListener('click', () => changeQuantity(-1));
    increaseBtn.addEventListener('click', () => changeQuantity(1));

     // Initial update
    updateTotalPrice();

    addToCartForm.addEventListener('submit', function(e) {
        e.preventDefault();
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
            if (data.status === 'success') {
                updateUIAfterAddToCart(data);
            } else {
                showMessage(data.message, 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showMessage('An error occurred. Please try again.', 'error');
        });
    });
});