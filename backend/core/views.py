from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.viewsets import ModelViewSet

from .models import Car
from .serializers import CarSerializer


class MyPagination(CursorPagination):
    page_size = 15
    # page_size_query_param = 'page_size'
    # max_page_size = 15
    ordering = 'id'


# def all_cars(request):
#     result = []
#     cars = Car.objects.all()
#     for car in cars:
#         # result.append({
#         #     "vendor": car.vendor,
#         #     "model": car.model,
#         #     "year": car.year,
#         #     "volume": car.volume,
#         # })
#         result.append(CarSerializer(car).data)
#     return JsonResponse(result, safe=False)

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = MyPagination

    def filter_queryset(self, queryset):
        for k, v in self.request.query_params.items():
            if k == "cursor":
                continue
            queryset = queryset.filter(**{k: v})
            # тоже самое что:
            # queryset = queryset.filter(model__icontains="asdf")
        return queryset
