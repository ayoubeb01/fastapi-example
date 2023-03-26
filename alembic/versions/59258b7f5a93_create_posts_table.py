"""create posts table

Revision ID: 59258b7f5a93
Revises: 
Create Date: 2023-03-24 14:33:24.972748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59258b7f5a93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable=False,primary_key=False)
                    
                    
                    )
    
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
