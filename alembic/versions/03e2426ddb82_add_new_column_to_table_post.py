"""add new column to table post

Revision ID: 03e2426ddb82
Revises: 59258b7f5a93
Create Date: 2023-03-25 13:20:36.090256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03e2426ddb82'
down_revision = '59258b7f5a93'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
