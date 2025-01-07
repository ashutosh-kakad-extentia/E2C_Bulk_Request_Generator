
# Python scripts to generate bulk Requests for Create and Update Scenario for Marken Custom Email-to-Case api testing 

<p align="right">-Ashutosh Kakad.</p>

### Files:
 - **Paramters.json**:    
 
        Contains the request parameters (subject, fromAddr, toAddr, sharePointLinks etc)
 - **createRequests.py**: 
 
        The python script which will create the bulk requests for Create Scenario 
 - **bulkRequests.json**: 
 
        After running the above script, the generated requests are stored here
 - **updateRequests.py**: 
 
        The python script which will create the bulk requests for Update Scenario 
 - **apiResponse.py**: 
 
        For update scenarios, caseRef is required for each case, those are to be pasted here. 
 - **updatedBulkRequests.py**: 
 
        After running the above updateRequests.py script, the generated requests are stored her



### Steps to create Requests:
- **Modify the Parameters.json file**:
     - **base_template:** defines the basic structure of you request, fill in subject, fromAddress, and body.
     - **email_groups:** Our scripts generate 100 requests.
    
        You can create all those 100 requests for a single mailbox like below: 


            "email_groups": [
                ["mil.test@marken.com", 100]
            ],
        or you can distribute the request for multiple mailboxes like below:


            "email_groups": [
                ["mil.test@marken.com", 33],
                ["sb.test@marken.com", 33],
                ["sr.test@marken.com", 34]
            ],
    
     - **(Optional)file_links:** if you want to include sharePointLinks you can define them here.

- **Run the createRequests.py script**:
     - Open your terminal using command: *ctrl + ~* and type in **python createRequests.py** and hit enter.
     - After the confirmation message appears on the terminal, check the **"bulkRequests.json"** file where all the generate requests will be stored.

- **Run the updateRequests.py script**:
     - After hitting the E2C api with this request you will receive the caseRef json in response. 
     - Paste this in its entirety in **"apiResponses.json"** file.
     - In your terminal, type in **python updateRequests.py**.
     - After the confirmation message appears on the terminal, check the **"updatedBulkRequests.json"** file where all the generate requests will be stored.
