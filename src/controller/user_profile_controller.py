from fastapi import APIRouter
from src.constants.constants import USER_PROFILE_URL, USER_PROFILE_TAG


user_profile_route = APIRouter(
    prefix=USER_PROFILE_URL,
    tags=[USER_PROFILE_TAG]
)


@user_profile_route.post("")
def create_user():
    return []
