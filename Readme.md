# SWE1 Polls App

[![Build Status](https://travis-ci.com/anushkagarg-30/swe1-app.svg?branch=deployment)](https://travis-ci.com/anushkagarg-30/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/anushkagarg-30/swe1-app/badge.svg?branch=deployment)](https://coveralls.io/github/anushkagarg-30/swe1-app?branch=deployment)

This is a simple Django application built by **Anushka Garg** as part of SWE1 coursework.  
It follows the official [Django Tutorial Parts 1–4](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) and is deployed to AWS Elastic Beanstalk.

---

## 🔗 Live Links

- **GitHub Repository**: [https://github.com/anushkagarg-30/swe1-app](https://github.com/anushkagarg-30/swe1-app)
- **Deployed Application**: [https://your-app-env.elasticbeanstalk.com/polls](https://your-app-env.elasticbeanstalk.com/polls)  
  *(replace this with your actual AWS EB URL after deployment)*

---

## 🚀 Features

- List recent polls
- Vote on choices
- See results
- Admin interface for managing polls
- Uses Django class-based generic views

---

## 🛠️ How to Run Locally

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/anushkagarg-30/swe1-app.git
cd swe1-app

# Create and activate virtual environment
python -m venv env
.\env\Scripts\activate   # Windows
# source env/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run
python manage.py migrate
python manage.py runserver
