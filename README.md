# Simple Flask App

## About

## How to Install and Run

### Development Container

This uses the default Flask development server. You can set your own environment variables in _.env.dev_ and _docker-compose.yml_.

Build the images:

```
$ docker-compose up -d --build
```

View it at [http://localhost:5000](http://localhost:5000). Any changes made within the 'web' folder will be applied automatically without having to rebuild the container.

### Production Container

Uses gunicorn + nginx.

Rename _.env.prod-sample_ to _.env.prod_ and _.env.prod.db-sample_ to _.env.prod.db_, and set your own environment variables.
Build the images:

```
$ docker-compose -f docker-compose.prod.yml up -d --build
```

To create/rebuild the database (**This will remove any existing database**):

```
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

View it at [http://localhost:1337](http://localhost:1337). To apply changes, the images must be rebuilt.

## How to Use

## Licence

MIT License

Copyright (c) 2022 Fred Luckham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
