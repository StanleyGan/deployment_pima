build-pima-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/${HEROKU_APP_NAME}/web .

push-pima-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest
