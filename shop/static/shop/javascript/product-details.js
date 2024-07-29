document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity');
    const addToCartButton = document.querySelector('button[type="submit"]');
    const totalPriceElement = document.getElementById('total-price');
    const maxStock = parseFloat(quantityInput.max);
    const minQuantity = parseFloat(quantityInput.min);
    const basePrice = parseFloat(document.getElementById('product-price').dataset.basePrice);

    function updatePrice() {
        const quantity = parseFloat(quantityInput.value) || 0;
        const totalPrice = (basePrice * quantity).toFixed(2);
        totalPriceElement.textContent = totalPrice;
    }

    function validateQuantity() {
        const quantity = parseFloat(quantityInput.value);
        addToCartButton.disabled = isNaN(quantity) || quantity < minQuantity || quantity > maxStock;
    }

    // Initial validation (price is pre-calculated in the template)
    validateQuantity();

    quantityInput.addEventListener('input', function() {
        updatePrice();
        validateQuantity();
    });
});