from django_filters import rest_framework as filters
from apps.service.models import Product
from django.db.models import Q, Avg


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    characteristic = CharFilterInFilter(field_name='characteristic__characteristic__title', lookup_expr='in')
    price = filters.RangeFilter()
    average_rating = filters.NumberFilter(method='filter_by_average_rating')

    class Meta:
        model = Product
        fields = ('category', 'city', 'price', 'type', 'characteristic', 'average_rating')

    def filter_by_average_rating(self, queryset, name, value):
        # Проверяем, что значение average_rating задано и валидно
        if value is not None:
            # Фильтруем продукты по среднему рейтингу
            return queryset.annotate(avg_rating=Avg('ratings__rating')).filter(avg_rating__gte=value)
        else:
            # Если значение average_rating не задано, возвращаем исходный queryset
            return queryset
