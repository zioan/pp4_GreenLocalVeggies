function showToast(message, type = "info") {
    const toastEl = document.getElementById("liveToast");
    const toastMessage = toastEl.querySelector("#toast-message");
    toastMessage.textContent = message;
    toastEl.classList.remove(
        "bg-success",
        "bg-danger",
        "bg-warning",
        "bg-info"
    );
    toastEl.classList.add(`bg-${type}`, "text-white");
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
}
