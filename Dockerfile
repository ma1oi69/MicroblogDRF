FROM python:3.9-slim

ARG GROUPID=1001
ARG USERID=$GROUPID
ARG USERNAME=appuser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -g $GROUPID $USERNAME && adduser --uid $USERID --gid $GROUPID --no-create-home $USERNAME

WORKDIR /home/app

COPY --chown=$USERNAME:$USERNAME ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY --chown=$USERNAME:$USERNAME . .

USER $USERNAME
WORKDIR /home/app/drfsite
CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]