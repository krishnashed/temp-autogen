from flask import Flask, request
from libs import jiraTransition, run_pair_programmer, gherkinGen, jiraExt

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_jira_webhook():
    issue = request.json
    server = "https://llm-jira-solver.atlassian.net/"
    email = "riteshjbhattad@gmail.com"
    jiraToken = "ATATT3xFfGF0cR1v4vkV0QcPjFs5FdN-5Ty8QckvCDtYXGwoDOfTKNBuPlHE81YyO0KTC0kzcR7MMZ6j55CpcfE2xkIuIz0LpP5iaJ93EoW8fr-e2TJxbTNlovUSZGYjvaWnP1jIN7xWkV9Fz13iyYQ2OavZFR8hOWDiB9qx5Gsc8yf0bQ5oL5A=7DEFC8F9"
    label = "Dev-tests"
    
    summary, description, attachments, comments, key, status = jiraExt(issue)
    print(f"Current Status of {key}: {status}")
    print(f"Jira issue: [Summary{summary}, Description: {description}, Attachments: {attachments}, Comments:{comments}, status: {status}", sep="\n")
    # gherkin_scenarios = gherkinGen(description)
    # print(f"Gherkin Scenarios generated: {gherkin_scenarios} \n")
    run_pair_programmer(description)
    #your eval and other functions
    updated_Status = 'Done'
    print(f"New Status: {jiraTransition(server, email, jiraToken, label, key, updated_Status)}")


    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Runs on http://localhost:5002