document.addEventListener('DOMContentLoaded', function() {
    const statusSelect = document.getElementById('status');
    const courierSelect = document.getElementById('courier');

    /**
     * Updates the courier dropdown based on the selected status.
     * Disables the courier dropdown if the status is 'pending' or 'processing'.
     * Clears the courier dropdown value if it is disabled.
     */
    function updateCourierDropdown() {
        const selectedStatus = statusSelect.value;
        const disableDropdown = ['pending', 'processing'].includes(selectedStatus);
        courierSelect.disabled = disableDropdown;
        if (disableDropdown) {
            // Clear selected value when disabled
            courierSelect.value = '';
        }
    }

    // Event listener for status dropdown change to update courier dropdown
    statusSelect.addEventListener('change', updateCourierDropdown);

    // Initial update to set the correct state of the courier dropdown
    updateCourierDropdown();
});
