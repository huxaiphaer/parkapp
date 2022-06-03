# PeterPark.

This is the parking application.


### Requirements for setting up the project.
1. Python3. 
2. Flask
3. Virtualenv.
4. Docker.
5. Postgres DB

### Installation on Mac

1 . First clone this repository 

```
$ git clone https://github.com/huxaiphaer/travel_huxy.git
```

2 . Add the following variables in your Environment Variables permanently:

```
FLASK_APP=run.py
DATABASE_URL=postgres://captiq:namungoona@localhost:5432/peterpark
SECRET_KEY=my_secrete_key
APPLICATION_HOST=0.0.0.0
APPLICATION_PORT=5002
APPLICATION_DEBUG=False
```

After, setting up the environment variables add create a Postgres Database called `huxy_tours`, followed by running SQLAlchemy migrations with the commands 
below to create all the necessary tables :


**NOTE :**
- The commands below won't run unless  you have your Redis server running and as well
as setting all the environment variables above.

```
$ flask db init
$ flask db migrate
$ flask db upgrade

```


3 . Then, create a virtual environment and install in on Mac :

```
$ virtualenv env
$ source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```
$ pip3 install -r requirements.txt
```

## Running with Docker.

The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```python3

 $ docker-compose up --build

```



 #### Endpoints.

| HTTP Method | End Point     | Action                 |
|-------------|---------------|------------------------|
| POST        | api/v1/plate  | Submit a plate         |
| GET         | /api/v1/plate | Get all number plates. |
| GET         | api/v1/search-plate?key=1234&levenshtein | Search number plates.  |


### Improvements
 Due to time being as a factor the following were left out, but they could improve on the 
 experience :
 
 - _Exhausting more on unit tests_.
 - _Handling levenshtein search_

### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)