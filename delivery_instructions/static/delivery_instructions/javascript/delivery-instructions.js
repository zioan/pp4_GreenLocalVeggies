document.addEventListener('DOMContentLoaded', function() {
    const savedInstructionSelect = document.getElementById('id_saved_instruction');
    const deliveryInstructionTextarea = document.getElementById('id_delivery_instruction');
    const saveInstructionCheckbox = document.getElementById('save_instruction');
    const newInstructionTitleDiv = document.getElementById('new_instruction_title');

    savedInstructionSelect.addEventListener('change', function() {
        const selectedOption = this.options[this.selectedIndex];
        if (selectedOption.value) {
            deliveryInstructionTextarea.value = selectedOption.text;
            deliveryInstructionTextarea.disabled = true;
            saveInstructionCheckbox.checked = false;
            newInstructionTitleDiv.style.display = 'none';
        } else {
            deliveryInstructionTextarea.value = '';
            deliveryInstructionTextarea.disabled = false;
        }
    });

    saveInstructionCheckbox.addEventListener('change', function() {
        newInstructionTitleDiv.style.display = this.checked ? 'block' : 'none';
    });

    deliveryInstructionTextarea.addEventListener('input', function() {
        if (this.value.trim() !== '') {
            savedInstructionSelect.value = '';
            this.disabled = false;
        }
    });
});