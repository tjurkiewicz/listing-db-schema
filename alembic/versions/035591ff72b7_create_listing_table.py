"""Create Listing table

Revision ID: 035591ff72b7
Revises: 
Create Date: 2017-08-04 13:55:06.773508

"""
import alembic.op
import sqlalchemy


# revision identifiers, used by Alembic.
revision = '035591ff72b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    alembic.op.create_table(
        'listing',
        sqlalchemy.Column('id', sqlalchemy.Sequence, primary_key=True),
        sqlalchemy.Column('listing_id', sqlalchemy.Integer),
        sqlalchemy.Column('last_update', sqlalchemy.DateTime),
        sqlalchemy.Column('city', sqlalchemy.String(length=64))
    )

def downgrade():
    alembic.op.drop_table('listing')
