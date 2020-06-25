# YouTube API

### Build image

```
sudo docker-compose run api django-admin startproject fampay .
```
### Run server

```
docker-compose up       
```

### Paginated response for video details

```
curl --location --request GET 'http://0.0.0.0:8000/api/videos/'     
```

### Api for searching videos on title, description
```
curl --location --request GET 'http://0.0.0.0:8000/api/videos/?search=best'  
```

### Background task for youtube api

Task for calling youtube api in background is not fully automated.
```
curl --location --request GET 'http://0.0.0.0:8000/api/task'
```
It requires calling above endpoint for one time after that it schedules tasks every 60 sec.

