from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll, Option
from django.shortcuts import redirect


def poll_view(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'index.html', {'poll': poll})

def vote(request):
    if request.method == 'POST':
        option_id = request.POST.get('option_id')
        option = get_object_or_404(Option, id=option_id)
        option.votes += 1
        option.save()
        return JsonResponse({'status': 'success', 'votes': option.votes})

def get_poll_data(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        options = list(poll.options.values('id', 'option_text', 'votes'))
        response_data = {
            'question': poll.question,
            'options': options
        }
        return JsonResponse(response_data)
    except Poll.DoesNotExist:
        return JsonResponse({'error': 'Poll not found'}, status=404)

def redirect_to_poll(request):
    # Redirect to poll with ID 1; you can choose a different ID if needed
    return redirect('poll_view', poll_id=1)

def add_option(request, poll_id):
    if request.method == 'POST':
        poll = Poll.objects.get(id=poll_id)
        option_text = request.POST.get('option_text')
        if option_text:
            Option.objects.create(poll=poll, option_text=option_text, votes=1)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

