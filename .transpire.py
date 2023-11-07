from pathlib import Path

from transpire.resources import Deployment, Ingress, Service
from transpire.internal import surgery
from transpire.types import Image
from transpire.utils import get_image_tag

name = "phpmyadmin"


def objects():
    dep = Deployment(
        name="phpmyadmin",
        image=get_image_tag("phpmyadmin"),
        ports=[8000],
    )

    svc = Service(
        name="phpmyadmin",
        selector=dep.get_selector(),
        port_on_pod=8000,
        port_on_svc=80,
    )

    ing = Ingress.from_svc(
        svc=svc,
        host="pma.ocf.berkeley.edu",
        path_prefix="/",
    )

    dns = {"dnsPolicy": "ClusterFirst", "dnsConfig": {"searches": "ocf.berkeley.edu"}}

    # add dnsPolicy and dnsConfig to deployment
    yield surgery.shelve(
        dep.build(), ["spec", "template", "spec"], dns, create_parents=True
    )
    yield svc.build()
    yield ing.build()


def images():
    yield Image(name=name, path=Path("/"))
