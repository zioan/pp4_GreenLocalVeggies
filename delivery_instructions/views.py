from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import DeliveryInstruction
from .forms import DeliveryInstructionForm


@login_required
@require_POST
def instruction_create(request):
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
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    instruction.delete()
    return JsonResponse({
        'status': 'success',
        'message': 'Instruction deleted successfully'
    })


@login_required
def instruction_detail(request, pk):
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    return JsonResponse({
        'id': instruction.pk,
        'title': instruction.title,
        'instruction': instruction.instruction
    })
