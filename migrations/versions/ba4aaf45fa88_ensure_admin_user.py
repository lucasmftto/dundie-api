"""ensure_admin_user

Revision ID: ba4aaf45fa88
Revises: 80a16ba89ca6
Create Date: 2024-02-18 20:08:36.801341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from dundie.models.user import User
from sqlmodel import Session


# revision identifiers, used by Alembic.
revision: str = 'ba4aaf45fa88'
down_revision: Union[str, None] = '80a16ba89ca6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Lucas Admin",
        username="lucas",
        email="lucas@dm.com",
        dept="management",
        currency="USD",
        password="123",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
