# MicroblogDRF

### Prerequisities
* Docker>=20.10.21
* docker compose>=2.13.0
* create `local.env` file similar to `example.env`. BUT DO NOT TOUCH db configuration values, just COPY THEM

## Backlog
* Добавить линтеров(ruff; black; isort; flake8; autoflake)
* Избавиться от пустых except
* Рейзить ошибки вместо их возврата
* Добавить wsgi сервер вместо использования development версии