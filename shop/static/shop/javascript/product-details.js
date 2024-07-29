document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity');
    const addToCartButton = document.querySelector('button[type="submit"]');
    const maxStock = parseFloat(quantityInput.max);
    const minQuantity = parseFloat(quantityInput.min);

    quantityInput.addEventListener('input', function() {
        const quantity = parseFloat(this.value);
        if (isNaN(quantity) || quantity < minQuantity || quantity > maxStock) {
            addToCartButton.disabled = true;
        } else {
            addToCartButton.disabled = false;
        }
    });

    //Dynamically update price based on quantity
    const priceElement = document.getElementById('product-price');
    const basePrice = parseFloat(priceElement.dataset.basePrice);

    quantityInput.addEventListener('input', function() {
        const quantity = parseFloat(this.value) || 0;
        const totalPrice = (basePrice * quantity).toFixed(2);
        priceElement.textContent = `€ ${totalPrice}`;
    });
});