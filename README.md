
## Technologies used

* Flask
* Postgres
* Docker

## Project structure

```
.
├── diagrams                          # contains diagram files
│   ├── high_level_diagram.png              # high level diagram
│   └── sequence_diagram.png                # sequence diagram
├── flask_app                         # contains the flask app python files
│   ├── app.py                              # main app file
│   ├── db.py                               # contains database related logics   
│   ├── error_handler.py                    # error handling file
│   ├── query.py                            # contains sql query statements
│   └── validator.py                        # contains validations
├── tests                             # contains test case file       
│   └── test_cases.py                       # test case file
├── docker-compose.yml                # docker compose file
├── Dockerfile                        # docker file of flask app
├── rates.sql                         # contains data for the database
├── README.md                         # read me file  
└── requirements.txt                  # contains the required packages
```


## Diagrams

### High-level design diagram

![high_level_diagram](https://user-images.githubusercontent.com/41287354/201577708-8f93dd0b-5d45-4cdc-9d92-498b968c1e48.png)

## 

### Sequence diagram

![sequence_diagram ](https://user-images.githubusercontent.com/41287354/201577721-70f8c4d2-86b9-4b33-af35-60f47a63b6a1.png)


## Initial setup

Run the following command to set up the API and Postgres database.

```
docker-compose up -d --build
```

API will be available on `127.0.0.1:80`

## Testing

Execute the following command to install the libraries needed for testing.

```
pip install pytest requests
```

Once the libraries are installed, run the `pytest` command to begin testing.


## API Documentation

### Requests

HTTP Request : `GET http://127.0.0.1/rates`

#### Request Parameters

| Parameter     | Description                                                                             | Accepted Values            |  Type  |
|---------------|-----------------------------------------------------------------------------------------|----------------------------|:------:|
| `date_from`   | Start date of the date range for market rate calculation, inclusive. YYYY-MM-DD format. | 2016-01-01                 | String |
| `date_to`     | End date of the date range for market rate calculation, inclusive. YYYY-MM-DD format.   | 2016-01-10                 | String |
| `origin`      | Origin location for the market rate calculation. Either port code or region slug.       | CNSGH or china_east_main   | String |
| `destination` | Destination location for the market rate calculation. Either port code or region slug.  | NLRTM or north_europe_main | String |

#### Request Example
GET `http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main`

### Response

Response is returned in JSON format.

#### Response Parameters

| Parameter       | Description                                                                          |  Type  |
|-----------------|--------------------------------------------------------------------------------------|:------:|
| `day`           | Day within the given range including the start date and end date. YYYY-MM-DD format. | String |
| `average_price` | Average price of the day on a route between given port codes origin and destination. | Number |


#### Response Example
```
[
    {
        "day": "2016-01-01",
        "average_price": 1112
    },
    {
        "day": "2016-01-02",
        "average_price": 1112
    },
    {
        "day": "2016-01-03",
        "average_price": null
    },
    ...
]
```


