from models import Dog

def create_table(base):
    engine = base.engine
    Dog.__table__.create(bind=engine, checkfirst=True)

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    pass

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    pass

def update_breed(session, dog_id, new_breed):
    dog = session.query(Dog).filter_by(id=dog_id).first()
    if dog:
        dog.breed = new_breed
        session.commit()
pass