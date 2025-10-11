from fastapi import APIRouter, Query, Depends, HTTPException
import logging
from collab_python.util.common import validate_token
from collab_python.repository.lists import fetch_my_lists, add_list, delete_list, owner_of_list
logging.basicConfig(level=logging.INFO)
import asyncio
from collab_python.schemas.list import ListAPIRequest

router = APIRouter(prefix='/api/v1/lists', tags=['List Management'])

@router.get("/")
async def get_lists(
    offset: int = Query(0, ge=0, description="Starting Index"),
    limit: int = Query(10, le=100, description="Number of Items to return"),
    jwt_token = Depends(validate_token)
):
    res = await asyncio.to_thread(fetch_my_lists, (offset, limit, ))

    return { "lists": res }


@router.post("/")
async def add_lists(
    user_input: ListAPIRequest,
    jwt_token = Depends(validate_token)
):
    owner_id = jwt_token.get("id")
    transformed_user = user_input
    transformed_user.owner_id = owner_id
    res = await asyncio.to_thread(add_list, transformed_user, user_input.is_public)
    if res:
        return {
            "message": "List Added Successfully"
        }

@router.delete("/")
async def delete_list_api(
    id: int = Query(description="List Id"),
    jwt_token = Depends(validate_token)
):
    
    

    owner_id = jwt_token.get("id")
    
    logging.info(f"owner = {owner_id} id = {id}")
    list_owner_id = await asyncio.to_thread(owner_of_list, id)
    logging.info(f"owner = {owner_id} id = {id} list_owner_id = {list_owner_id}")


    if owner_id == list_owner_id:
        await asyncio.to_thread(delete_list, id)
        return {
            "message": "deleted successfully"
        }
    else:
        raise HTTPException(status_code=401, detail="You are not allowed to delete this list or list does not exist")