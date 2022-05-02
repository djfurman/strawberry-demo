# strawberry-demo

This demo shows usage of the Strawberry GraphQL server

## Running the demo

1. Run `pipenv sync --dev` to install your virtual environment to match pinned dependencies 
1. Run `cp .env.example .env` to create your source control excluded environment configuration
1. Run `pipenv run flask run` to run Strawberry GraphQL within Flask's development server
1. Open your browser to [127.0.0.1:5000/graphql](http://127.0.0.1/graphql) to use the interactive discovery UI
1. Run the query below to see the results of our static data

```graphql
{
  books {
    title
    author
  }
  users {
    id
    name
    signupTs
    friends
  }
}
```

## Tests

Automation tests are written using pytest, but currently this requires the flask server to be running, so to currently run the tests, start the flask local development server and then run `pipenv run pytest` to execute an automated GraphQL query and assert that appropriate data was returned.

## Deployment

In order to deploy this service in Flask, you would follow typical Flask configuration (e.g., gunicorn with correct number of workers) and have Flask serve up the Strawberry GraphQL API.

Make sure to follow security practices such as containerized deployment, end-to-end encryption on the gunicorn server, load balancer with appropriate SSL configuration, and of course appropriate secrets management.