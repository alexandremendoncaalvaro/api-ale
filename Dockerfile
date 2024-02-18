FROM python:3.12.2-slim-buster as base

EXPOSE 8123

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED=1

FROM base AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip install --upgrade pip

RUN useradd --create-home ale
WORKDIR /home/ale

COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8123"]
