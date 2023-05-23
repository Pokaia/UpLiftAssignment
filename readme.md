# Take Home Assignment

## We're building a matching engine and need your help!

You are tasked with creating a light-weight service for sorting, ranking, and displaying a list of skilled service providers. Providers have several attributes which are filterable.
The service should factor in these attributes as well as factors related to the use of the service when generating results.
Below are several user stories which outline the functionality expected in this service, as well as an attached `.json` file with some mock provider data to seed the project. The service can be expressed in any way you choose, as long as there is an interface to generate a list of providers based on the requirements in the user stories.
Please use Python to code the service.

## User Stories

- I would like to be able to exclude/include certain providers from results based on their active property
- I would like to be able to filter through providers on a combination of any of their user traits
- I would like the order of results to adjust based on how many times a provider has been returned; surfacing providers who have been returned fewer times towards the front of the list.
- I would like higher ranked providers to always be surfaced towards the front of the list.

## The user stories purposefully leave room for interpretation and flexibility in how you decide to implement them; don't overthink them. The point of this exercise is to create a body of work we can discuss / review in the followup. Feel free to bring in any other interesting ideas/concepts you would like in a matching engine.

## Things we're looking out for in our review:

- Extensibility of code
- Consistency
- Organization of code
- Familiarity with Python
- Documentation if necessary
- Tests

Please send either a zip of the code or a link to github/gitlab where they're storing the code. Let me know if you have any questions!


## Instructions to run

# Create a virtual environment
    python3 -m venv env
    source env/bin/activate

# Install dependencies
    pip install -r requirements.txt
 
# Create a superuser account
    python3 manage.py createsuperuser
Fill in prompts. This step is only needed if you want to test the admin site

# Load Test Data
    python3 managy.py loaddata providers/fixtures/testData.json

# run tests
    python3 manage.py test

# run localserver
    python3 manage.py runserver
 
# URLs for sampling
- 'http://127.0.0.1:8000/admin/' - admin site (need a superuser to access)
- 'http://127.0.0.1:8000/providers/' - get a list of all providers
- 'http://127.0.0.1:8000/providers/?active=true' - list active users
- 'http://127.0.0.1:8000/providers/?first_name=Elisabetta&sex=Male' - list users with filters
