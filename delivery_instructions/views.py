from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryInstruction
from .forms import DeliveryInstructionForm


@login_required
def instruction_list(request):
    instructions = DeliveryInstruction.objects.filter(user=request.user)
    return render(request, 'delivery_instructions/instruction_list.html', {
        'instructions': instructions
    })


@login_required
def instruction_create(request):
    if request.method == 'POST':
        form = DeliveryInstructionForm(request.POST)
        if form.is_valid():
            instruction = form.save(commit=False)
            instruction.user = request.user
            instruction.save()
            return redirect('instruction_list')
    else:
        form = DeliveryInstructionForm()
    return render(request, 'delivery_instructions/instruction_form.html', {
        'form': form
    })


@login_required
def instruction_update(request, pk):
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DeliveryInstructionForm(request.POST, instance=instruction)
        if form.is_valid():
            form.save()
            return redirect('instruction_list')
    else:
        form = DeliveryInstructionForm(instance=instruction)
    return render(request, 'delivery_instructions/instruction_form.html', {
        'form': form
    })


@login_required
def instruction_delete(request, pk):
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    if request.method == 'POST':
        instruction.delete()
        return redirect('instruction_list')
    return render(request,
                  'delivery_instructions/instruction_confirm_delete.html', {
                      'instruction': instruction
                  })


@login_required
def instruction_detail(request, pk):
    instruction = get_object_or_404(
        DeliveryInstruction, pk=pk, user=request.user)
    return render(request, 'delivery_instructions/instruction_detail.html', {
        'instruction': instruction
    })
