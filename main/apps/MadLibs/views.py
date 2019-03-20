from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django import forms
from .models import Card


def index(request):
    return render(request, '../templates/index.html')


def create(request):
    errors = Card.objects.card_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        new_card = Card.objects.create()
        new_card.sender = request.POST['sender']
        new_card.recipient = request.POST['recipient']
        new_card.event = request.POST['event']
        new_card.noun1 = request.POST['noun1']
        new_card.noun2 = request.POST['noun2']
        new_card.noun3 = request.POST['noun3']
        new_card.noun4 = request.POST['noun4']
        new_card.noun5 = request.POST['noun5']
        new_card.noun6 = request.POST['noun6']
        new_card.noun7 = request.POST['noun7']
        new_card.noun8 = request.POST['noun8']
        new_card.noun9 = request.POST['noun9']
        new_card.adj1 = request.POST['adj1']
        new_card.adj2 = request.POST['adj2']
        new_card.adj3 = request.POST['adj3']
        new_card.adj4 = request.POST['adj4']
        new_card.adj5 = request.POST['adj5']
        new_card.adj6 = request.POST['adj6']
        new_card.adj7 = request.POST['adj7']
        new_card.save()
        request.session['id'] = new_card.id

        context = {
            'card': new_card
        }

        return redirect("/card", context)


def show(request):
    new_card = Card.objects.get(id=request.session['id'])
    context = {
        'card': new_card
    }

    return render(request, '../templates/card.html', context)


def clear(request):
    request.session.clear()
    return redirect('/')
