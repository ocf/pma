from pathlib import Path

from transpire.resources import Deployment, Ingress, Service
from transpire.types import Image
from transpire.utils import get_image_tag

NAME = "phpmyadmin"


def objects():
    dep = Deployment(
        name=NAME,
        image=get_image_tag(NAME),
        ports=[8000],
    )

    svc = Service(
        name=NAME,
        selector=dep.get_selector(NAME),
        port_on_pod=8000,
        port_on_svc=80,
    )

    ing = Ingress.from_svc(
        svc=svc,
        host="pma.ocf.berkeley.edu",
        path_prefix="/",
    )

    yield dep.build()
    yield svc.build()
    yield ing.build()


def images():
    yield Image(name=NAME, path=Path("/"))
