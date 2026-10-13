from fastapi import APIRouter
from src.constants.constants import USER_PROFILE_URL, USER_PROFILE_TAG
from src.modelo.user_profile_dto import UserProfileDto
from src.service.user_profile_service import create_user_profile, fetch_user_profile_by_Id

user_profile_route = APIRouter(
    prefix=USER_PROFILE_URL,
    tags=[USER_PROFILE_TAG]
)


@user_profile_route.post("")
async def create_user(user_profile_dto: UserProfileDto):
    return await create_user_profile(user_profile_dto=user_profile_dto)


@user_profile_route.get("/{user_id}")
async def get_user(user_id: int):
    return await fetch_user_profile_by_Id(user_profile_id=user_id)


