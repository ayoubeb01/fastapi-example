"""add user table

Revision ID: c977efdba70d
Revises: 03e2426ddb82
Create Date: 2023-03-25 13:29:03.206298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c977efdba70d'
down_revision = '03e2426ddb82'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')

    )


def downgrade() -> None:
    op.drop_table('users')
    pass
