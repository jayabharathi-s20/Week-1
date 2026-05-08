from fastapi import APIRouter, Depends,status,HTTPException
from sqlalchemy.orm import Session
from ..controllers import category_controllers
from ..models import CategoryCreate, CategoryUpdate, CategoryPatch
from ..utils.dependencies import  admin_only,all_roles,admin_manager,get_db
from ..constants import *



router = APIRouter()

@router.post("/categories",status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate,db: Session = Depends(get_db),current_user=Depends(all_roles)):
    """
    Create a new category.
    """
    try:
        created_category =category_controllers.create_category(db, category.model_dump())
        return {
            "success": True,
            "message": CATEGORY_CREATED_SUCCESS,
            "data": created_category
        }
    except HTTPException:
        raise

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error_code": "CREATE_CATEGORY_FAILED",
                "message": str(e)
            }
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "CREATE_CATEGORY_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.get("/categories",status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db),current_user=Depends(all_roles)):
    """
    Retrieve all categories.
    """
    try:
        categories = category_controllers.get_categories(db)

        return {
            "success": True,
            "message": CATEGORIES_FETCHED_SUCCESS,
            "data": categories
        }
    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "FETCH_CATEGORIES_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.get("/categories/{category_id}",status_code=status.HTTP_200_OK)
def get_category(category_id: int,db: Session = Depends(get_db),current_user=Depends(all_roles)):
    """
    Retrieve a category by ID.
    """
    try:
        category = category_controllers.get_category(db,category_id)

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "CATEGORY_NOT_FOUND",
                    "message": CATEGORY_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": CATEGORY_FETCHED_SUCCESS,
            "data": category
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "FETCH_CATEGORY_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.put("/categories/{category_id}",status_code=status.HTTP_200_OK)
def update_category(category_id: int,category: CategoryUpdate,db: Session = Depends(get_db),current_user=Depends(admin_manager)):
    """
    Fully update a category.
    """
    try:
        updated_category= category_controllers.update_category(db, category_id, category.model_dump())
    
        if not updated_category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "CATEGORY_NOT_FOUND",
                    "message": CATEGORY_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": CATEGORY_UPDATED_SUCCESS,
            "data": updated_category
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error_code": "UPDATE_CATEGORY_FAILED",
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
                "error_code": "UPDATE_CATEGORY_FAILED",
                "message": INTERNAL_SERVER_ERROR
            }
        )


@router.patch("/categories/{category_id}",status_code=status.HTTP_200_OK)
def patch_category(category_id: int,category: CategoryPatch,db: Session = Depends(get_db),current_user=Depends(admin_manager)):
    """
    Partially update a category.
    """
    try:
        patched_category = category_controllers.patch_category(
            db,
            category_id,
            category.model_dump(exclude_unset=True)
        )

        if not patched_category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "success": False,
                    "error_code": "CATEGORY_NOT_FOUND",
                    "message": CATEGORY_NOT_FOUND
                }
            )

        return {
            "success": True,
            "message": CATEGORY_UPDATED_SUCCESS,
            "data": patched_category
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "success": False,
                "error_code": "PATCH_CATEGORY_FAILED",
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
                "error_code": "PATCH_CATEGORY_INTERNAL_ERROR",
                "message": INTERNAL_SERVER_ERROR
            }
        )

@router.delete("/categories/{category_id}",status_code=status.HTTP_200_OK)
def delete_category(category_id: int,db: Session = Depends(get_db),current_user=Depends(admin_only)):
    """
    Delete a category.
    """
    try:
        category_controllers.delete_category(db, category_id)

        return {
            "success": True,
            "message": CATEGORY_DELETED,
            "data": None
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "success": False,
                "error_code": "DELETE_CATEGORY_INTERNAL_ERROR",
                "message": INTERNAL_SERVER_ERROR
            }
        )