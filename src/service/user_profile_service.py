from src.modelo.user_profile_dto import UserProfileDto
from src.database.database import get_database_connection
from src.constants.constants import USER_PROFILE_COLLECTION
from bson import ObjectId


async def create_user_profile(user_profile_dto: UserProfileDto):
    user_profile_model = user_profile_dto.model_dump()
    created_id = await get_database_connection(USER_PROFILE_COLLECTION).insert_one(user_profile_model)
    return {"id": str(created_id.inserted_id)}


async def fetch_user_profile_by_Id(user_profile_id: int):
    user_profiles = await get_database_connection(USER_PROFILE_COLLECTION).find(
        {"player_id": user_profile_id}
    ).to_list(length=None)


    for user_profile in user_profiles:
        user_profile["_id"]=str(user_profile["_id"])


    return user_profiles
