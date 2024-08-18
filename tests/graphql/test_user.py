from tests.conftest import TestAsynchronously
from tests.graphql.queries import get_users_query, get_specific_user_query
from tests.graphql.mutations import create_user, delete_specific_user
from src.app import schema

class TestUsers(TestAsynchronously):

    def test_01_an_async_get_all_users(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert resp.data["users"] == []

    def test_02_an_async_create_users(self):
        resp = self.get_async_result(schema.execute(
            create_user,
        ))
        assert resp.data["addUser"] == {'id': 1, 'name': 'test'}

    def test_03_an_async_create_users_again(self):
        resp = self.get_async_result(schema.execute(
            create_user,
        ))
        assert resp.data == {'addUser': {'message': 'User with this name already exists'}}

    def test_04_an_async_get_all_users_with_created_user(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert len(resp.data["users"]) == 1
        for key_user in resp.data["users"][0].keys():
            assert key_user in ['id','name'] 

    def test_05_an_async_get_specific_user(self):
        resp = self.get_async_result(schema.execute(
            get_specific_user_query,
        ))
        for key_user in resp.data["user"].keys():
            assert key_user in ['id','name']

    def test_06_an_async_delete_specific_user(self):
        resp = self.get_async_result(schema.execute(
            delete_specific_user,
        ))
        assert resp.data == {"deleteUser": {"message": "User deleted"}}
        resp = self.get_async_result(schema.execute(
            delete_specific_user,
        ))
        assert resp.data == {"deleteUser": { "message": "Couldn't find user with the supplied id"}}
    
    def test_07_an_async_get_all_users(self):
        resp = self.get_async_result(schema.execute(
            get_users_query,
        ))
        assert resp.data["users"] == []
