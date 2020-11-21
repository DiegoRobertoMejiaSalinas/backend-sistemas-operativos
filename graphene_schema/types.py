import graphene
from graphene_django import DjangoObjectType
from graphene import ObjectType

from base.models import Role, User, Directory, File
"""
CONVIERTE LOS MODELOS EN OBJETOS
LEGIBLES PARA GRAPHQL BASADO EN DjangoObjectType
"""

class RoleType(DjangoObjectType):
    class Meta:
        model= Role
        fields= "__all__"
        description= "Brings all roles created"

class UserType(DjangoObjectType):
    class Meta:
        model= User
        fields= "__all__"
        description= "Careful, it brings all users, so take it with care"

class DirectoryType(DjangoObjectType):
    class Meta:
        model= Directory
        fields= "__all__"

class FileType(DjangoObjectType):
    class Meta: 
        model= File
        fields= "__all__"