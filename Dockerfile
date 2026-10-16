FROM ghcr.io/astral-sh/uv:python3.13-alpine
LABEL authors="jknap"

WORKDIR /app

COPY . /app

# Disable dev dependencies
ENV UV_NO_DEV=1

RUN uv sync --all-extras

CMD ["uv", "run", "wowbot"]
