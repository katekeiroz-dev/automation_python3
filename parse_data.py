import yaml

file_path = "user_config.yaml"

# Load YAML data safely
with open(file_path, "r") as file:
    data = yaml.safe_load(file)#It reads and parses YAML in a safe way.
    

# Print usernames and emails
for user in data["users"]:
    print("username:", user["username"], "| email:", user["email"])
