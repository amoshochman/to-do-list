# from app import db, Task
# import sys
#
#
# def insert_example_data():
#     task = Task("comprar verdura", "y luego mandar verdura")
#     db.session.add(task)
#     task = Task("ir al medico")
#     db.session.add(task)
#
#
# if __name__ == '__main__':
#     db.create_all()
#     params = sys.argv
#     # if len(params) == 2 and params[1] == "--examples":
#     #     insert_example_data()
#     db.session.commit()
