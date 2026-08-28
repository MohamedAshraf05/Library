# Library Project – Team Workflow Guide

This guide explains how the team should work on the project, organize the code, complete assigned tasks, and submit their work through GitHub.

---

## 1. Clone the Project

To get the project on your local machine, open your terminal and run:

```bash
git clone <repository_url>
```

Then navigate to the project directory:

```bash
cd Library
```

---

# 2. Project Structure

The project is divided into two main folders:

```text
Library/
│
├── Library/        # Main project configuration
│
└── apps/           # Contains all project applications
    │
    ├── auth/       # Authentication application
    │
    └── books/      # Core application
```

### Applications

* **auth** → Responsible for authentication-related features such as login, registration, logout, etc.
* **books** → The core application responsible for the main library functionality.

---

# 3. App Structure

Each application follows the same basic structure:

```text
app_name/
│
├── templates/
├── views/
└── models/
```

This structure helps keep the project clean and organized.

---

## 4. Creating Views

When you need to create a new view:

1. Go to the `views` folder inside your application.
2. Create a new Python file with a descriptive name.

For example:

```text
views/
├── __init__.py
├── login_view.py
└── register_view.py
```

Inside `login_view.py`, create your view:

```python
class LoginView:
    pass
```

After creating the file, you **must import the view inside the `__init__.py` file** in the `views` folder.

Example:

```python
from .login_view import LoginView
```

This keeps all views organized and allows them to be imported easily from one place.

---

## 5. Creating Models

The same structure should be followed for models.

For example:

```text
models/
├── __init__.py
├── user.py
└── book.py
```

After creating a model file, import it inside the `__init__.py` file:

```python
from .user import User
```

Always use descriptive file names that clearly explain the purpose of the model.

---

# 6. Templates Structure

The `templates` folder is responsible for all HTML files.

It should contain:

```text
templates/
│
├── base.html
│
└── pages/
    ├── home.html
    ├── login.html
    ├── register.html
    └── ...
```

### `base.html`

The `base.html` file contains the main design and structure shared across the project.

Other pages should extend it when needed.

Example:

```html
{% extends "base.html" %}

{% block content %}
    <h1>Home Page</h1>
{% endblock %}
```

### `pages/`

The `pages` folder contains the different pages of the application, such as:

* Home page
* Login page
* Registration page
* Forms
* Book pages
* Other application pages

---

# 7. Static Files

Each member can create and organize the static files needed for their task.

The basic static structure has already been prepared.

You can create the files you need, such as:

```text
static/
├── css/
├── js/
└── images/
```

Make sure to configure any required static files correctly in the Django `settings.py` file.

Only add the files that are necessary for your task and keep the structure clean.

---

# 8. Working With Branches

Each team member will work on their **own branch**.

The branch name should represent the task or application the member is responsible for.

For example:

```text
auth
```

This branch can be used by the member responsible for authentication.

Other examples:

```text
books
frontend
book-management
```

Before starting your work, switch to your assigned branch:

```bash
git checkout <branch_name>
```

To make sure you have the latest version of your branch:

```bash
git pull origin <branch_name>
```

---

# 9. Submitting Your Work

When you finish a part of your task, follow these steps.

### Check your changes

```bash
git status
```

### Add your changes

```bash
git add .
```

### Create a commit

Write a clear commit message describing what you completed:

```bash
git commit -m "Add login functionality"
```

### Push your work to GitHub

```bash
git push origin <branch_name>
```

---

# 10. Important Rule: Do Not Merge Into Main

⚠️ **DO NOT merge your branch into the `main` branch yourself.**

Your workflow should be:

```text
Work on your branch
        ↓
Test your changes
        ↓
Commit your changes
        ↓
Push to GitHub
        ↓
Inform the Team Leader
        ↓
Team Leader reviews the code
        ↓
Team Leader tests the feature
        ↓
Merge into main
```

Once you finish your assigned task:

1. Make sure your code is working.
2. Commit your changes.
3. Push your branch to GitHub.
4. Inform the **Team Leader** that your task is ready for review.
5. Wait for the code to be reviewed and tested.

The Team Leader will be responsible for reviewing the work and merging it into the `main` branch.

This workflow helps us:

* Avoid conflicts.
* Keep the `main` branch stable.
* Review code before adding it to the project.
* Detect bugs before merging.
* Keep the project organized.

---

# 11. General Rules

Please follow these rules while working on the project:

* Work only on your assigned branch.
* Do not push directly to the `main` branch.
* Use clear and descriptive file names.
* Use clear commit messages.
* Keep your code organized.
* Follow the project structure.
* Test your code before pushing.
* Do not modify another member's code unless necessary and approved.
* Inform the Team Leader when your task is ready.

---

# Final Workflow

```text
1. Clone the repository
        ↓
2. Switch to your assigned branch
        ↓
3. Pull the latest changes
        ↓
4. Complete your assigned task
        ↓
5. Test your code
        ↓
6. git add .
        ↓
7. git commit -m "Describe your changes"
        ↓
8. git push origin <your_branch>
        ↓
9. Inform the Team Leader
        ↓
10. Code Review & Testing
        ↓
11. Team Leader merges into main
```

## Remember

> **Your branch is your workspace. The `main` branch is the stable version of the project. Never merge your own work into `main` without approval.**
