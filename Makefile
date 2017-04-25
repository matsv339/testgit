production: build
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

develop:
	docker-compose up -d

stop:
	docker-compose stop
	docker-compose rm -v

build:
	docker-compose build