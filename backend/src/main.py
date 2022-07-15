from entities.entity import Session, engine, Base
from entities.exam import Exam

# generate database schema
Base.metadata.create_all(engine)

session = Session()

#exams = session.query(Exam).all()
exams = session.execute(Exam).all()

if len(exams) == 0:
    exam1 = Exam("AI/ML", "1 year PGDM course from Texas university via Great learing", "Postgraduate Diploma")
    session.add(exam1)
    session.commit()
    session.close()

    exams = session.query(Exam).all()

# show existing exams
print('### Exams:')
for exam in exams:
    print(f'({exam.id}) {exam.title} - {exam.description}')