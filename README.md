# U-Money Calculator

Небольшое Python-приложение для учёта личных средств.
Автоматизированный CI/CD процесс через GitLab:

- Этап `lint` — проверка стиля кода с flake8
- Этап `test` — тесты с pytest
- Этап `build` — сборка docker-образа и загрузка в GitLab Container Registry
- Этап `deploy` — автоматический деплой на сервер через SSH и docker-compose
