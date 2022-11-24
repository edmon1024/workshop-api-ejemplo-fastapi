import sqlalchemy as sa
import databases
from settings import DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sa.MetaData()

t_customers = sa.Table(
    "customers",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50)),
    sa.Column('last_name', sa.String(50)),
    sa.Column('email', sa.String(50)),
    sa.Column('age', sa.Integer),
)

engine = sa.create_engine(DATABASE_URL)

metadata.create_all(engine)


