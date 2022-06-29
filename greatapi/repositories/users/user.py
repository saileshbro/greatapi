from __future__ import annotations

from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from greatapi.db.models.user import User
from greatapi.repositories.auth.hashing import Hash
from greatapi.schemas.user import UserType


def create_new_user(request: UserType, db: Session) -> list[tuple[int, str]]:
    new_user = User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(id: int, db: Session) -> list[tuple[int, str]]:
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User id {id} does not exist.',
        )

    return user