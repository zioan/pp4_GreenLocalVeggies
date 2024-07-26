// Save the active tab in the profile template to sessionStorage.
// This way, when the page is reloaded, or a form action trigger 
// a rerender, the active tab will remain active.

document.addEventListener("DOMContentLoaded", function () {
    // Get the saved tab from sessionStorage
    let activeTab = sessionStorage.getItem('activeTab');

    // If there's a saved tab, activate it
    if (activeTab) {
        let tab = new bootstrap.Tab(document.querySelector(`a[href="${activeTab}"]`));
        tab.show();
    }

    // Add click event listener to all nav-link elements
    document.querySelectorAll('.nav-link').forEach(function (tab) {
        tab.addEventListener('click', function (event) {
            // Save the current tab identifier
            sessionStorage.setItem('activeTab', event.target.getAttribute('href'));
        });
    });
});