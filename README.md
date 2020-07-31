pma
--------
[![Build Status](https://jenkins.ocf.berkeley.edu/buildStatus/icon?job=ocf/pma/master)](https://jenkins.ocf.berkeley.edu/job/ocf/job/pma/job/master)

This is the OCF's Marathon service for [phpMyAdmin][pma].

phpMyAdmin is a good candidate for Marathon because it has no state or secrets.
In fact, anyone can run a copy of this service with `make dev` against the
actual MySQL database (you should be careful not to type passwords over
plaintext HTTP, though, which you will be when in dev mode).

Deploying phpMyAdmin in the past was difficult because it requires downloading
a tarball from a website, adding some config, etc. We had it configured as a
regular virtual host, but that meant a root staffer had to manually set
everything up, and updates were painful.


### Bumping to new versions of phpMyAdmin

Just change the version at the top of the `Makefile`.


### Starting in development

Just run `make dev` and go to the URL it tells you to. Remember not to log in
with a real username or password, since it's over plain HTTP (consider user
`anonymous` and no password instead).


[pma]: https://www.phpmyadmin.net/
