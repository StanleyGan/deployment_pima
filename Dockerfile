FROM python:3.6.10

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' pima-api-user

WORKDIR /opt/pima_api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run_app.py

# Install requirements, including from Gemfury
ADD ./pima_package/pima_api /opt/pima_api/
RUN pip install --upgrade pip
RUN pip install -r /opt/pima_api/requirements.txt

RUN chmod +x /opt/pima_api/run.sh
RUN chown -R pima-api-user:pima-api-user ./

USER pima-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]
