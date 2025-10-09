from pydantic import BaseModel


class UserRequestSignUp(BaseModel):
    email: str
    password: str
    display_name: str


class UserLoginRequest(BaseModel):
    username: str
    password: str
