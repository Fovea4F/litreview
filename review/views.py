from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from . import forms, models


@login_required
def home1(request):
    tickets = models.Ticket.objects.filter(
        Q(user__in=request.user.all())
    )
    reviews = models.Review.objects.filter(
        uploader__in=request.user.follows.all()).exclude(review__in=tickets)
    return render(request, 'review/home.html', context={'tickets': tickets, 'reviews': reviews})


@login_required
def home(request):
    tickets = models.Ticket.objects.filter(user=request.user).order_by("time_created")  # most recent before
    tickets_and_review = []
    for ticket in tickets:
        reviews = ticket.review_set.all()
        print(f'Ticket : {ticket}')
        print(f'Critique : {reviews}')
        for review in reviews:
            if review == 'Null':
                tickets_and_review.append((ticket, ''))
            tickets_and_review.append((ticket, review))
    context = {
        'tickets_and_review': tickets_and_review
        }
    return render(request, 'review/home.html', context)


@login_required
def post(request):
    '''print('la méthode de requête est : ', request.method)
    print('les données POST sont : ', request.POST)'''
    tickets = models.Ticket.objects.filter(user=request.user)
    tickets_and_review = []
    for ticket in tickets:
        reviews = ticket.review_set.all()
        print(f'Ticket : {ticket}')
        print(f'Critique : {reviews}')
        for review in reviews:
            tickets_and_review.append((ticket, review))
    context = {
        'tickets_and_review': tickets_and_review
        }
    return render(request, 'review/post.html', context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'review/review_view.html', {'review': review})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'review/ticket_view.html', {'ticket': ticket})


@login_required
def ticket_create(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    context = {'ticket_form': ticket_form}
    return render(request, 'review/ticket_create.html', context=context)


@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('post')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }

    return render(request, 'review/ticket_edit.html', context)


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    delete_form = forms.DeleteTicketForm()
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('post')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'review/ticket_delete.html', context=context)


@login_required
def review_edit(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'review/review_edit.html', context=context)


@login_required
def review_create(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/review_create.html', context=context)


@login_required
def review_and_ticket_edit(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST, )
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/ticket_review_post_edit.html', context=context)


@login_required
def review_and_ticket_create(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST, )
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/review_ticket_create.html', context=context)
