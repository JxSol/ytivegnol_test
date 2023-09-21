# Test task for Longevity InTime
Current project contains RESTful API for authentication and authorization made with Django.
***
## Useful links
- API weblink: https://longevity.jxsol.online/api/v1/
- API Documentation: https://longevity.jxsol.online/api/docs

## Basic technologies
### ------- Backend -------
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)![version](https://img.shields.io/badge/3.11-gray) <br>
![Django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white)![version](https://img.shields.io/badge/4.2.4-gray) <br>
![DjangoREST](https://img.shields.io/badge/DjangoREST-800000.svg?style=flat&logo=Django&logoColor=white)![version](https://img.shields.io/badge/3.14.0-gray) <br>
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat&logo=PostgreSQL&logoColor=white)![version](https://img.shields.io/badge/15.3-gray) <br>
![Redis](https://img.shields.io/badge/Redis-DC382D.svg?style=flat&logo=Redis&logoColor=white)![version](https://img.shields.io/badge/7.0-gray) <br>
![Celery](https://img.shields.io/badge/Celery-37814A.svg?style=flat&logo=Celery&logoColor=white)![version](https://img.shields.io/badge/5.3.4-gray) <br>
### ------- DevOps -------
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)![version](https://img.shields.io/badge/24.0.2-gray) <br>
![Nginx](https://img.shields.io/badge/NGINX-009639.svg?style=flat&logo=NGINX&logoColor=white)![version](https://img.shields.io/badge/1.25.2-gray) <br>
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white)![version](https://img.shields.io/badge/20.1.0-gray) <br>

## Sample API requests
### 1. User registration
Sends an email with activation data. Use it to activate your account.
<br> `POST` https://longevity.jxsol.online/api/v1/users
```json
{
    "email": "mymail@example.com",
    "password": "bangbang12345",
    "first_name": "John",
    "last_name": "Wick"
} 
```
### 2. User activation
Activates your account with data from the activation letter.
<br> `POST` https://longevity.jxsol.online/api/v1/users/activation
```json
{
    "uid": "Mg",
    "token": "buvkku-cfa03651f13eac6dcc573f180c4c2f89"
} 
```
### 3. OTP sending
Sends an email with OTP for obtaining a login token.
<br> `POST` https://longevity.jxsol.online/api/v1/users/login
```json
{
    "email": "mymail@example.com",
    "password": "bangbang12345"
} 
```
### 4. User authentication
Responses with auth token for access to the API.
<br> `POST` https://longevity.jxsol.online/api/v1/token/login
```json
{
    "email": "mymail@example.com",
    "password": "bangbang12345",
    "otp": "123456"
} 
```
### 5. Access to your profile
Responses with your profile data.
<br> `GET` https://longevity.jxsol.online/api/v1/users/me
<br> `Authorization: Token f197e5b21938311f0896531d77416f692d870b22`

## Running a project on a production server
1. Open your server terminal.
2. Check that Git and Docker versions are up to date. 
You can find out how to do this on the Internet.
3. Open your project directory or create it.
4. Clone repository.
```sh
git clone https://github.com/JxSol/ytivegnol_test.git
```
5. Rename the file `.env.sample` to `.env`and fill its contents 
in accordance with the comments indicated next to the variables.
6. Run docker compose.
```sh
docker compose up -d
```
7. Project is deployed now.