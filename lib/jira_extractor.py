def jiraExt(issue):
    summaries = issue['fields']['summary']
    descriptions = issue['fields']['description']
    attachments = []
    # Extract attachments
    issue_attachments = issue['fields'].get('attachment', [])
    attachments.append([attachment['content'] for attachment in issue_attachments])
    comments = []
    # Extract comments
    issue_comments = issue['fields']['comment']['comments']
    comments.append([comment['body'] for comment in issue_comments])
    key = issue['key']
    status = issue['fields']['status']['name']

    return summaries,descriptions,attachments,comments, key, status