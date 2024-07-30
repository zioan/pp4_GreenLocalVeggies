document.addEventListener('DOMContentLoaded', function() {
    const addToCartForms = document.querySelectorAll('.add-to-cart-form');

    addToCartForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const productId = this.querySelector('button[type="submit"]').getAttribute('data-product-id');
            
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
                    document.querySelectorAll('#cart-count').forEach(el => {
                        el.textContent = data.cart_count;
                    });
                    // alert(data.message);
                    
                    // Update add-to-cart buttons when product is added to cart
                    document.querySelectorAll(`button[data-product-id="${productId}"]`).forEach(button => {
                        button.innerHTML = '<i class="fas fa-check"></i> In Cart';
                        button.classList.remove('btn-primary');
                        button.classList.add('btn-success');
                    });
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    });
});