# Reading the Game dev container: Python + Quarto (Typst for PDFs, so no TeX needed).
FROM python:3.12-slim-bookworm

ARG QUARTO_VERSION=1.10.19
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl ca-certificates git ffmpeg poppler-utils fonts-dejavu-core fonts-liberation \
    && curl -fsSL -o /tmp/quarto.deb \
        "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb" \
    && apt-get install -y /tmp/quarto.deb && rm /tmp/quarto.deb \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG USERNAME=dev
RUN useradd -m -s /bin/bash ${USERNAME}
ENV UV_PROJECT_ENVIRONMENT=/opt/venv UV_LINK_MODE=copy PATH=/opt/venv/bin:$PATH
RUN mkdir -p /opt/venv && chown ${USERNAME} /opt/venv
USER ${USERNAME}
