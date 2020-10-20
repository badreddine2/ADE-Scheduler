import pytest
import datetime

import backend.models as md
import backend.schedules as schd
import views.utils as utl

from app import app as ade_scheduler
from flask_security import hash_password, login_user, logout_user


@pytest.fixture
def app(scope="session"):
    yield ade_scheduler


@pytest.fixture
def jyl(app):
    """Create a test user - this one is logged in"""
    mng = app.config["MANAGER"]
    user_datastore = app.config["SECURITY_MANAGER"].datastore

    jyl = user_datastore.create_user(
        email="jyl@scheduler.ade",
        password=hash_password("password"),
        confirmed_at=datetime.datetime.now(),
        active=True,
    )
    login_user(jyl)
    utl.init_session()

    schedule = md.Schedule(
        schd.Schedule(mng.get_default_project_id(), label="JYL'S SCHEDULE"), user=jyl
    )
    md.db.session.add(schedule)
    md.db.session.commit()

    yield jyl

    logout_user()
    md.db.session.delete(schedule)
    md.db.session.delete(jyl)
    md.db.session.commit()


@pytest.fixture
def jerom(app):
    """Create a test user - this one is not logged in"""
    mng = app.config["MANAGER"]
    user_datastore = app.config["SECURITY_MANAGER"].datastore

    jerom = user_datastore.create_user(
        email="jerom@scheduler.ade",
        password=hash_password("password"),
        confirmed_at=datetime.datetime.now(),
    )

    schedule = md.Schedule(
        schd.Schedule(mng.get_default_project_id(), label="JEROM'S SCHEDULE"),
        user=jerom,
    )
    md.db.session.add(schedule)
    md.db.session.commit()

    yield jerom

    md.db.session.delete(schedule)
    md.db.session.delete(jerom)
    md.db.session.commit()


@pytest.fixture
def louwi(app):
    """Create a test user - this one has no schedules"""
    mng = app.config["MANAGER"]
    user_datastore = app.config["SECURITY_MANAGER"].datastore

    louwi = user_datastore.create_user(
        email="louwi@scheduler.ade",
        password=hash_password("password"),
        confirmed_at=datetime.datetime.now(),
    )
    md.db.session.commit()

    yield louwi

    md.db.session.delete(louwi)
    md.db.session.commit()
