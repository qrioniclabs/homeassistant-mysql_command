"""Support for mysql_command notification."""
from __future__ import annotations
from .const import CONF_DB

import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_TITLE,
    ATTR_TITLE_DEFAULT,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,
    CONF_USERNAME,
)
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

# REQUIREMENTS = ['mysql-connector==2.1.6']
import mysql.connector


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_DB): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
    }
)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> MySQLCommandNotificationService:
    """Get the mysql_command service."""
    host = config[CONF_HOST]
    db = config[CONF_DB]
    username = config[CONF_USERNAME]
    password = config[CONF_PASSWORD]

    return MySQLCommandNotificationService(host, db, username, password)


class MySQLCommandNotificationService(BaseNotificationService):
    """Implement the notification service for the mysql_command service."""

    def __init__(self, host, db, username, password):
        """Initialize the service."""
        self.host = host
        self.db = db
        self.user = username
        self.password = password

    def send_message(self, message="", **kwargs):
        """Send a message as command to a MySQL server."""
        cnx = mysql.connector.connect(
            host=self.host,
            db=self.db,
            user=self.user,
            password=self.password,
        )
        cursor = cnx.cursor(buffered=True)  # (buffered=True)
        cursor.execute(message)
        # something = cursor.lastrowid

        cnx.commit()
        cursor.close()
        cnx.close()
