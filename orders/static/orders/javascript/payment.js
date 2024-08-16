document.addEventListener("DOMContentLoaded", function () {
    // Retrieve the payment form and related sections from the DOM
    const form = document.getElementById("payment-form");

    // Check if the payment form exists
    if (form) {
        const stripePublishableKey = form.dataset.stripePublishableKey;
        const clientSecret = form.dataset.clientSecret;
        const returnUrl = form.dataset.returnUrl;

        const stripe = Stripe(stripePublishableKey);

        const elements = stripe.elements({ clientSecret });

        // Create and mount the payment element to the form
        const paymentElement = elements.create("payment");
        paymentElement.mount("#payment-element");

        // Handle form submission
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            // Confirm the payment with Stripe
            const { error } = await stripe.confirmPayment({
                elements,
                confirmParams: {
                    // Redirect URL after payment confirmation
                    return_url: returnUrl,
                },
            });

            // Display error message if payment fails
            if (error) {
                const messageContainer = document.querySelector("#payment-message");
                messageContainer.textContent = error.message;
                messageContainer.classList.remove("hidden");
            } else {
                // Redirect to the post-payment page if payment is successful
                window.location.href = '/orders/post-payment-redirect/';
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Retrieve the payment form, checkout form, and delivery instructions section from the DOM
    const stripeForm = document.getElementById("payment-form");
    const checkoutForm = document.getElementById('checkout-form');
    const deliveryInstructionsSection = document.getElementById("delivery-instructions-section");

    /**
     * Toggle visibility of the checkout button and delivery instructions section
     * based on the presence of the payment form.
     */
    function toggleCheckoutButtonVisibility() {
        if (stripeForm) {
            // Hide checkout form and delivery instructions if payment form is present
            if (checkoutForm) {
                checkoutForm.style.display = 'none';
            }
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'none';
            }
        } else {
            // Show checkout form and delivery instructions if payment form is hidden
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
    /**
     * Check if the cart total is zero and redirect to the cart page if true.
     */
    function checkCartAndRedirect() {
        const cartTotal = document.getElementById('cart-total');
        if (cartTotal && parseFloat(cartTotal.textContent) === 0) {
            window.location.href = '/cart/';
        }
    }

    // Perform initial cart check and redirect if needed
    checkCartAndRedirect();

    // Recheck cart status when the document becomes visible
    document.addEventListener('visibilitychange', function () {
        if (!document.hidden) {
            checkCartAndRedirect();
        }
    });

    // Ensure cart check on browser navigation
    // This prevents the user from navigating back to the payment page after completing the order
    window.history.pushState(null, "", window.location.href);
    window.onpopstate = function () {
        checkCartAndRedirect();
        window.history.pushState(null, "", window.location.href);
    };
});
