document.addEventListener('DOMContentLoaded', function() {
    const addToCartForms = document.querySelectorAll('.add-to-cart-form');

    addToCartForms.forEach(form => {
        const button = form.querySelector('button[type="submit"]') || form.querySelector('button');
        
        if (button) {
            // Check if the product is already in the cart
            if (button.classList.contains('btn-success')) {
                button.type = 'button';
                button.addEventListener('click', redirectToCart);
            } else {
                form.addEventListener('submit', handleAddToCart);
            }
        } else {
            return;
        }
    });

    function handleAddToCart(e) {
        e.preventDefault();
        
        const form = e.target;
        const button = form.querySelector('button[type="submit"]') || form.querySelector('button');

        const productId = button.getAttribute('data-product-id');
        
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateCartCount(data.cart_count);
                updateAddToCartButton(productId);
                showToast(data.message, 'success');
                // alert(data.message);
            } else {
                showToast(data.message, 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showToast('An error occurred. Please try again.', 'danger');
        });
    }

    function updateCartCount(count) {
        document.querySelectorAll('.cart-count').forEach(el => {
            el.textContent = count;
        });
    }

    function updateAddToCartButton(productId) {
        document.querySelectorAll(`button.btn-primary[data-product-id="${productId}"]`).forEach(button => {
            button.innerHTML = '<i class="fas fa-check"></i> Show in Cart';
            button.classList.remove('btn-primary');
            button.classList.add('btn-success');
            button.type = 'button';
            button.removeEventListener('click', handleAddToCart);
            button.addEventListener('click', redirectToCart);
        });
    }

    function redirectToCart() {
        window.location.href = '/cart/';
    }
});