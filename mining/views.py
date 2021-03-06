# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Mine, Upgrade
from .forms import MineForm
from companies.models import MineOwnership

# Create your views here.
@login_required(login_url='/login/')
def mines_all(request):
	mines = Mine.objects.all()
	return render(request, "mines.html", {'mines': mines}) 

@login_required(login_url='/login/')
def mine_detail(request, mine_pk):
	player = request.user.company
	mine = get_object_or_404(Mine, pk=mine_pk)
	if request.method == "POST":            
		form = MineForm(request.POST, request.FILES)
		if form.is_valid():
			player = request.user.company
			owned_mine = form.save(commit=False)
			if owned_mine.amount > 0: # amount must be above zero	        
				if owned_mine.amount * mine.price <= player.money:	         
					try: # find player mines of same type, if already exist, add another to amount of mines.
						player_mine = get_object_or_404(MineOwnership, element=owned_mine.element, owner=request.user.company, mine=mine)         
						sale = MineOwnership.objects.add_mine(owned_mine.amount, owned_mine.element, mine, request.user.company)   
						messages.success(request, 'Thank you for your purchase! You can view your purchase on your company profile page.')
						return redirect(mines_all)
					except: # if player mine not already exists, create empty one, then add amount.
						new_mine = MineOwnership.objects.create_mine(mine, owned_mine.element, request.user.company)
						sale = MineOwnership.objects.add_mine(owned_mine.amount, owned_mine.element, mine, request.user.company)
						messages.success(request, 'Thank you for your purchase! You can view your purchase on your company profile page.')
						return redirect(mines_all)
				else:
					messages.error(request, 'You cannot afford this Trade.')	
			else:
				messages.error(request, 'You must choose at least one')
	else:		   
		form = MineForm()
	return render(request, "minedetail.html", {'mine': mine, 'form': form, 'player': player}) 

# upgrades
@login_required(login_url='/login/')
def upgrades(request):
	upgrades = Upgrade.objects.all()
	return render(request, "upgrades.html", {'upgrades': upgrades}) 

# upgrades
@login_required(login_url='/login/')
def upgrade_detail(request, upgrade_pk):
	upgrade = get_object_or_404(Upgrade, pk=upgrade_pk)
	return render(request, "upgradedetail.html", {'upgrade': upgrade}) 

