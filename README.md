# performance-api
Provides performance metrics from the Data Collection Pipelines

## Postgrest spike

As part of Trello ticket, a prototype version of the Performance API has been implemented using PostgREST.

This prototype version mounts the init.sql file to a Postgres docker container to create the initial schema and insert
some example data.

### Pre-requisites

 * Docker (including Docker Compose)
 * Access to host ports 3000, 54320 and 8080

### Run

Execute the docker compose setup:

```
docker compose up -d
```

## Try

### View Swagger/OpenAPI spec:

```
curl --location 'http://localhost:3000'
```

### List organisation summaries

```
curl --location 'http://localhost:3000/organisations'
```

### List organisation summary for Borchester Council

```
curl --location 'http://localhost:3000/organisations?id=eq.BOR'
```

### List dataset summaries for Borchester Council organisation

```
curl --location 'http://localhost:3000/organisations?id=eq.BOR&select=datasets(*)'
```

### List dataset summaries for Borchester Council dataset

```
curl --location 'http://localhost:3000/datasets?organisation_id=eq.BOR'
```

### List dataset summaries for Tree dataset

```
curl --location 'http://localhost:3000/datasets?dataset=eq.Tree'
```