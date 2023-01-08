import requests
import os

class PRException(Exception):
    pass

def check_pr():
    # Set the repository owner and name
    owner = "Anoopkr"
    repo = "spring-boot-angular-examples"

    # Set the authentication parameters (if necessary)
    PAT = os.getenv("PAT")
    auth = ("Anoopkr", PAT)

    # Set the headers
    headers = {"Accept": "application/vnd.github+json"}

    # questions1 = ["Is this a fix for something broken from the user perspective? What is broken?", "What is the new behavior after the fix?", "Root cause. When did the breakage start to happen in production?",
    #             "How/Where did you test your change?", "Link to other PRs dependent to this change (config, client, server)", "Previous PRs(list all) that this is a fix for", "Which other areas should QA do regression on?"]

    questions = ["Is this a fix for something broken from the user perspective? What is broken?", "What is the new behavior after the fix?", "Root cause. When did the breakage start to happen in production?",
                "How/Where did you test your change?", "Link to other PRs dependent to this change (config, client, server)", "Previous PRs(list all) that this is a fix for", "Which other areas should QA do regression"]

    # Send the GET request
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls", auth=auth, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        # Print the list of pull requests
        pull_requests = response.json()
        for pull_request in pull_requests:
            print(pull_request["url"])
            response = requests.get(
                f"{pull_request['url']}", auth=auth, headers=headers)
            if response.status_code == 200:
                comment = response.json()
                print(comment["body"])
                if comment["body"] is None:
                     print(f"No description")
                     raise PRException("No description")
                if all_elements_in_string(questions, comment["body"]):
                    print('All questions are present in the description')
                    count = 0

                    while count < len(questions)-1:
                        result = get_string_between(comment["body"], questions[count], questions[count+1])
                        if len(result.strip()) < 3:
                            print(f"{questions[count]} not answered")
                            raise PRException(f"{questions[count]} not answered")
                        count += 1

                    # for index, question in enumerate(questions):
                    #     # print(question)
                    #     result = get_string_between(comment["body"], questions[index], questions[index+1])
                    #     print(result)
                else:
                    print('Not all questions are present in the description') 
                    raise PRException("Not all questions are present in the description")

    else:
        # Print the error message
        print(response.json()["message"])


def all_elements_in_string(elements, string):
    return all(element in string for element in elements)

def get_string_between(paragraph, start_string, end_string):
    start_index = paragraph.find(start_string)
    if start_index == -1:
        return ""
    end_index = paragraph.find(end_string, start_index)
    if end_index == -1:
        return ""
    return paragraph[start_index + len(start_string):end_index]

check_pr()
