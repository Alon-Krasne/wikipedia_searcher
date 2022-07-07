# Wikipedia Searcher
![build](https://github.com/AlonKrasne/wikipedia_searcher/actions/workflows/test-wiki-searcher.yaml/badge.svg)
![Coverage](https://raw.githubusercontent.com/AlonKrasne/WikipediaSearcher/main/.github/coverage/coverage.svg?sanitize=true)


## Running
To run the project, use [pipenv](https://pipenv.pypa.io/en/latest/):
* `python3 -m pipenv install` - To build the environment and install dependencies
* `python3 -m pipenv run test` - To run unit tests
* `python3 -m pipenv run wiki_searcher` - To run the calculator CLI program

#### Using Docker Compose
To run the project using Docker Compose, use:

First time:
```bash
docker-compose up --build 
```

After:
```bash
docker-compose up
```

*You can also use the `-d` flag to run it in the background* 

## API Documentation
You can access 
```Bash
http://localhost:8000/docs
``` 
to see an interactive OpenAPI documentation