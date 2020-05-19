NAME=pima-api

build-pima-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/${HEROKU_APP_NAME}/web .

push-pima-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest

build-pima-api-aws:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t $(NAME):$(COMMIT_ID) .

push-pima-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/$(NAME):latest

tag-pima-api:
	docker tag $(NAME):latest ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-2.amazonaws.com/$(NAME):latest
