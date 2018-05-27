# python101

## Docker build 

```
docker build -t flask1 .
```

## Docker run

```
docker run -p 80:5000 -it flask1
```

## Verification

In your browser open http://localhost

## CURL commands

Get "existing" message:

```
curl http://localhost/message\?message_id\=1
```

Post "new" message:

```
curl -d "new_message=Testing sending a new message with spaces" -X POST http://localhost/message
```