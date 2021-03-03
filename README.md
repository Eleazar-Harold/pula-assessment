## [PULA INTERVIEW: Sourcing Service]
###### The service handles all sourcing service requests. Rest Endpoint documentation is provisioned withing the service

### Technology Stack ###
* [Django](https://docs.djangoproject.com/en/3.0/releases/2.2.19) 2.2.19, 
* [Python](https://www.python.org/downloads/release/python-3710) Python 3.7.10,
* [Vue.js](https://vuejs.org/) [Vue 2.x](https://vuejs.org/v2/guide/)
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest) to manage all dependencies (and sub-dependencies)


### App Propagation ###

###### For Development ######
1. Run `sh destroy-dev.sh && sh deploy-dev.sh` from the project root folder to build the images and run the containers.
2. Test it out by loading [api documentation](http://localhost:4000/swagger/).

NB: The script `deploy-dev.sh` will build the service, create migrations, run migrations and propage the service build.

###### For Production ######
1. A little more configuration will be required for the production set up, thought the procedure is similar to the development setup.
2. Run `sh deploy-prod.sh` from the project root folder to build the images and run the containers.
3. Test it out by loading [api documentation](http://localhost:4000/swagger/).

###### Environment File ######
Example `.env.dev.example` file:

```bash
PG_DB_PSWD=
PG_DB_USER=
PG_DB_NAME=
PG_DB_HOST=
PG_DB_PORT=
DJANGO_SETTINGS_MODULE=core.settings.dev #for development else core.settings.prod
REDIS_URL=
PROD=
```

### Contribution guidelines ###

* Code review
* Other guidelines
* Contact [repo owner](mailto:eleazar.yewa.harold@gmail.com) for more details.
