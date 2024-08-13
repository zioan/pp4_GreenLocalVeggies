document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("payment-form");
    const deliveryInstructionsSection = document.getElementById("delivery-instructions-section");
    if (form) {
        const stripePublishableKey = form.dataset.stripePublishableKey;
        const clientSecret = form.dataset.clientSecret;
        const returnUrl = form.dataset.returnUrl;

        const stripe = Stripe(stripePublishableKey);

        const elements = stripe.elements({
            clientSecret: clientSecret,
        });

        const paymentElement = elements.create("payment");

        paymentElement.mount("#payment-element");

        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            const { error } = await stripe.confirmPayment({
                elements,
                confirmParams: {
                    return_url: returnUrl,
                },
            });

            if (error) {
                const messageContainer = document.querySelector("#payment-message");
                messageContainer.textContent = error.message;
                messageContainer.classList.remove("hidden");
            } else {
                // Redirect to post-payment page
                window.location.href = '/orders/post-payment-redirect/';
            }
        });

    }
});

document.addEventListener("DOMContentLoaded", function() {
    const stripeForm = document.getElementById("payment-form");
    const checkoutForm = document.getElementById('checkout-form');
    const deliveryInstructionsSection = document.getElementById("delivery-instructions-section");

    // Function to toggle visibility of the checkout button and hide delivery instructions
    function toggleCheckoutButtonVisibility() {
        if (stripeForm) {
            if (checkoutForm) {
                checkoutForm.style.display = 'none';
            }
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'none';
            }
        } else {
            if (checkoutForm) {
                checkoutForm.style.display = 'inline-block';
            }
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'block';
            }
        }
    }

    // Run the function to set initial visibility
    toggleCheckoutButtonVisibility();
});

document.addEventListener('DOMContentLoaded', function () {
    function checkCartAndRedirect() {
        const cartTotal = document.getElementById('cart-total');
        if (cartTotal && parseFloat(cartTotal.textContent) === 0) {
            window.location.href = '/cart/';
        }
    }

    checkCartAndRedirect();

    document.addEventListener('visibilitychange', function () {
        if (!document.hidden) {
            checkCartAndRedirect();
        }
    });

    window.history.pushState(null, "", window.location.href);
    window.onpopstate = function () {
        checkCartAndRedirect();
        window.history.pushState(null, "", window.location.href);
    };
});