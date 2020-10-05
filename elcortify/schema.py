import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from elcortify.products.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "category__id": ["exact"],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    product = relay.Node.Field(ProductType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    all_products = DjangoFilterConnectionField(ProductType)


schema = graphene.Schema(query=Query)
