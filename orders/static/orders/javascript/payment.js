document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("payment-form");
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
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const stripeForm = document.getElementById("payment-form");
    const checkoutFormButton = document.querySelector("#checkout-form input[type='submit']");

    // Function to toggle visibility of the checkout button
    function toggleCheckoutButtonVisibility() {
        if (stripeForm) {
            if (checkoutFormButton) {
                checkoutFormButton.style.display = 'none';
            }
        } else {
            if (checkoutFormButton) {
                checkoutFormButton.style.display = 'inline-block';
            }
        }
    }

    // Run the function to set initial visibility
    toggleCheckoutButtonVisibility();
});
