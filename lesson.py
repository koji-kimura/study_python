import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///test_sqlite2', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
p2 = Person(name='Nancy')
p3 = Person(name='Jun')
session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Micel'
session.query(Person)
session.add(p4)
session.commit()
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
