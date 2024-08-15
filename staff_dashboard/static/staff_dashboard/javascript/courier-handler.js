document.addEventListener('DOMContentLoaded', function() {
    const statusSelect = document.getElementById('status');
    const courierSelect = document.getElementById('courier');

    function updateCourierDropdown() {
        const selectedStatus = statusSelect.value;
        const disableDropdown = ['pending', 'processing'].includes(selectedStatus);
        courierSelect.disabled = disableDropdown;
        if (disableDropdown) {
            courierSelect.value = '';
        }
    }

    statusSelect.addEventListener('change', updateCourierDropdown);
    updateCourierDropdown();
});