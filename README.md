# AWSGPT

AWSGPT - Your assistance for any AWS code or search

## Overview

Today, I'm excited to present a project that I've been working on for quite some time. The project is called AWS GPT, and it's currently in its alpha stage.You might be asking, "Why do we need AWS GPT when we already have ChatGPT and other large language models?" Well, this project was born out of two main motivations:
1. Whenever I search for AWS-related code in ChatGPT, I find myself wishing there was a button to execute the code directly in my AWS account, eliminating the need for copy-pasting. While this might sound like a security concern for some, I recommend using this tool in a pre-production environment.
2. ChatGPT's last training data was updated in September 2021. This means it doesn't have information on any features released after that date. I am working on integrating this with Facebook's Llama2, allowing users to train their own models with there own data to get more up-to-date information.

## Demo Video


[![Watch the Video](https://raw.githubusercontent.com/100daysofdevops/awsgpt/main/img/awsgpt.ico?token=GHSAT0AAAAAACG73UCDPYAPOZYS46XW37PIZHRPQNQ)](https://www.youtube.com/watch?v=8chae6d97-4)


## Prerequisites
- Python 3.x
- Bash shell
- An OpenAI API key
- AWS Access Key ID and Secret Access Key
- Streamlit
- A `requirements.txt` file for your Python dependencies


## Installation

```bash
git clone https://github.com/100daysofdevops/awsgpt.git
```

## Usage

```python
source setup_environment.sh
```

## Phase1 Features

* **Search and Execute Code**: Allows you to search for AWS code snippets and execute them.
* **Search for Documentation**: Provides quick access to relevant AWS documentation.
* **Basic Authentication**: Comes with a super secure default username and password (`admin/admin`).
* **Basic Search History**: Keeps a history of your recent searches .

## Phase 2 Features (Upcoming)

* **Search Within Your Own Documents**: Enables you to perform searches within your own uploaded or linked documents.
* **Integration with Third-Party Authentication**: Supports third-party authentication methods like Google or Okta.
* **Clickable Search History**: Allows you to click on your search history items to retrieve complete previous results.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
