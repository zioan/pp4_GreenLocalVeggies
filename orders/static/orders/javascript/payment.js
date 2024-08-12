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

            // Hide the delivery instructions section
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'none';
            }

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
                
                // Show the delivery instructions section again if there's an error
                if (deliveryInstructionsSection) {
                    deliveryInstructionsSection.style.display = 'block';
                }
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const stripeForm = document.getElementById("payment-form");
    const checkoutFormButton = document.querySelector("#checkout-form input[type='submit']");
    const deliveryInstructionsSection = document.getElementById("delivery-instructions-section");

    // Function to toggle visibility of the checkout button and hide delivery instructions
    function toggleCheckoutButtonVisibility() {
        if (stripeForm) {
            if (checkoutFormButton) {
                checkoutFormButton.style.display = 'none';
            }
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'none';
            }
        } else {
            if (checkoutFormButton) {
                checkoutFormButton.style.display = 'inline-block';
            }
            if (deliveryInstructionsSection) {
                deliveryInstructionsSection.style.display = 'block';
            }
        }
    }

    // Run the function to set initial visibility
    toggleCheckoutButtonVisibility();
});
