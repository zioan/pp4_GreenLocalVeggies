document.addEventListener('DOMContentLoaded', function() {
    // Get references to DOM elements
    const savedInstructionSelect = document.getElementById('id_saved_instruction');
    const editInstructionSelect = document.getElementById('editInstructionSelect');
    const instructionForm = document.getElementById('instructionForm');
    const deleteInstructionBtn = document.getElementById('deleteInstruction');
    const saveInstructionBtn = document.getElementById('saveInstruction');
    const instructionTitleInput = document.getElementById('instructionTitle');
    const instructionTextInput = document.getElementById('instructionText');
    const toggleManageInstructionsBtn = document.getElementById('toggleManageInstructions');
    const manageInstructionsSection = document.getElementById('manageInstructionsSection');
    const deleteConfirmModal = new bootstrap.Modal(document.getElementById('deleteConfirmModal'));
    const confirmDeleteBtn = document.getElementById('confirmDelete');
    const selectedInstructionDisplay = document.getElementById('selectedInstructionDisplay');
    const selectedInstructionText = document.getElementById('selectedInstructionText');
    const checkoutForm = document.getElementById('checkout-form');

    // Create a hidden input field to store the selected instruction ID in the checkout form
    const hiddenInstructionInput = document.createElement('input');
    hiddenInstructionInput.type = 'hidden';
    hiddenInstructionInput.name = 'selected_instruction';
    hiddenInstructionInput.id = 'selected_instruction';
    checkoutForm.appendChild(hiddenInstructionInput);

    // Event handler for changes in the saved instruction dropdown
    savedInstructionSelect.addEventListener('change', function() {
        if (this.value) {
            fetch(`/delivery-instructions/${this.value}/`)
            .then(response => response.json())
            .then(data => {
                selectedInstructionText.textContent = data.instruction;
                selectedInstructionDisplay.style.display = 'block';
                hiddenInstructionInput.value = data.instruction;
            });
        } else {
            clearSelectedInstructionDisplay();
            hiddenInstructionInput.value = '';
        }
    });

    // Event handler for the manage instructions button click
    toggleManageInstructionsBtn.addEventListener('click', function() {
        manageInstructionsSection.style.display = 
            manageInstructionsSection.style.display === 'none' ? 'block' : 'none';
        if (manageInstructionsSection.style.display === 'block') {
            populateEditSelect();
        }
    });

    // Event handler to enable or disable the Place Order button based on checkbox status
    termsCheckbox.addEventListener('change', function() {
        placeOrderBtn.disabled = !this.checked;
    });

    // Event handler for the Place Order button click. Hides the delivery instructions card and shows the payment form.
    placeOrderBtn.addEventListener('click', function() {
        const deliveryInstructionsCard = document.querySelector('.delivery-instructions-card');
        if (deliveryInstructionsCard) {
            deliveryInstructionsCard.style.display = 'none';
        }

        // Show the Stripe payment form
        const paymentForm = document.getElementById('payment-form');
        if (paymentForm) {
            paymentForm.style.display = 'block';
        }
    });

    /**
     * Populates the edit instruction dropdown with options from the saved instructions dropdown.
     */
    function populateEditSelect() {
        editInstructionSelect.innerHTML = '<option value="">Choose an instruction or add new</option>';
        Array.from(savedInstructionSelect.options).forEach(option => {
            if (option.value) {
                const newOption = new Option(option.text, option.value);
                editInstructionSelect.add(newOption);
            }
        });
    }

    // Event handler for changes in the edit instruction dropdow.Fetches and displays the details of the selected instruction for editing.
    editInstructionSelect.addEventListener('change', function() {
        if (this.value) {
            fetch(`/delivery-instructions/${this.value}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('instructionAction').value = 'update';
                document.getElementById('instructionId').value = data.id;
                instructionTitleInput.value = data.title;
                instructionTextInput.value = data.instruction;
                deleteInstructionBtn.style.display = 'block';
                updateSaveButtonState();
            });
        } else {
            resetForm();
        }
    });

    /**
     * Resets the form fields and button states to their default values.
     */
    function resetForm() {
        document.getElementById('instructionAction').value = 'add';
        document.getElementById('instructionId').value = '';
        instructionTitleInput.value = '';
        instructionTextInput.value = '';
        deleteInstructionBtn.style.display = 'none';
        updateSaveButtonState();
    }

    /**
     * Updates the state of the save button based on the input field values.
     */
    function updateSaveButtonState() {
        saveInstructionBtn.disabled = !(instructionTitleInput.value.trim() && instructionTextInput.value.trim());
    }

    // Event listeners for input fields to update save button state
    instructionTitleInput.addEventListener('input', updateSaveButtonState);
    instructionTextInput.addEventListener('input', updateSaveButtonState);

    // Event handler for the form submission (add/update instruction). Sends the form data to the server and updates the dropdowns based on the response.
    instructionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const action = formData.get('action');
        const url = action === 'add' ? '/delivery-instructions/create/' : `/delivery-instructions/${formData.get('instruction_id')}/update/`;

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                if (action === 'add') {
                    const option = new Option(data.title, data.id);
                    savedInstructionSelect.add(option);
                    editInstructionSelect.add(new Option(data.title, data.id));
                } else {
                    const option = savedInstructionSelect.querySelector(`option[value="${data.id}"]`);
                    const editOption = editInstructionSelect.querySelector(`option[value="${data.id}"]`);
                    if (option) option.text = data.title;
                    if (editOption) editOption.text = data.title;
                }
                savedInstructionSelect.value = data.id;
                savedInstructionSelect.dispatchEvent(new Event('change'));
                resetForm();
                manageInstructionsSection.style.display = 'none';
                showToast(data.message, 'success');
            } else {
                showToast(data.message, 'error');
            }
        });
    });

    // Event handler for the delete instruction button click.Shows the confirmation modal for deletion.
    deleteInstructionBtn.addEventListener('click', function() {
        deleteConfirmModal.show();
    });

    // Event handler for confirming instruction deletion. Sends a delete request to the server and updates the dropdowns based on the response.
    confirmDeleteBtn.addEventListener('click', function() {
        const id = document.getElementById('instructionId').value;
        fetch(`/delivery-instructions/${id}/delete/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Remove the option from both select elements
                removeOptionFromSelect(savedInstructionSelect, id);
                removeOptionFromSelect(editInstructionSelect, id);

                // Clear the selection and hide the display
                savedInstructionSelect.value = '';
                clearSelectedInstructionDisplay();

                resetForm();
                deleteConfirmModal.hide();
                showToast(data.message, 'success');

                // Refresh the edit select options
                populateEditSelect();
            } else {
                showToast(data.message, 'error');
            }
        });
    });

    /**
     * Removes an option from a select element based on its value.
     * @param {HTMLElement} selectElement - The select element to remove the option from.
     * @param {string} value - The value of the option to remove.
     */
    function removeOptionFromSelect(selectElement, value) {
        const option = selectElement.querySelector(`option[value="${value}"]`);
        if (option) {
            option.remove();
        }
    }

    /**
     * Clears the selected instruction display and resets the hidden input.
     */
    function clearSelectedInstructionDisplay() {
        selectedInstructionText.textContent = '';
        selectedInstructionDisplay.style.display = 'none';
        hiddenInstructionInput.value = '';
    }

    // Initial call to set correct button states
    updateSaveButtonState();

    // Initial call to display instruction if one is pre-selected
    if (savedInstructionSelect.value) {
        savedInstructionSelect.dispatchEvent(new Event('change'));
    }
});
