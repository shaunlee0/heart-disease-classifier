# Heart Disease Predictor

## Training the model

1. Change directory to the src directory: `cd src`

2. Run the script that trains the model: `./train.sh rf` where `rf` represents
the model to use in the model dispatcher, in this case this is a RandomForestClassifier.

## Starting the application in development mode

To start the application run the following command:

`gunicorn --bind 0.0.0.0:8080 wsgi:application -w 1`

## Testing the application in development mode

Test the application by using the following curl request which predicts false.

```bash
curl --location --request POST 'http://0.0.0.0:8080/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": {
        "0": 43
    },
    "sex": {
        "0": 1
    },
    "cp": {
        "0": 0
    },
    "trtbps": {
        "0": 132
    },
    "chol": {
        "0": 247
    },
    "fbs": {
        "0": 1
    },
    "restecg": {
        "0": 0
    },
    "thalachh": {
        "0": 143
    },
    "exng": {
        "0": 1
    },
    "oldpeak": {
        "0": 0.1
    },
    "slp": {
        "0": 1
    },
    "caa": {
        "0": 4
    },
    "thall": {
        "0": 3
    }
}'
```

Or this one which predicts true:

```bash
curl --location --request POST 'http://0.0.0.0:8080/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": {
        "0": 49
    },
    "sex": {
        "0": 1
    },
    "cp": {
        "0": 0
    },
    "trtbps": {
        "0": 130
    },
    "chol": {
        "0": 234
    },
    "fbs": {
        "0": 0
    },
    "restecg": {
        "0": 1
    },
    "thalachh": {
        "0": 163
    },
    "exng": {
        "0": 0
    },
    "oldpeak": {
        "0": 0.0
    },
    "slp": {
        "0": 2
    },
    "caa": {
        "0": 0
    },
    "thall": {
        "0": 2
    }
}'
```
# Docker

## Building the docker image

```sh
docker build --tag flask-app .
```

## Running the docker image

```sh
docker run -p 8080:8080 flask-app
```

## Testing the running image

```sh
curl --location --request POST 'http://0.0.0.0:8080/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": {
        "0": 49
    },
    "sex": {
        "0": 1
    },
    "cp": {
        "0": 0
    },
    "trtbps": {
        "0": 130
    },
    "chol": {
        "0": 234
    },
    "fbs": {
        "0": 0
    },
    "restecg": {
        "0": 1
    },
    "thalachh": {
        "0": 163
    },
    "exng": {
        "0": 0
    },
    "oldpeak": {
        "0": 0.0
    },
    "slp": {
        "0": 2
    },
    "caa": {
        "0": 0
    },
    "thall": {
        "0": 2
    }
}'
```

or

```sh
curl --location --request POST 'http://0.0.0.0:8080/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": {
        "0": 43
    },
    "sex": {
        "0": 1
    },
    "cp": {
        "0": 0
    },
    "trtbps": {
        "0": 132
    },
    "chol": {
        "0": 247
    },
    "fbs": {
        "0": 1
    },
    "restecg": {
        "0": 0
    },
    "thalachh": {
        "0": 143
    },
    "exng": {
        "0": 1
    },
    "oldpeak": {
        "0": 0.1
    },
    "slp": {
        "0": 1
    },
    "caa": {
        "0": 4
    },
    "thall": {
        "0": 3
    }
}'
```
