# Implementation

## Design
The design of this project is divided into the following parts:

1. `create_shortlink`: The function that handles the `/shorlinks` post endpoint. Because this is let's say our 'main' func we need need to increase our **cohesion** by decoupling our logic into different components
2. `shorty`: The `Shorty` class is our requests handler responsible for validating the request params and abstracting the url shortening logic for the different providers. We achieve this by using the factory pattern which separates creation from use. Shorty is also responsible for handling any provider logic failure by utilizing the rest of the available providers.
3. `providers`: The `providers` module contains classes that serve as our external api wrappers responsible for processing the external api's response and handling any external api erros.
4. `validators`: the validator class is responsible for validating the correctness of our input params
4. `errors`: Crucial to our app is the error hanling for our different components. By creating custom errors with appropriate status code and messages, we can track the trace of our errors in a cleaner manner
4. `tests`: Testing is the most crucial part in a development enviroment. The tests are separated into functional and unit tests. Emphasis was given in :

    a. testing the functionality of our api end to end

    b. testing the functionality of our `Shorty` handler in normal and edge cases

    c. testing our pure functions

## Scope 
The scope of this project, from my perspective, is to show my skills in writing production level code which can be easily maintained, tested and deployed. Therefore i wrote the app in microservice oriented design. For this reason, containerization of the project is supported.  

## Running the app
### Local env
```
cd shorty-app
```
In current dir run 
```
setup_venv.sh 
```
to create the python virtual env.

Then 
```
python run.py
```

To run tests

```
pytest tests/
```

### Remote/Dockerized env
In the project folder

```
docker-compose -f docker-compose.services.yml build shorty-app
docker-compose -f docker-compose.services.yml up shorty-app
```

In both cases, you need to pass your api tokens to receive external apis valid response either hardcoded or as an env variable.

You can inspect the api in `http://127.0.0.1:5000/apidocs/` via the Swagger UI

## Improvements / Best Practices
Integrating external APIs to our platform could impact severely our app's functionality. Therefore the goto solution is to 
apply the following best practices

1. **Timeouts**:

    Setting a timeout could prevent freezing our app from possible external api delays
2. **Fallback logic:**

    In our case one of our short url providers might be down so we need to apply a fallback mechanism to trigger another supported service for fetching the shortened url
3. **Batching:**

    External apis provide batching support (in our case, a list of url to shorten). Implementing a batching mechanism we could reduce externall api calls therefore reducing costs and network traffic
4. **Rate limiting:**
    
    Various performance gains
5. **Caching:**

    Caching support is crucial to our system. Storing api responses for a specific url could reduce external api calls and response time. Database Management and caching could be supported in our app, nonetheless i believe this is out of scope for this assesment. We could further discuss on the specifics in later stages.