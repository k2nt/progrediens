from typing import Dict, Optional

from http import HTTPStatus

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """Base response schema"""
    code: int = ''
    message: str = ''
    data: Optional[Dict] = None


def ok_response(message: str, data: Optional[Dict] = None) -> ResponseBase:
    """Returns a ResponseBase object with status code 200.
    
    Args:
        message -- str: Response message
        data -- str: Response data [default: None]
        
    Returns:
        ResponseBase
    """
    return ResponseBase(
        code=HTTPStatus.OK.value, 
        message=message, 
        data=data
        )


def not_found_response(message: str, data: Optional[Dict] = None) -> ResponseBase:
    """Returns a ResponseBase object with status code 200.
    
    Args:
        message -- str: Response message
        data -- str: Response data [default: None]
        
    Returns:
        ResponseBase
    """
    return ResponseBase(
        code=HTTPStatus.NOT_FOUND.value, 
        message=message, 
        data=data
        )
