FROM docker.ocf.berkeley.edu/theocf/debian:stretch

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apache2 \
        libapache2-mod-php \
        php-mbstring \
        php-mysql \
        pwgen \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/pma
ARG pma_version
RUN curl https://files.phpmyadmin.net/phpMyAdmin/${pma_version}/phpMyAdmin-${pma_version}-all-languages.tar.gz | tar -C /opt/pma --strip-components=1 -xzf-

COPY apache2/ /etc/apache2/
COPY config.inc.php /opt/pma/

CMD [ \
    "apachectl", \
    "-d", "/etc/apache2", \
    "-f", "apache2.conf", \
    "-e", "info", \
    "-DFOREGROUND" \
]
