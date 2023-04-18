import requests

teste1 = requests.get("http://localhost:5000/get")
print(teste1.json(), teste1.status_code)

teste2 = requests.get("http://localhost:5000/get/senha?senha=1234")
#Tem que printar {"response": "OK, acesso permitido"}
print(teste2.json(), teste2.status_code)

teste3 = requests.get("http://localhost:5000/get/senha?senha=12345")
#Tem que printar {"Error": "Senha invalida, acesso negado"}
print(teste3.json(), teste3.status_code)
