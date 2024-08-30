# Engineering Assessment

Starter project to use for the engineering assessment exercise

## Requirements
- Docker
- docker compose

## Getting started
Build the docker container and run the container for the first time
```docker compose up```

Rebuild the container after adding any new packages
``` docker compose up --build```

The run command script creates a super-user with username & password picked from `.env` file
with the following credentials:
username:admin
password:admin


During the first run 2 dummy quizzes are generated

## API
root url should be "http://localhost:8000/"

/admin/: Admin site. All objects can be manually created here

/quiz/{id}: Simple quiz page

/api/quiz/: List and create quizzes.

/api/questions/: List and create questions.

/api/answers/: List and create answers.

/api/participants/: List and create participants.

/api/quiz/{quiz_id}/questions/: (GET) quiz questions

/api/participants/{user_id}/quizzes/: (GET) user's quizzes
/quizzes/{user_id}: redirects to URL above^


## Running tests
In docker container console run this command: "python manage.py test quiz.tests"