from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from ..models import User
from ..constants import *


def get_users(db: Session):
    """
    Retrieve all users.

    Args:
        db (Session):
            Active SQLAlchemy database session.

    Returns:
        dict:
            Returns list of users or failure response.
    """

    try:
        users = db.query(User).all()

        return {
            "success": True,
            "message": USERS_FETCHED_SUCCESS,
            "data": users
        }

    except Exception as e:
        return {
            "success": False,
            "message": FETCH_USERS_FAILED,
            "error": str(e)
        }


def get_user(db: Session, user_id: int):
    """
    Retrieve a user by ID.

    Args:
        db (Session):
            Active SQLAlchemy database session.

        user_id (int):
            User ID.

    Returns:
        dict:
            Returns user data or failure response.
    """

    try:
        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if not user:
            return {
                "success": False,
                "message": USER_NOT_FOUND
            }

        return {
            "success": True,
            "message": USER_FETCHED_SUCCESS,
            "data": user
        }

    except Exception as e:
        return {
            "success": False,
            "message": FETCH_USER_FAILED,
            "error": str(e)
        }


def update_user(db: Session, user_id: int, data: dict):
    """
    Fully update a user.

    Args:
        db (Session):
            Active SQLAlchemy database session.

        user_id (int):
            User ID.

        data (dict):
            Updated user payload.

    Returns:
        dict:
            Returns updated user or failure response.
    """

    try:
        user_response = get_user(db, user_id)

        if not user_response["success"]:
            return user_response

        user = user_response["data"]

        if "email" in data:
            existing = db.query(User).filter(
                User.email == data["email"],
                User.id != user_id
            ).first()

            if existing:
                return {
                    "success": False,
                    "message": EMAIL_EXISTS
                }

        for key, value in data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "message": USER_UPDATED_SUCCESS,
            "data": user
        }

    except IntegrityError:
        db.rollback()

        return {
            "success": False,
            "message": EMAIL_EXISTS
        }

    except SQLAlchemyError as e:
        db.rollback()

        return {
            "success": False,
            "message": DATABASE_ERROR,
            "error": str(e)
        }

    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": UPDATE_USER_FAILED,
            "error": str(e)
        }


def patch_user(db: Session, user_id: int, data: dict):
    """
    Partially update a user.

    Args:
        db (Session):
            Active SQLAlchemy database session.

        user_id (int):
            User ID.

        data (dict):
            Partial user payload.

    Returns:
        dict:
            Returns patched user or failure response.
    """

    try:
        user_response = get_user(db, user_id)

        if not user_response["success"]:
            return user_response

        user = user_response["data"]

        if "email" in data:
            existing = db.query(User).filter(
                User.email == data["email"],
                User.id != user_id
            ).first()

            if existing:
                return {
                    "success": False,
                    "message": EMAIL_EXISTS
                }

        for key, value in data.items():
            if value is not None:
                setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return {
            "success": True,
            "message": USER_UPDATED_SUCCESS,
            "data": user
        }

    except IntegrityError:
        db.rollback()

        return {
            "success": False,
            "message": EMAIL_EXISTS
        }

    except SQLAlchemyError as e:
        db.rollback()

        return {
            "success": False,
            "message": DATABASE_ERROR,
            "error": str(e)
        }

    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": PATCH_USER_FAILED,
            "error": str(e)
        }


def delete_user(db: Session, user_id: int):
    """
    Delete a user by ID.

    Args:
        db (Session):
            Active SQLAlchemy database session.

        user_id (int):
            User ID.

    Returns:
        dict:
            Returns deletion status response.
    """

    try:
        user_response = get_user(db, user_id)

        if not user_response["success"]:
            return user_response

        user = user_response["data"]

        db.delete(user)
        db.commit()

        return {
            "success": True,
            "message": USER_DELETED
        }

    except SQLAlchemyError as e:
        db.rollback()

        return {
            "success": False,
            "message": DATABASE_ERROR,
            "error": str(e)
        }

    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": DELETE_USER_FAILED,
            "error": str(e)
        }