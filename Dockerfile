FROM python:3.11-slim

WORKDIR /app
COPY ./app /app
COPY ./.env /app/.env

ADD crontab /etc/cron.d/empty-result-folder

RUN mkdir files &&  \
    chmod 0644 /etc/cron.d/empty-result-folder && \
    chmod 0644 /app/launch_cron.sh && \
    chmod +x /app/launch_cron.sh && \
    touch /var/log/cron.log && \
    apt update && \
    apt -y install cron && \
    pip install -r /app/requirements.txt

EXPOSE 5000

ENTRYPOINT [ "/app/launch_cron.sh" ]
CMD ["python3", "/app/run.py" ]
