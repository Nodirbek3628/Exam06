
import json
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from .models import Player

# Create your views here.


def players_view(request: HttpRequest, id=None):

    if request.method == "GET":
        if id:
            player = get_object_or_404(Player, pk=id)
            return JsonResponse(player.to_dict_score())
    
        players = Player.objects.all()
        country = request.GET.get("country")
        min_rating = request.GET.get("min_rating")
        search = request.GET.get("search")

        if country:
            players = players.filter(country__iexact=country)
        if min_rating:
            players = players.filter(rating__gte=int(min_rating))
        if search:
            players = players.filter(nickname__icontains=search)

        data = [p.to_dict_score() for p in players]
        return JsonResponse(data, safe=False)
    
    if request.method == "POST":
        data = json.loads(request.body.decode())
        nickname = data.get("nickname")
        country = data.get("country")

        if not nickname:
            return JsonResponse({"nickname": "Required"}, status=400)
        if not country:
            return JsonResponse({"country": "Required"}, status=400)

        if Player.objects.filter(nickname=nickname).exists():
            return JsonResponse({"nickname": "Already exists"}, status=400)

        player = Player(nickname=nickname, country=country)
        player.save()

        return JsonResponse(player.to_dict(), status=201)
    
    if request.method == "PATCH":
            if not id:
                return JsonResponse({"error": "ID required"}, status=400)

            player = get_object_or_404(Player, pk=id)
            data = json.loads(request.body.decode())

            player.nickname = data.get("nickname", player.nickname)
            player.country = data.get("country", player.country)
            player.save()

            return JsonResponse({"message": "Player updated successfully"})

     
    if request.method == "DELETE":
            if not id:
                return JsonResponse({"error": "ID required"}, status=400)

            player = get_object_or_404(Player, pk=id)

            if player.score.exists():
                    return JsonResponse(
                        {"error": f"Cannot delete player with game history. Player has {player.score.count()} recorded games."},
                        status=400
                    )

            player.delete()
            return JsonResponse({"message": "Player deleted successfully"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
