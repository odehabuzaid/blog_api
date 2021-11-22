## [Pull Request](https://github.com/odehabuzaid/blog_api/pull/4)

## djangoREST-api


### Tech stack

-   Django
-   Django REST Framework
-   SQLlite


### Database Schema

#### Posts

-   title
-   body
-   author

#### Vlogs

-   title
-   v_url
-   body
-   author

#### <ins>Routes API

#### VLog

Routes - HTTP

Description

`GET` **vlog/api/** 

Get all Posts

`GET` **/vlog/1/:id**

Get Single Post details

**vlog/api/**

`POST`

Create a Post
```json
{
    "title": "",
    "body": "",
    "author": null
}
```

**/vlog/api/:id**

`DELETE`

Delete a post

**/vlog/api/:id**

`PUT`

Update data of a post



#### Blog

Routes - HTTP

Description

`GET` **blog/api/** 

Get all Posts

`GET` **/blog/1/:id**

Get Single Post details

**blog/api/**

`POST`

Create a Post
```json
{
    "title": "",
    "body": "",
    "author": null
}
```

**/blog/api/:id**

`DELETE`

Delete a post

**/blog/api/:id**

`PUT`

Update data of a post



### Installation

```
git clone git@github.com:odehabuzaid/blog_api.git
cd blog_api
poetry install
python manage.py runserver
```