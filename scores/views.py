import json
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from .models import Score
from games.models import Game
from players.models import Player


def scores_view(request: HttpRequest, id=None):
    if request.method == "GET":
        if id:
            score = get_object_or_404(Score, pk=id)
            return JsonResponse(score_to_dict(score))
        
        scores = Score.objects.all()
        data = [score_to_dict(s) for s in scores]
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        data = json.loads(request.body.decode())

        game_id = data.get("game")
        player_id = data.get("player")
        result = data.get("result")
        opponent_name = data.get("opponent_name")

        if not game_id:
            return JsonResponse({"game": "Required"}, status=400)
        if not player_id:
            return JsonResponse({"player": "Required"}, status=400)
        if not result:
            return JsonResponse({"result": "Required"}, status=400)

        game = get_object_or_404(Game, pk=game_id)
        player = get_object_or_404(Player, pk=player_id)

        new_score = Score(
            game=game,
            player=player,
            result=result,
            opponent_name=opponent_name
        )
        new_score.save()

        return JsonResponse(score_to_dict(new_score), status=201)
    
    if request.method == "PATCH":
        if not id:
            return JsonResponse({"error": "ID required"}, status=400)

        score = get_object_or_404(Score, pk=id)
        data = json.loads(request.body.decode())

        score.result = data.get("result", score.result)
        score.opponent_name = data.get("opponent_name", score.opponent_name)
        score.save()

        return JsonResponse({"message": "Score updated successfully"})
    if request.method == "DELETE":
   
        if not id:
            return JsonResponse({"error": "ID required"}, status=400)

        score = get_object_or_404(Score, pk=id)
        score.delete()

        return JsonResponse({"message": "Score deleted successfully"})

    return JsonResponse({"error": "Method not allowed"}, status=405)

def score_to_dict(obj: Score) -> dict:
    return {
        "id": obj.id,
        "game": obj.game_id,
        "player": obj.player_id,
        "result": obj.result,
        "points": obj.points,
        "opponent_name": obj.opponent_name,
        "created_at": obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    }
