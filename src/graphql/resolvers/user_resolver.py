from sqlalchemy import delete, insert, select
from sqlalchemy.orm import load_only

from src.graphql.db.session import get_session
from src.graphql.helpers.helper import get_valid_data
from src.graphql.models import user_model
from src.graphql.scalars.user_scalar import User, UserDeleted, UserExists, UserNotFound

async def get_users(info):
    """ Get all users resolver """
    async with get_session() as s:
        sql = select(user_model.User).options(load_only(*[user_model.User.id,user_model.User.name])).order_by(user_model.User.id)
        db_users = (await s.execute(sql)).scalars().unique().all()

    users_data_list = []
    for user in db_users:
        user_dict = get_valid_data(user,user_model.User)
        users_data_list.append(User(**user_dict))

    return users_data_list

async def get_user(user_id, info):
    """ Get specific user by id resolver """
    async with get_session() as s:
        sql = select(user_model.User).options(load_only(*[user_model.User.id,user_model.User.name])).filter(user_model.User.id == user_id).order_by(user_model.User.name)
        db_user = (await s.execute(sql)).scalars().unique().one()
    
    user_dict = get_valid_data(db_user,user_model.User)
    return User(**user_dict)

async def add_user(name):
    """ Add user resolver """
    async with get_session() as s:
        sql = select(user_model.User).options(load_only(user_model.User.name)) \
            .filter(user_model.User.name == name)
        existing_db_user = (await s.execute(sql)).first()
        if existing_db_user is not None:
            return UserExists()

        query = insert(user_model.User).values(name=name)
        await s.execute(query)
        
        sql = select(user_model.User).options(load_only(user_model.User.name)).filter(user_model.User.name == name)
        db_user = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

    db_user_serialize_data = db_user.as_dict()
    return User(**db_user_serialize_data)

async def delete_user(user_id):
    """ Delete user resolver """
    async with get_session() as s:
        sql = select(user_model.User).where(user_model.User.id == user_id)
        existing_db_user = (await s.execute(sql)).first()
        if existing_db_user is None:
            return UserNotFound()

        query = delete(user_model.User).where(user_model.User.id == user_id)
        await s.execute(query)
        await s.commit()
    
    return UserDeleted()
