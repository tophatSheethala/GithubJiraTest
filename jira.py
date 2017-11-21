#Here are the wrapper methods for JIRA
import requests
import json
import pprint

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic c2hlZXRoYWxhLnN3YW1pbmF0aGFuOkZyb290czE5NTk1"
}


def move_to_column(ticket_number, column):
    #some definition goes here
    transition_id = get_transition_id_from_column_name(ticket_number, column)
    payload = {
	   "transition": {
            "id": str(transition_id)
        }
    }

    url = create_base_url(ticket_number, "transitions")

    r = requests.post(
        url,
        json=payload,
        headers=headers
    )
    #Handle Errors here (If not found etc....)
    return r.status_code

def set_asignee(ticket_number, asignee):
    payload = {
        "name": asignee
    }

    url = create_base_url(ticket_number, "assignee")

    response = requests.put(
        url,
        json=payload,
        headers=headers
    )
    return response.status_code

def get_transition_id_from_column_name(ticket_number, column_name):
    url = create_base_url(ticket_number, "transitions")
    response = requests.get(
        url,
        headers=headers
    )
    data = response.json()
    for transition in data["transitions"]:
        if transition["name"] == column_name:
            return transition["id"]

def create_base_url(ticket_number, field):
    return "https://github-jira-integration.atlassian.net/rest/api/2/issue/{0}/{1}".format(ticket_number, field)
