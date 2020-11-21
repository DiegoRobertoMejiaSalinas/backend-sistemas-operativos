import graphene
from base.models import Role, User, Directory, File
from .types import *


class Query(graphene.ObjectType):
    # Crea Directorio como una lista Graphene que toma el DirectoryType como PLANTILLA
    directory = graphene.List(DirectoryType)
    directory_by_id= graphene.Field(DirectoryType, id= graphene.String(required=True))

    file= graphene.List(FileType)
    file_by_id= graphene.Field(FileType, id= graphene.String(required=True))

    role= graphene.List(RoleType)
    role_by_id= graphene.Field(RoleType, id= graphene.String(required=True))

    user= graphene.List(UserType)
    user_by_id= graphene.Field(UserType, id= graphene.String(required=True))



    def resolve_directory(self, args):
        return Directory.objects.select_related("user", "belongs_to").all()

    def resolve_directory_by_id(root, info, id):
        try:
            return Directory.objects.get(pk=id)
        except Directory.DoesNotExist:
            return None

    def resolve_file(self, args):
        return File.objects.select_related("user", "belongs_to").all()

    def resolve_file_by_id(root, info, id):
        try:
            return File.objects.get(pk=id)
        except File.DoesNotExist:
            return None

    def resolve_user(self, args):
        return User.objects.select_related("role").all()

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def resolve_role(self, args):
        return Role.objects.all()

    def resolve_role_by_id(root, info, id):
        try:
            return Role.objects.get(pk=id)
        except Role.DoesNotExist:
            return None