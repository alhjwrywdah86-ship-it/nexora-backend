from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):

    name: str = Field(min_length=1, max_length=255)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserLogin(BaseModel):

    email: EmailStr
    password: str = Field(max_length=72)


class UserResponse(BaseModel):

    id: str
    name: str
    email: EmailStr

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"
