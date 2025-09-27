"""increase username length to 36

Revision ID: 56bb30d4539b
Revises: 2b231de97dc3
Create Date: 2025-09-27 12:27:36.155671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56bb30d4539b'
down_revision = '2b231de97dc3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # تغییر طول ستون username به 36
    op.alter_column(
        'users',
        'username',
        type_=sa.String(length=36, collation='utf8mb4_bin'),
        nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        'users',
        'username',
        type_=sa.String(length=34, collation='utf8mb4_bin'),
        nullable=True
    )
