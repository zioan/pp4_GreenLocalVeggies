document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity');
    const totalPriceSpan = document.getElementById('total-price');
    const basePrice = parseFloat(document.getElementById('product-price').dataset.basePrice);
    const decreaseBtn = document.querySelector('.quantity-decrease');
    const increaseBtn = document.querySelector('.quantity-increase');

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

    decreaseBtn.addEventListener('click', () => changeQuantity(-1));
    increaseBtn.addEventListener('click', () => changeQuantity(1));

    // Initial update
    updateTotalPrice();
});