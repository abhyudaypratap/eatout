"""View for Search Api."""
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurant import search


class RestaurantSearchApiView(APIView):
    """Restaurant Search Api."""
    renderer_classes = (JSONRenderer, )

    def post(self, request, *args, **kwargs):

        coordinates = request.data.get("coordinates")
        query = request.data.get("query")
        if query and coordinates:
            result = search.searchbyquery(query, coordinates)
            return Response(result)
        elif query:
            result = search.searchbyquery(query, coordinates)
            return Response(result)
        elif coordinates:
            result = search.searchbycordinates(coordinates)
            return Response(result)
        else:
            return Response({"data": "no data send"})
