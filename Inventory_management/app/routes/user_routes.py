from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..controllers import user_controllers 
from ..models import UserUpdate, UserPatch
from ..utils.dependencies import  admin_only,get_db
from ..constants import *



router = APIRouter()


@router.get("/users",status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db),current_user=Depends(admin_only)):
    """
    Retrieve all users.
    """
    try:
        users= user_controllers.get_users(db)
        return {
            "success": True,
            "message": USERS_FETCHED_SUCCESS,
            "data": users
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "FETCH_USERS_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):
    """
    Retrieve a user by ID.
    """

    try:
        user = user_controllers.get_user(db, user_id)

        if not user["success"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "USER_NOT_FOUND",
                    "message": USER_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": USER_FETCHED_SUCCESS,
            "data": user
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "FETCH_USER_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.put("/users/{user_id}",status_code=status.HTTP_200_OK)
def update_user(user_id: int,user: UserUpdate,db: Session = Depends(get_db),current_user=Depends(admin_only)):
    """
    Fully update a user.
    """
    try:
        updated_user= user_controllers.update_user(db, user_id, user.model_dump())
        if not updated_user["success"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "USER_NOT_FOUND",
                    "message": USER_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": USER_UPDATED_SUCCESS,
            "data": updated_user["data"]
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error_code": "UPDATE_USER_FAILED",
                "message": str(e)
            }
        )

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "UPDATE_USER_INTERNAL_ERROR",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.patch("/users/{user_id}",status_code=status.HTTP_200_OK)
def patch_user(
    user_id: int,
    user: UserPatch,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):
    """
    Partially update a user.
    """

    try:
        patched_user = user_controllers.patch_user(
            db,
            user_id,
            user.model_dump(exclude_unset=True)
        )

        if not patched_user["success"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "USER_NOT_FOUND",
                    "message": USER_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": USER_UPDATED_SUCCESS,
            "data": patched_user["data"]
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error_code": "PATCH_USER_FAILED",
                "message": str(e)
            }
        )

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "PATCH_USER_INTERNAL_ERROR",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_only)
):
    """
    Delete a user.
    """

    try:
        result = user_controllers.delete_user(db, user_id)

        if not result["success"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "USER_NOT_FOUND",
                    "message": USER_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": USER_DELETED
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "DELETE_USER_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )
