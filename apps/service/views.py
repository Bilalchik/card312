from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from django.utils import timezone

from apps.categories.models import Service_category
from apps.service.models import ProductImage, Characteristic, Product, AdditionalInformation, Promotion, PromotionType
from apps.service.serializers import (ProductCreateSerializer, CharacteristicListSerializer, CategoryListSerializer,
                                      ProductUpdateSerializer, ProductListSerializer, PromotionTypeListSerializer,
                                      PromotionCreateSerializer, PromotionUpdateSerializer)
from apps.service.pagination import ProductPagination
from apps.service.filters import ProductFilter


current_date = timezone.now()


class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        characteristic = Characteristic.objects.filter(category__id=pk)
        category = Service_category.objects.filter(parent__isnull=False)
        print(category)

        characteristic_serializer = CharacteristicListSerializer(characteristic, many=True)
        category_serializer = CategoryListSerializer(category, many=True)

        all_data = {
            'category': category_serializer.data,
            'characteristic': characteristic_serializer.data
        }

        return Response(all_data)

    def post(self, request, pk, format=None):
        serializer = ProductCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

    def get_object(self):
        product = super().get_object()
        user = self.request.user

        if product.user != user:
            raise PermissionDenied(
                "Вы не можете изменить этот объект, так как он принадлежит другому пользователю.")
        return product


class MyProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user.id).order_by('-id')


class PromotionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        products = Product.objects.filter(user=self.request.user.id).order_by('-id')
        products_serializer = ProductListSerializer(products, many=True)

        promotion_type = PromotionType.objects.all()
        promotion_type_serializer = PromotionTypeListSerializer(promotion_type, many=True)

        all_data = {
            'products': products_serializer.data,
            'promotion_type': promotion_type_serializer.data
        }

        return Response(all_data)

    def post(self, request, format=None):
        serializer = PromotionCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromotionUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Promotion.objects.all()
    serializer_class = PromotionUpdateSerializer

    def get_object(self):
        promotion = super().get_object()
        user = self.request.user

        if promotion.user != user:
            raise PermissionDenied(
                "Вы не можете изменить этот объект, так как он принадлежит другому пользователю.")
        return promotion


class ProductListView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = ProductPagination

    def get(self, request):
        queryset = Product.objects.all()

        # Проверяем наличие параметров фильтрации в URL
        if request.query_params:
            filter_params = request.query_params.dict()
            filtered_queryset = ProductFilter(filter_params, queryset=queryset).qs
            filtered_serializer = ProductListSerializer(filtered_queryset, many=True)
            return Response(filtered_serializer.data)

        else:
            # Если параметров фильтрации нет, формируем JSON с тремя разными наборами данных
            new_products = Product.objects.all().order_by('-id')
            new_products_serializer = ProductListSerializer(new_products, many=True)

            popular_products = Product.objects.annotate(average_rating=Avg('ratings__rating')).order_by(
                '-average_rating')
            popular_products_serializers = ProductListSerializer(popular_products, many=True)

            burning_products = Product.objects.filter(promotions__end__gte=current_date).distinct().order_by(
                'promotions__end')
            burning_products_serializer = ProductListSerializer(burning_products, many=True)

            category = Service_category.objects.filter(parent__isnull=False)
            category_serializer = CategoryListSerializer(category, many=True)

            all_data = {
                'category': category_serializer.data,
                'new_products': new_products_serializer.data,
                'popular_products': popular_products_serializers.data,
                'burning_products': burning_products_serializer.data,
            }

            return Response(all_data)


