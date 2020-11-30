import graphene
# from graphene_file_upload.scalars import Upload

from base.models import *
from .types import *
from .input import *
"""
    ROLE
"""


class CreateRoleMutation(graphene.Mutation):
    class Input:
        role = graphene.Argument(CreateRoleInput)

    role = graphene.Field(RoleType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('role').name.strip()

        obj = Role.objects.create(name=name)

        return CreateRoleMutation(category=obj)


class UpdateRoleMutation(graphene.Mutation):
    class Input:
        role = graphene.Argument(UpdateRoleInput)

    role = graphene.Field(RoleType)

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('role').id
        name = kwargs.get('role').name.strip()

        obj = Role.objects.get(pk=id)

        obj.name = name
        obj.save()

        return UpdateRoleMutation(category=obj)


class DeleteRoleMutation(graphene.Mutation):
    class Input:
        role = graphene.Argument(DeleteInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('role').id

        obj = Role.objects.get(pk=id)
        obj.delete()

        return DeleteRoleMutation(success=True)


"""
    USER
"""


class CreateUserMutation(graphene.Mutation):
    class Input:
        user = graphene.Argument(CreateUserInput)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('user').name.strip()
        role = kwargs.get('user').role.strip()

        obj = User.objects.create(name=name)

        return CreateUserMutation(category=obj)


class UpdateUserMutation(graphene.Mutation):
    class Input:
        user = graphene.Argument(UpdateUserInput)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('user').id
        name = kwargs.get('user').name.strip()
        role = kwargs.get('user').role.strip()

        obj = User.objects.get(pk=id)

        obj.name = name
        obj.role = role

        obj.save()

        return UpdateUserMutation(category=obj)


class DeleteUserMutation(graphene.Mutation):
    class Input:
        user = graphene.Argument(DeleteInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('user').id

        obj = User.objects.get(pk=id)
        obj.delete()

        return DeleteUserMutation(success=True)


"""
    DIRECTORY
"""


class CreateDirectoryMutation(graphene.Mutation):
    class Input:
        directory = graphene.Argument(CreateDirectoryInput)

    directory = graphene.Field(DirectoryType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('directory').name.strip()
        # readableRoot = kwargs.get('directory').readable
        # writableRoot = kwargs.get('directory').writable
        user = None
        belongs_to = None

        dataTempUser = kwargs.get('directory').user
        dataTempBelongsTo = kwargs.get('directory').belongsTo

        if dataTempUser != '' and dataTempUser:
            user = User.objects.get(pk=dataTempUser)

        if dataTempBelongsTo != '' and dataTempBelongsTo:
            belongs_to = Directory.objects.get(pk=dataTempBelongsTo)

        obj = Directory.objects.create(
            name=name,  user=user, belongs_to=belongs_to)

        return CreateDirectoryMutation(directory=obj)


class UpdateDirectoryMutation(graphene.Mutation):
    class Input:
        directory = graphene.Argument(UpdateDirectoryInput)

    directory = graphene.Field(DirectoryType)

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('directory').id
        name = kwargs.get('directory').name.strip()
        # readable = kwargs.get('directory').readable
        # writable = kwargs.get('directory').writable
        user = None
        belongs_to = None

        dataTempUser = kwargs.get('directory').user
        dataTempBelongsTo = kwargs.get('directory').belongsTo

        if dataTempUser != '' and dataTempUser:
            user = User.objects.get(pk=dataTempUser)

        if dataTempBelongsTo != '' and dataTempBelongsTo:
            belongs_to = Directory.objects.get(pk=dataTempBelongsTo)

        obj = Directory.objects.get(pk=id)

        obj.name = name
        # obj.readable = readable
        # obj.writable = writable
        obj.user= user
        obj.belongs_to = belongs_to
        obj.save()

        return UpdateDirectoryMutation(directory=obj)


class DeleteDirectoryMutation(graphene.Mutation):
    class Input:
        directory = graphene.Argument(DeleteInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('directory').id

        obj = Directory.objects.get(pk=id)
        obj.delete()

        return DeleteDirectoryMutation(success=True)



"""
    FILE
"""


class CreateFileMutation(graphene.Mutation):
    class Input:
        file = graphene.Argument(CreateFileInput)

    file = graphene.Field(FileType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('file').name.strip()
        # readable = kwargs.get('file').readable
        # writable = kwargs.get('file').writable
        # content= kwargs.get('file').content.strip()
        user = None
        belongs_to = None

        dataTempUser = kwargs.get('file').user
        dataTempBelongsTo = kwargs.get('file').belongsTo

        if dataTempUser != '' and dataTempUser:
            user = User.objects.get(pk=dataTempUser)

        if dataTempBelongsTo != '' and dataTempBelongsTo:
            belongs_to = Directory.objects.get(pk=dataTempBelongsTo)

        obj = File.objects.create(
            name=name, user=user, belongs_to=belongs_to)

        return CreateFileMutation(file=obj)


class UpdateFileMutation(graphene.Mutation):
    class Input:
        file = graphene.Argument(UpdateFileInput)

    file = graphene.Field(FileType)

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('file').id
        name = kwargs.get('file').name.strip()
        # readable = kwargs.get('file').readable
        # writable = kwargs.get('file').writable
        content= kwargs.get('file').content.strip()
        user = None
        belongs_to = None

        dataTempUser = kwargs.get('file').user
        dataTempBelongsTo = kwargs.get('file').belongsTo

        if dataTempUser != '' and dataTempUser:
            user = User.objects.get(pk=dataTempUser)

        if dataTempBelongsTo != '' and dataTempBelongsTo:
            belongs_to = File.objects.get(pk=dataTempBelongsTo)

        obj = File.objects.get(pk=id)

        obj.name = name
        obj.content= content
        # obj.readable = readable
        # obj.writable = writable
        obj.user= user
        obj.belongs_to = belongs_to
        obj.save()

        return UpdateFileMutation(file=obj)


class DeleteFileMutation(graphene.Mutation):
    class Input:
        file = graphene.Argument(DeleteInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **kwargs):
        id = kwargs.get('file').id

        obj = File.objects.get(pk=id)
        obj.delete()

        return DeleteFileMutation(success=True)

"""
MUTATIONS - Junta todas las funciones de Mutacion en una clase Mutation
"""

class Mutation(graphene.ObjectType):
    create_role = CreateRoleMutation.Field()
    create_user = CreateUserMutation.Field()
    create_file = CreateFileMutation.Field()
    create_directory = CreateDirectoryMutation.Field()

    update_role = UpdateRoleMutation.Field()
    update_user = UpdateUserMutation.Field()
    update_file = UpdateFileMutation.Field()
    update_directory = UpdateDirectoryMutation.Field()

    delete_role = DeleteRoleMutation.Field()
    delete_user = DeleteUserMutation.Field()
    delete_file = DeleteFileMutation.Field()
    delete_directory = DeleteDirectoryMutation.Field()

 