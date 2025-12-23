"""create tables2

Revision ID: edf280b1ffa0
Revises: 94dd2ae44126
Create Date: 2025-12-24 00:07:47.215140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edf280b1ffa0'
down_revision: Union[str, Sequence[str], None] = '94dd2ae44126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
