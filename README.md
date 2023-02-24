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
[community_forum]: https://community.home-assistant.io/t/xiaomi-cloud-vacuum-map-extractor/231292

# MySQL Command
Home Assistant custom component that creates a Notify service to send a command to a MySQL server.

## Features
- Send commands to a MySQL server using the Notify platform / service

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)
This component can be installed using HACS. Please follow directions [here](https://hacs.xyz/docs/faq/custom_repositories/) and use [https://github.com/qrioniclabs/home-assistant-mysql-command](https://github.com/qrioniclabs/homeassistant-mysql_command) as the repository URL.

### Manual
- Copy directory `custom_components/mysql_command` to your `<config dir>/custom_components` directory.
- Configure with config below.
- Restart Home-Assistant.

## Configuration
### YAML
In configuration.yaml:
```yaml
notify:
  - name: mysql_command_example_db
    platform: mysql_command
    host: 192.168.1.20
    username: your_user
    password: your_password
    db: example_db
```

Then, use the service like so:
```yaml
- service: notify.mysql_command_example_db
      data_template:
        message: >
          INSERT INTO `table` (column1, column2, column3) VALUES ('value1', 'value2', 'value3');
```

### Available configuration parameters
| Key | Type | Required | Value | Description |
|---|---|---|---|---|
| `platform` | string | true | `mysql_command` | Name of a platform |
| `host` | string | true | `192.168.1.123` | IP address of MySQL server |
| `db` | string | true | `my_db` | The database that the commands are sent to |
| `username` | string | true | `db_user` | MySQL user with access to the database |
| `password` | string | true | `aVerySecretPassword` | Password for the MySQL user |

## Special thanks
- Inspired by https://community.home-assistant.io/t/how-do-i-call-an-insert-sql-command-to-mariadb-addon/
- First steps taken with the help of [@mikey0000](https://github.com/mikey0000) via HA Discord
