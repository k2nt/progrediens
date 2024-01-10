"""The so-called 'z-pages' for system heath checks."""
from fastapi import APIRouter

from app.schema.base import (
    ResponseBase, 
    ok_response,
    )


router = APIRouter()


@router.get('/livez')
async def get_livez():
    """Check if system if alive."""
    return ok_response('ok')
