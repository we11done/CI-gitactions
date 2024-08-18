import strawberry

from src.graphql.resolvers.user_resolver import add_user, delete_user
from src.graphql.fragments.user_fragments import AddUserResponse, DeleteUserResponse



@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_user(self, name: str) -> AddUserResponse:
        """ Add user """
        add_user_resp = await add_user(name)
        return add_user_resp

    @strawberry.mutation
    async def delete_user(self, user_id: int) -> DeleteUserResponse:
        """ Delete user """
        delete_user_resp = await delete_user(user_id)
        return delete_user_resp
