from pydantic import BaseModel, Field


class UserProfileDto(BaseModel):
    user_headquarter: str = Field(min_length=2, max_length=20)
    user_rol: str = Field(min_length=2, max_length=20)
    player_id: int = Field(min=0, max=99)
