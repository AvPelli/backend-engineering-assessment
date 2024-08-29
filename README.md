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


## API

/admin/: Admin site.

/api/quiz/: List and create quizzes.

/api/questions/: List and create questions.

/api/answers/: List and create answers.

/api/participants/: List and create participants.
