"""
Seed initial data into database.

Run:

python -m app.database.seed
"""

from app.database.database import SessionLocal

from app.models.user import User

from app.models.hcp import HCP


def seed():

    db = SessionLocal()

    try:

        if db.query(User).count() == 0:

            users = [

                User(
                    name="Vivek Choudhary",
                    email="vivek@example.com",
                    territory="Delhi",
                ),

                User(
                    name="Rahul Sharma",
                    email="rahul@example.com",
                    territory="Mumbai",
                ),
            ]

            db.add_all(users)

        if db.query(HCP).count() == 0:

            doctors = [

                HCP(
                    doctor_name="Dr. Rajesh Sharma",
                    speciality="Cardiology",
                    hospital="Apollo Hospital",
                    city="Delhi",
                    phone="9876543210",
                ),

                HCP(
                    doctor_name="Dr. Neha Verma",
                    speciality="Diabetology",
                    hospital="Fortis Hospital",
                    city="Noida",
                    phone="9876501234",
                ),

                HCP(
                    doctor_name="Dr. Amit Gupta",
                    speciality="Neurology",
                    hospital="Max Hospital",
                    city="Gurgaon",
                    phone="9811122233",
                ),
            ]

            db.add_all(doctors)

        db.commit()

        print("Database seeded successfully.")

    except Exception as e:

        db.rollback()

        print("Error:", e)

    finally:

        db.close()


if __name__ == "__main__":
    seed()
