import joblib
saved_data = joblib.load("priority_model.joblib")

print("Winner:", saved_data["winner"])

print("\nClasses:")
print(saved_data["classes"])

print("\nMembers:")

for i, member in enumerate(saved_data["members"]):

    print(f"\nMember {i}:")
    print("Type:", type(member))

    if isinstance(member, dict):
        for key, value in member.items():
            print(key, ":", type(value))

print("\nEncoders:")

for key, value in saved_data["encoders"].items():
    print(key, ":", type(value))