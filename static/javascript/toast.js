/**
 * Displays a toast notification with the given message and type.
 * 
 * @param {string} message - The message to display in the toast.
 * @param {string} [type="info"] - The type of the toast, which determines its color.
 */
function showToast(message, type = "info") {
    // Get the toast element and the message container
    const toastEl = document.getElementById("liveToast");
    const toastMessage = toastEl.querySelector("#toast-message");
    
    // Set the message text
    toastMessage.textContent = message;
    
    // Remove existing background color classes
    toastEl.classList.remove(
        "bg-success",
        "bg-danger",
        "bg-warning",
        "bg-info"
    );
    
    // Map Django message types to Bootstrap classes
    const typeMap = {
        'success': 'success',
        'error': 'danger',
        'warning': 'warning',
        'info': 'info'
    };
    
    // Get the correct Bootstrap class
    const bsType = typeMap[type] || type;
    
    // Add the class corresponding to the toast type
    toastEl.classList.add(`bg-${bsType}`, "text-white");
    
    // Create and show the toast
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
}
