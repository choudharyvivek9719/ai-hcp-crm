from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def get_user(db: Session, user_id: int) -> Optional[User]:
    """
    Get a user by ID.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    Get a user by email.
    """
    return db.query(User).filter(User.email == email).first()


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> List[User]:
    """
    Get all users with pagination.
    """
    return (
        db.query(User)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new sales representative.
    """

    db_user = User(
        name=user.name,
        email=user.email,
        territory=user.territory,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user_update: UserUpdate,
) -> Optional[User]:
    """
    Update an existing user.
    """

    db_user = get_user(db, user_id)

    if not db_user:
        return None

    update_data = user_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    user_id: int,
) -> bool:
    """
    Delete a user.
    """

    db_user = get_user(db, user_id)

    if not db_user:
        return False

    db.delete(db_user)
    db.commit()

    return True


def search_users(
    db: Session,
    keyword: str,
) -> List[User]:
    """
    Search users by name or territory.
    """

    keyword = f"%{keyword}%"

    return (
        db.query(User)
        .filter(
            (User.name.ilike(keyword))
            | (User.territory.ilike(keyword))
        )
        .all()
    )
