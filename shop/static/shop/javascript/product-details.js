document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity');
    const totalPriceSpan = document.getElementById('total-price');
    const basePrice = parseFloat(document.getElementById('product-price').dataset.basePrice);

    quantityInput.addEventListener('change', function() {
        const quantity = parseInt(this.value);
        const total = (basePrice * quantity).toFixed(2);
        totalPriceSpan.textContent = total;
    });
});
