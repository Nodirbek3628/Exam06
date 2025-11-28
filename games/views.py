import json
from django.http import HttpRequest,JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Game

# Create your views here.


class GameView(View):
    def get(self, request: HttpRequest, id) -> JsonResponse:
        game = get_object_or_404(Game, pk=id)
        return JsonResponse(game.to_dict())
    

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        title = data.get("title")
        location = data.get("location")
        start_date = data.get("start_date")
        description = data.get("description")

        if title is None:
            return JsonResponse({"title": "Required"}, status=400)
        if location is None:
            return JsonResponse({"location": "Required"}, status=400)
        if start_date is None:
            return JsonResponse({"start_date": "Required"}, status=400)
        if len(title) > 200:
            return JsonResponse({"error": "Title max length 200"}, status=400)
        if len(location) > 100:
            return JsonResponse({"error": "Location max length 100"}, status=400)

        game = Game(
            title=title,
            location=location,
            start_date=start_date,
            description=description
        )
        game.save()

        return JsonResponse(game.to_dict(), status=201)

    def patch(self, request: HttpRequest, id) -> JsonResponse:
        game = get_object_or_404(Game, pk=id)
        data = json.loads(request.body.decode())

        game.title = data.get("title", game.title)
        game.location = data.get("location", game.location)
        game.start_date = data.get("start_date", game.start_date)
        game.description = data.get("description", game.description)

        game.save()

        return JsonResponse({
            "message": "Game updated successfully",
            "game": game.to_dict()
        })

    def delete(self, request: HttpRequest, id) -> JsonResponse:
        game = get_object_or_404(Game, pk=id)

        if game.score:
            return JsonResponse({
                "error": "Cannot delete game with existing scores"
            }, status=400)

        game.delete()
        return JsonResponse({
            "message": "Game deleted successfully"
        }, status=200)
