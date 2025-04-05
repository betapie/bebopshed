FROM ubuntu:24.04

WORKDIR /app

# Django dependencies
RUN apt update && apt install -y \
  git \
  libpq-dev \
  lilypond \
  python3-venv \
  python3-pip

RUN python3 -m venv /app/venv

COPY bebopshed/requirements.dev.txt /app/

RUN /app/venv/bin/pip install --upgrade pip && /app/venv/bin/pip install -r requirements.dev.txt

RUN git clone https://github.com/OpenLilyPondFonts/lilyjazz.git /tmp/lilyjazz && \
  cp -r /tmp/lilyjazz/otf/* /usr/share/lilypond/2.24.3/fonts/otf && \
  cp -r /tmp/lilyjazz/svg/* /usr/share/lilypond/2.24.3/fonts/svg && \
  cp /tmp/lilyjazz/supplementary-files/lilyjazz-chord/lilyjazz-chord.otf /usr/share/lilypond/2.24.3/fonts/otf && \
  cp /tmp/lilyjazz/supplementary-files/lilyjazz-text/lilyjazz-text.otf /usr/share/lilypond/2.24.3/fonts/otf && \
  rm -rf /tmp/lilyjazz

CMD ["/app/venv/bin/python", "/app/bebopshed/manage.py", "runserver", "0.0.0.0:8000"]
