"""Support for mysql_command notification."""
from __future__ import annotations

from .const import (
    CONF_MYSQL_HOST,
    CONF_MYSQL_PORT,    
    CONF_MYSQL_USERNAME,
    CONF_MYSQL_PASSWORD,
    CONF_MYSQL_DB,
    CONF_MYSQL_TIMEOUT,
    DEFAULT_MYSQL_PORT,
    DEFAULT_MYSQL_TIMEOUT,
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
        vol.Optional(CONF_MYSQL_PORT, default=DEFAULT_MYSQL_PORT): vol.Coerce(int),
        vol.Required(CONF_MYSQL_USERNAME): cv.string,
        vol.Required(CONF_MYSQL_PASSWORD): cv.string,
        vol.Required(CONF_MYSQL_DB): cv.string,        
        vol.Optional(CONF_MYSQL_TIMEOUT, default=DEFAULT_MYSQL_TIMEOUT): vol.Coerce(int),
    }
)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> MySQLCommandNotificationService:
    """Get the mysql_command service."""
    host = config[CONF_MYSQL_HOST]
    port = config[CONF_MYSQL_PORT]
    username = config[CONF_MYSQL_USERNAME]
    password = config[CONF_MYSQL_PASSWORD]
    db = config[CONF_MYSQL_DB]
    timeout = config[CONF_MYSQL_TIMEOUT]

    return MySQLCommandNotificationService(host, port, username, password, db, timeout)


class MySQLCommandNotificationService(BaseNotificationService):
    """Implement the notification service for the mysql_command service."""

    
    def __init__(self, host, port, username, password, db, timeout):
        """Initialize the service."""
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.timeout = timeout

   
    def send_message(self, message="", **kwargs):
        """Send a message as command to a MySQL server."""
        cnx = mysql.connector.connect(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            db=self.db,
            connection_timeout=self.timeout,
        )
        cursor = cnx.cursor(buffered=True)  # (Why buffered=True? I don't have a clue...)
        cursor.execute(message)

        cnx.commit()
        cursor.close()
        cnx.close()
