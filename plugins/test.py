from time_entry_integration.models.res_users import load_user

users = load_user([])

for user in users:
    print(user.model_computed_fields)