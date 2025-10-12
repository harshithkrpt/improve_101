from fastapi import APIRouter, Query, Depends, HTTPException
import logging
from collab_python.util.common import validate_token
from collab_python.repository.lists import fetch_my_lists, add_list, delete_list, owner_of_list, fetch_list_id, update_list_id
logging.basicConfig(level=logging.INFO)
import asyncio
from collab_python.schemas.list import UpdateListIn, ListAPIRequest

router = APIRouter(prefix='/api/v1/lists', tags=['List Management'])

@router.get("/")
async def get_lists(
    offset: int = Query(0, ge=0, description="Starting Index"),
    limit: int = Query(10, le=100, description="Number of Items to return"),
    jwt_token = Depends(validate_token)
):
    owner_id = jwt_token.get("id")
    res = await asyncio.to_thread(fetch_my_lists, owner_id, offset, limit,)

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
    list_owner_id = await asyncio.to_thread(owner_of_list, id)
  
    if owner_id == list_owner_id:
        await asyncio.to_thread(delete_list, id)
        return {
            "message": "deleted successfully"
        }
    else:
        raise HTTPException(status_code=401, detail="You are not allowed to delete this list or list does not exist")
    

@router.get("/{id}")
async def fetch_lists_by_id(id: int, jwt_token = Depends(validate_token)):
    res = await asyncio.to_thread(fetch_list_id, id)
    if res is None:
        raise HTTPException(status_code=404, detail="List item not found")
    if res.get("owner_id") != jwt_token.get("id"):
        raise HTTPException(status_code=404, detail="You are not authorised to view the data")
    return res

@router.put("/{id}")
async def update_list(id: int, list_request: UpdateListIn, jwt_token = Depends(validate_token)):
    res = await asyncio.to_thread(fetch_list_id, id, True)
    if res.get("owner_id") != jwt_token.get("id"):
        raise HTTPException(status_code=404, detail="You are not authorised to view the data")
    else:
        logging.info(res)
        title = res.get("title")
        if list_request.title:
            title = list_request.title

        desc = res.get("description")
        if list_request.description:
            desc = list_request.description

        await asyncio.to_thread(update_list_id, {
            'title': title,
            'description': desc,
            'is_public': res.get("is_public"),
            'id': id
        })

        return {
            'detail': "updated successfully"
        }