"""Support for mysql_command notification."""
from __future__ import annotations

from .const import (
    CONF_MYSQL_HOST,
    CONF_MYSQL_USERNAME,
    CONF_MYSQL_PASSWORD,
    CONF_MYSQL_DB,
)

import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_TITLE,
    ATTR_TITLE_DEFAULT,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

import mysql.connector

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_MYSQL_HOST): cv.string,
        vol.Required(CONF_MYSQL_USERNAME): cv.string,
        vol.Required(CONF_MYSQL_PASSWORD): cv.string,
        vol.Required(CONF_MYSQL_DB): cv.string,
    }
)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> MySQLCommandNotificationService:
    """Get the mysql_command service."""
    host = config[CONF_MYSQL_HOST]
    username = config[CONF_MYSQL_USERNAME]
    password = config[CONF_MYSQL_PASSWORD]
    db = config[CONF_MYSQL_DB]

    return MySQLCommandNotificationService(host, username, password, db)


class MySQLCommandNotificationService(BaseNotificationService):
    """Implement the notification service for the mysql_command service."""

    
    def __init__(self, host, username, password, db):
        """Initialize the service."""
        self.host = host
        self.username = username
        self.password = password
        self.db = db

   
    def send_message(self, message="", **kwargs):
        """Send a message as command to a MySQL server."""
        cnx = mysql.connector.connect(
            host=self.host,
            username=self.username,
            password=self.password,
            db=self.db,
        )
        cursor = cnx.cursor(buffered=True)  # (buffered=True)
        cursor.execute(message)

        cnx.commit()
        cursor.close()
        cnx.close()
