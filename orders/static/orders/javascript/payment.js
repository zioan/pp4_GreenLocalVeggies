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
