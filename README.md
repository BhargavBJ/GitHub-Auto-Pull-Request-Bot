
---

# GitHub-Auto-Pull-Request-Bot

## Introduction

Recruiters often don't focus on the specific projects you have worked on, but rather the activity and frequency of contributions displayed on your GitHub profile. A higher number of commits and pull requests can showcase your dedication, engagement with development, and ability to contribute consistently to projects. 

The **GitHub-Auto-Pull-Request-Bot** is an automated solution designed to help you maintain active contributions on GitHub by automatically generating pull requests. The bot creates random commits to your repository, enabling frequent updates and pull requests without manual intervention, ensuring that your GitHub activity remains visible and updated.

## Features

- **Automatic Pull Request Generation**: The bot creates pull requests automatically based on predefined configurations.
- **Random Commit Content**: Each commit contains randomly generated sentences, ensuring variety and constant activity.
- **Customizable Frequency**: You can configure the bot to create a specified number of pull requests per day.
- **GitHub API Integration**: Uses GitHub's API to automate pull request creation and repository interactions.
- **Logging**: The bot logs its activity, allowing you to track every commit, PR creation, and any errors encountered.

## Directory Structure

```
auto-pr-bot/
├── config/
│   ├── config.py             # Configuration file for API keys, repo details, and other settings
├── logs/
│   ├── bot_activity.log      # Log file for tracking the bot's activity (commits, PRs, errors)
├── src/
│   ├── __init__.py           # Marks the directory as a package
│   ├── auto-pr-bot.py        # Main script that automates the PR generation and commit process
│   ├── utils.py              # Utility functions like random sentence generation
│   ├── github_api.py         # Handles GitHub API calls (PR creation, repo interaction)
│   ├── git_operations.py     # Git operations (checkout branches, commit, push, etc.)
├── data/
│   ├── random_sentences.txt  # Store any pre-generated sentences (optional)
├── requirements.txt          # Python dependencies required for the project
├── README.md                 # Project overview, setup instructions, and usage
└── run_bot.py                # Entry point to run the bot
```

## Setup Instructions

1. **Clone the Repository**

   Begin by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/GitHub-Auto-Pull-Request-Bot.git
   cd GitHub-Auto-Pull-Request-Bot
   ```

2. **Install Dependencies**

   Install the necessary Python dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API and Repository Details**

   Update the `config/config.py` file with your GitHub username, token, repository name, and other configuration details:

   ```python
   GITHUB_USERNAME = "your_github_username"
   GITHUB_TOKEN = "your_github_token"
   REPO_NAME = "your_repo_name"
   TARGET_FILE = "your_target_file.txt"
   LOCAL_REPO_PATH = "your_local_repo_path"
   DEFAULT_BRANCH = "main"
   GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
   NUM_PRS_PER_DAY = 15
   ```

4. **Run the Bot**

   You can now run the bot by executing the following:

   ```bash
   python run_bot.py
   ```

   The bot will start creating pull requests on your specified repository, adding random sentences in commits, and pushing them automatically.

## Dependencies

This project requires the following Python packages:

- `requests`
- `gitpython`

To install these dependencies, you can run:

```bash
pip install -r requirements.txt
```

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Feel free to fork this repository, make improvements, and create pull requests. Any contributions are welcome!

---

