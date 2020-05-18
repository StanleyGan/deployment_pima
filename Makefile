COMMIT_ID=$(shell git rev-parse HEAD)

build-pima-api-heroku:
    docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/${HEROKU_APP_NAME}/web:${COMMIT_ID} .

push-pima-api-heroku:
    docker push registry.heroku.com/${HEROKU_APP_NAME}/web:${COMMIT_ID}
