// Save the active tab in the profile template to sessionStorage.
// This way, when the page is reloaded, or a form action triggers
// a rerender, the active tab will remain active.
document.addEventListener("DOMContentLoaded", function () {
    // Get the saved tab from sessionStorage
    let activeTab = sessionStorage.getItem("activeTab");

    // If there's a saved tab, activate it
    if (activeTab) {
        let tabElement = document.querySelector(`a[href="${activeTab}"]`);
        if (tabElement) {
            let tab = new bootstrap.Tab(tabElement);
            tab.show();
        } else {
            return;
        }
    }

    // Add click event listener to all tab-link elements
    document.querySelectorAll(".tab-link").forEach(function (tab) {
        tab.addEventListener("click", function (event) {
            // Save the current tab identifier
            sessionStorage.setItem(
                "activeTab",
                event.target.getAttribute("href")
            );
        });
    });

    // Handle redirection to the profile tab when the cancel button in account delete tab is clicked
    const cancelDeleteButton = document.getElementById("cancel-account-delete-button");
    if (cancelDeleteButton) {
        cancelDeleteButton.addEventListener("click", function (event) {
            event.preventDefault();

            // Set the active tab to "My Profile"
            sessionStorage.setItem("activeTab", "#v-pills-profile");

            // Redirect to the profile tab
            window.location.href = event.target.href;
        });
    }
});

// Handle the account deletion confirmation modal
document.addEventListener("DOMContentLoaded", function () {
    const deleteForm = document.getElementById("delete-account-form");
    const confirmDeleteBtn = document.getElementById("confirm-delete");

    if (deleteForm && confirmDeleteBtn) {
    confirmDeleteBtn.addEventListener("click", function () {
        deleteForm.submit();
    });
    }
});
