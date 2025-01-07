import json

input_requests_file = "bulkRequests.json"
input_responses_file = "apiResponses.json"
output_file = "updatedBulkRequests.json"

with open(input_requests_file, "r") as f:
    email_requests = json.load(f)

with open(input_responses_file, "r") as f:
    api_responses = json.load(f)
    
for request, response in zip(email_requests, api_responses):
    if response.get("caseRef"):
        request["caseRef"] = response["caseRef"]

with open(output_file, "w") as f:
    json.dump(email_requests, f, indent=2)

print(f"Updated email requests with caseRefs saved to {output_file}")
