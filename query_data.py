# query_data.py
from app import app, db
from app.models import User

with app.app_context():
    # Query all users
    all_users = User.query.all()
    print("All Users:")
    for user in all_users:
        print(user.id, user.username, user.email)

    # Query a specific user by ID
    user_id_to_query = 1
    specific_user = User.query.get(user_id_to_query)
    if specific_user:
        print(f"\nUser with ID {user_id_to_query}:")
        print(specific_user.id, specific_user.username, specific_user.email)
    else:
        print(f"\nUser with ID {user_id_to_query} not found.")