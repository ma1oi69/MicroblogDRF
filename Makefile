run-dev:
	docker compose up -d --build

shutdown-dev:
	docker compose rm -fs