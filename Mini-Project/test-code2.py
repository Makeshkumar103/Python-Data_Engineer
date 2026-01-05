import sys

if len(sys.argv) == 2:
    print("Usage: python email_generator.py 'Full name and last name'")
    sys.exit()

full_name = sys.argv[1]
last_name = sys.argv[2]

# Format the name

#email = full_name.lower().replace(_old:" ", _new:".") + "@company.continue"
email = full_name.lower().replace(" ",".") + "@company.continue"

# output
print("\n--- Your profile ---")
print("Full Name : ", full_name)
print("General Email : ", email)