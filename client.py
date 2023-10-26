import requests
body = {
    "age": 94,
    "sex": 1,
    "cp": 3,
    "trestbps": 140,
    "chol": 320,
    "fbs": 0,
    "restecg": 0,
    "thalach": 199,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
    }
response = requests.post(url = 'https://heart-model-service-myrosandrade89.cloud.okteto.net/score',
              json = body)
print (response.json())

