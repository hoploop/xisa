
# PYTHON IMPORTS
from typing import Annotated
import logging

# LIBRARY IMPORTS
from fastapi import Depends, HTTPException, Request, status

# LOCAL IMPORTS
from api.models.auth import Token, User

# INITIALIZATION
log = logging.getLogger(__name__)


class AuthController:
    USERS = {}
    TOKENS = {}
    
    async def check_token(self,token: str) -> bool:  
        if token is None:
            return False
        found = await Token.find_many(Token.code == token).first_or_none()
        if not found:
            return False
        return True
    
    async def login(self,username:str,password:str,host:str)-> dict:
        user = await User.find_many(User.username == username).first_or_none()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        verified = await user.verify_password(password)
        if not verified:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        token_doc = Token(user=user.id,host=host)
        await token_doc.insert()
        AuthController.USERS[token_doc.code] = user
        AuthController.TOKENS[token_doc.code] = token_doc
            

        return {"access_token": token_doc.code, "token_type": "bearer"}
    
    async def logout(self,token:str|None) -> bool:
        if token is None:
            return False
        await Token.find_many(Token.code == token).delete()
        if token in AuthController.USERS:
            del AuthController.USERS[token]
        if token in AuthController.TOKENS:
            del AuthController.TOKENS[token]
        return True

    async def register(self,username:str,email:str,password:str)-> bool:
        user = await User.find_one(User.username == username)
        
        if user is None:
            log.debug("Creating user: {0}".format(username))
            user = User(
                username=username,
                email=email,
                password=password,
                full_name=username,
            )
            await User.insert_one(user)
            return True
        
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User already exists",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
    async def unregister(self,token:str)-> bool:
        log.debug('Unregistering')
        token_doc = await Token.find_many(Token.code == token).first_or_none()
        if token_doc is None:
            return False
        await User.find(User.id == token.user).delete()
        await token.delete()
        if token in AuthController.TOKENS:
            del AuthController.TOKENS[token]
        if token in AuthController.USERS:
            del AuthController.USERS[token]
        return True
    
    async def password_reset(self,token:str,host:str,old_password:str,new_password:str) -> bool:
        token_doc = await Token.find_many(
            Token.code == token, Token.host == host
        ).first_or_none()
        if token_doc is None:
            return False
        user = await User.find_many(User.id == token_doc.user).first_or_none()
        if user is None:
            return False
        verified = await user.verify_password(old_password)
        if not verified:
            return False
        user.password = new_password
        await user.save()
        return True


async def get_auth(request: Request) ->  AuthController:
    if not hasattr(request.app.state,'auth'):
        request.app.state.auth = AuthController()
    return request.app.state.auth

Auth = Annotated[AuthController,Depends(get_auth)]