import json

def load_config(config_file):
    with open(config_file, "r") as f:
        return json.load(f)

def generate_email_requests(start, end, base_template, email_groups, file_links):
    email_requests = []
    link_count = len(file_links)

    current_index = 0
    for group_email, group_count in email_groups:
        for _ in range(group_count):
            if current_index >= end - start + 1:
                break
            request = base_template.copy()
            request["subject"] += f" #{start + current_index}"
            request["originAddress"] = group_email
            request["toAddress"] = group_email
            request["fileLinks"][0]["fileLink"] = file_links[current_index % link_count]
            email_requests.append(request)
            current_index += 1

    return email_requests

# Load configuration from external JSON file
config_file = "Parameters.json"
config_data = load_config(config_file)

base_template = config_data["base_template"]
email_groups = config_data["email_groups"]
file_links = config_data["file_links"]

start_subject = 1
end_subject = 100
email_requests = generate_email_requests(start_subject, end_subject, base_template, email_groups, file_links)

output_file = "bulkRequests.json"
with open(output_file, "w") as f:
    json.dump(email_requests, f, indent=2)

print(f"Email requests generated and saved to {output_file}")
