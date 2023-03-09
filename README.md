[![HACS Custom][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Community Forum][community_forum_shield]][community_forum]

[hacs_shield]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge
[hacs]: https://github.com/hacs/integration

[latest_release]: https://github.com/qrioniclabs/homeassistant-mysql_command/releases/latest
[releases_shield]: https://img.shields.io/github/release/qrioniclabs/homeassistant-mysql_command.svg?style=for-the-badge

[releases]: https://github.com/qrioniclabs/home-assistant-mysql-command/releases/
[downloads_total_shield]: https://img.shields.io/github/downloads/qrioniclabs/homeassistant-mysql_command/total?style=for-the-badge

[community_forum_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Forum&style=for-the-badge&color=41bdf5&logo=HomeAssistant&logoColor=white
[community_forum]: https://community.home-assistant.io/t/mysql-command/539839

# MySQL Command
A Home Assistant custom component that creates a `notify` service to send a command to a MySQL server.

<sup>Forum Topic: https://community.home-assistant.io/t/mysql-command/539839</sup>

## Features
- Send commands to a MySQL server using the Notify platform / service

## Installation

### Using [HACS](https://hacs.xyz/)
This component can be installed using HACS. Please follow directions [here](https://hacs.xyz/docs/faq/custom_repositories/) and use [https://github.com/qrioniclabs/homeassistant-mysql_command](https://github.com/qrioniclabs/homeassistant-mysql_command) as the repository URL.

### Manual
- Copy directory `custom_components/mysql_command` to your `<config dir>/custom_components` directory
- Configure with config below
- Restart Home Assistant

## Configuration
### YAML
In configuration.yaml:
```yaml
notify:
  - name: mysql_command_example_db
    platform: mysql_command
    host: YourHostnameOrIP
    username: YourUser
    password: YourPassword
    db: YourDB
```

Then, use the service like so:
```yaml
- service: notify.mysql_command_example_db
      data_template:
        message: >
          INSERT INTO `table` (column1, column2, column3) VALUES ('value1', 'value2', 'value3');
```

Here is an example with a template timestamp:
```yaml
- service: notify.mysql_command_example_db
      data_template:
        message: >
          INSERT INTO `table` (datetime, column1, column2) VALUES ('{{ now().timestamp() | timestamp_custom('%Y-%m-%d %H:%M:%S') }}', 'value1', 'value2');
```

### Available configuration parameters
| Key | Type | Required | Value | Description |
|---|---|---|---|---|
| `platform` | string | true | `mysql_command` | Name of a platform |
| `host` | string | true | `192.168.1.123` | Hostname or IP address of MySQL server |
| `username` | string | true | `example_user` | MySQL user with access to the database |
| `password` | string | true | `aVerySecretPassword` | Password for the MySQL user |
| `db` | string | true | `example_db` | The database that the command is sent to |
| `timeout` | int | false | `30` | Timeout (in seconds) for the database connection. Default: 10 |

## Special thanks
- Inspired by https://community.home-assistant.io/t/how-do-i-call-an-insert-sql-command-to-mariadb-addon/
- First steps taken with the help of [@mikey0000](https://github.com/mikey0000) via HA Discord
