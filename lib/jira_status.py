from jira import JIRA

def jiraTransition(server, email, token, label, key, updated_Status):
    jiraOptions = {'server': f"{server}"}
    jira = JIRA(options=jiraOptions, basic_auth=(f"{email}", f"{token}"))
    jql_query = f'labels = {label} AND key = {key} ORDER BY created ASC'
    issue = jira.search_issues(jql_query)[0]
    print("Old status =", issue.fields.status)
    jira.transition_issue(issue, transition=updated_Status)
    issue = jira.search_issues(jql_query)[0]
    return issue.fields.status
