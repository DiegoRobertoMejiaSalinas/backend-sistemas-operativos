import graphene
"""
Los INPUT son una plantilla que indicará que campos son obligatorios
esa plantilla se usará en el mutation como Argument

ejm:
graphene.Argument(ModuloInput)
"""

class CreateRoleInput(graphene.InputObjectType):
    name= graphene.String(required=True)

class CreateUserInput(graphene.InputObjectType):
    name= graphene.String(required=True)
    role= graphene.String(required=True)

class CreateDirectoryInput(graphene.InputObjectType):
    name= graphene.String(required=True)
    # readable= graphene.Boolean(required=True)
    # writable= graphene.Boolean(required=True)
    user= graphene.String(required=True)
    belongsTo= graphene.String(required=True)

class CreateFileInput(graphene.InputObjectType):
    name= graphene.String(required=True)
    content= graphene.String(required=True)
    # readable= graphene.Boolean(required=True)
    # writable= graphene.Boolean(required=True)
    user= graphene.String(required=True)
    belongsTo= graphene.String(required=True)


# UPDATE
class UpdateRoleInput(graphene.InputObjectType):
    id= graphene.Int(required=True)
    name= graphene.String(required=True)

class UpdateUserInput(graphene.InputObjectType):
    id= graphene.Int(required=True)
    name= graphene.String(required=True)
    role= graphene.String(required=True)

class UpdateDirectoryInput(graphene.InputObjectType):
    id= graphene.Int(required=True)
    name= graphene.String(required=True)
    readable= graphene.Boolean(required=True)
    writable= graphene.Boolean(required=True)
    user= graphene.String(required=True)
    belongsTo= graphene.String(required=True)

class UpdateFileInput(graphene.InputObjectType):
    id= graphene.Int(required=True)
    name= graphene.String(required=True)
    content= graphene.String(required=True)
    readable= graphene.Boolean(required=True)
    writable= graphene.Boolean(required=True)
    user= graphene.String(required=True)
    belongsTo= graphene.String(required=True)

class DeleteInput(graphene.InputObjectType):
    id = graphene.Int(required=True)