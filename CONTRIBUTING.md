# Contributing to White Knight

First off, thank you for considering contributing to White Knight! We're excited to see the open-source community help grow and improve this project.

**A Little About Me & This Project:**

I've been coding for many years, and I love building software. However, White Knight is my first venture into Python as a primary language for a project. This means that while I bring a lot of software development experience, I'm still learning the Python-specific ropes and best practices. I'm incredibly open to feedback, suggestions, and contributions that can help make this project better and more idiomatic Python. Your expertise, whether you're a seasoned Pythonista or also learning, is highly valued!

## How Can I Contribute?

There are many ways you can contribute to White Knight, and we appreciate all of them:

### Reporting Bugs
If you encounter a bug, please help us by submitting an issue to our [GitHub Issues page](https://github.com/geoscope/white-knight-loader/issues).

When reporting a bug, please include:
* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.
* What you expected to happen.
* What actually happened.
* Screenshots or error messages if applicable.

### Suggesting Enhancements
If you have an idea for a new feature or an improvement to an existing one, please open an issue on our [GitHub Issues page](https://github.com/geoscope/white-knight-loader/issues).
* Use a clear and descriptive title.
* Provide a step-by-step description of the suggested enhancement in as many details as possible.
* Explain why this enhancement would be useful to other White Knight users.
* You might want to include code snippets, screenshots, or mockups.

### Pull Requests
We love pull requests! If you're planning to contribute code, please follow these steps:

1.  **Fork the Repository:** Start by forking the White Knight repository to your own GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine:
    ```bash
    git clone [https://github.com/geoscope/white-knight-loader](https://github.com/geoscope/white-knight-loader).git
    cd [white-knight-loader]
    ```
3.  **Create a Branch:** Create a new branch for your changes. Please use a descriptive branch name (e.g., `fix/button-bug` or `feat/new-user-auth`).
    ```bash
    git checkout -b name-of-your-new-branch
    ```
4.  **Set Up Your Environment (Python Specific):**
    
    This project uses Poetry for python version and dependency management. To get started, install Poetry using their [instructions](https://python-poetry.org/docs/).
    Then go into the project directory type the following once to initialise the project:
    
    ```bash
    poetry init
    ```
    
5.  **Make Your Changes:** Write your code and make sure to follow the coding style (see "Coding Standards" below).
6.  **Test Your Changes:**
    * Please add tests for any new features or bug fixes.
    * Ensure all tests pass before submitting your pull request.
        ```bash
        # (Command to run tests, e.g., pytest, python -m unittest)
        pytest
        ```
7.  **Lint Your Code:** We aim for clean, readable code. Please lint your code before committing.
    ```bash
    #
    black .
    ```
8.  **Commit Your Changes:** Use clear and concise commit messages.
    ```bash
    git add .
    git commit -m "feat: Add amazing new feature"
    ```
    (Consider using [Conventional Commits](https://www.conventionalcommits.org/) if you like structured commit messages).
9.  **Push to Your Fork:**
    ```bash
    git push origin name-of-your-new-branch
    ```
10. **Open a Pull Request (PR):**
    * Go to the original White Knight repository on GitHub.
    * Click on "New Pull Request".
    * Choose your branch to compare and create the PR.
    * Provide a clear title and description for your PR, explaining the changes and referencing any relevant issues (e.g., "Fixes #123").

## Coding Standards

* **PEP 8:** Please follow [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). Most linters (like Flake8) will help enforce this.
* **Docstrings:** Write clear docstrings for all modules, classes, functions, and methods. We generally follow [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).
* **Type Hinting:** We encourage the use of [Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/) for better code clarity and maintainability, especially since I'm still deepening my Python knowledge!
* **Readability:** Write code that is easy to understand. Add comments where necessary to explain complex logic.

## Development Setup

Beyond the Python-specific environment setup mentioned in the "Pull Requests" section:
* Make sure you have Python 3.x installed (specify your version, e.g., Python 3.8+).
* Git is required for version control.

*(Add any other specific setup instructions for your project here, e.g., database setup, API keys, etc.)*

## Code of Conduct

We want to foster an open and welcoming environment. All contributors are expected to adhere to our [Code of Conduct](LINK_TO_CODE_OF_CONDUCT.md). Please read it before contributing.

*(If you don't have a CODE_OF_CONDUCT.md yet, you can create one. A popular option is the Contributor Covenant: https://www.contributor-covenant.org/)*

## Getting Help

If you have questions or need help with your contribution, please feel free to:
* Open an issue on GitHub and tag it as a "question".
* (Optional: Add other communication channels like a Discord server, mailing list, etc.)

## A Final Thank You!

Your contributions are valuable. As this is my first Python project, I'm especially grateful for your patience, guidance, and willingness to help. Let's build something great together!

---

**Remember to replace the bracketed placeholders like `White Knight`, `link-to-your-issues-page`, and `YOUR_USERNAME` with your actual project details.**

You'll also want to:
1.  Create a `CODE_OF_CONDUCT.md` file if you link to one.
2.  Ensure your `requirements.txt` (and potentially `dev-requirements.txt`) are up to date.
3.  Specify the actual commands for running tests and linters if they differ from the examples.
4.  Link to your GitHub issues page correctly.

Good luck with your project!