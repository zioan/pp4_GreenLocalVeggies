from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import DeliveryInstruction
from .forms import DeliveryInstructionForm


@login_required
@require_POST
def instruction_create(request):
    """
    Create a new delivery instruction.

    This view handles POST requests to create a new delivery instruction.
    The instruction is associated with the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object containing form data.

    Returns:
        JsonResponse: A JSON response with the status and message, and the
                      created instruction's ID and title if successful.
    """
    form = DeliveryInstructionForm(request.POST)
    if form.is_valid():
        instruction = form.save(commit=False)
        instruction.user = request.user
        instruction.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Instruction created successfully',
            'id': instruction.id,
            'title': instruction.title
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid form data'})


@login_required
@require_POST
def instruction_update(request, pk):
    """
    Update an existing delivery instruction.

    This view handles POST requests to update an existing delivery instruction.
    The instruction must belong to the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object containing form data.
        pk (int): The primary key of the delivery instruction to update.

    Returns:
        JsonResponse: A JSON response with the status and message, and the
                      updated instruction's ID and title if successful.
    """
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    form = DeliveryInstructionForm(request.POST, instance=instruction)
    if form.is_valid():
        instruction = form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Instruction updated successfully',
            'id': instruction.id,
            'title': instruction.title
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid form data'})


@login_required
@require_POST
def instruction_delete(request, pk):
    """
    Delete a delivery instruction.

    This view handles POST requests to delete a delivery instruction.
    The instruction must belong to the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the delivery instruction to delete.

    Returns:
        JsonResponse: A JSON response with the status and message
            of the deletion.
    """
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    instruction.delete()
    return JsonResponse({
        'status': 'success',
        'message': 'Instruction deleted successfully'
    })


@login_required
def instruction_detail(request, pk):
    """
    Retrieve the details of a delivery instruction.

    This view handles GET requests to retrieve the details of a specific
    delivery instruction. The instruction must belong to the currently
    logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the delivery instruction to retrieve.

    Returns:
        JsonResponse: A JSON response with the instruction's ID, title,
            and details.
    """
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    return JsonResponse({
        'id': instruction.pk,
        'title': instruction.title,
        'instruction': instruction.instruction
    })
