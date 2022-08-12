from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Date


Base = declarative_base()


palette_colors = Table(
    'palette_colors',
    Base.metadata,
    Column('palette_id', ForeignKey('palette.id')),
    Column('color_id', ForeignKey('color.id'))
)


class Color(Base):

    __tablename__ = 'color'

    id = Column(Integer, primary_key=True)
    red = Column(Integer)
    green = Column(Integer)
    blue = Column(Integer)


class Palette(Base):

    __tablename__ = 'palette'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300))
    date = Column(Date)
    colors = relationship('Color', secondary=palette_colors)
