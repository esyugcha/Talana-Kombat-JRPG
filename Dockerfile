FROM python:3.8

# RUN git clone https://github.com/esyugcha/Talana-Kombat-JRPG.git

WORKDIR /app/Talana-Kombat-JRPG

COPY . /app/Talana-Kombat-JRPG

CMD ["python", "app.py"]