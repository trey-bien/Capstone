from django.shortcuts import render

from .models import Actor

def actor_detail_view(request, actor_id):
    selected_actor = Actor.objects.filter(id=actor_id).first()
    return render(request, 'actordetail.html', { 'actor': selected_actor })