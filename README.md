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

### Configuration
### YAML
In configuration.yaml:
```yaml
notify:
  - platform: mysql_command
    host: 192.168.1.20
    db: your_db
    username: your_user
    password: your_password
```

## Configuration

After installation of the custom component, it needs to be configured in `configuration.yaml` file.
To do so, add a camera entry to your configuration with at least a [basic](#basic) or [recommended](#recommended) configuration.
Vacuum token can be extracted by following [this guide](https://www.home-assistant.io/integrations/xiaomi_miio/#retrieving-the-access-token) (ignore "not recommended" message, as it applies only to built-in Xiaomi Miio integration).
You also need to enter your Xiaomi Cloud username and password.
These are the credentials used for the Xiaomi Home app (_not ones from Roborock app_).

After installation and a reboot of your Home Assistant instance, you should get a camera entity which shows the vacuum map.
This might take a few minutes after a first restart.
If you have a problem with configuration validation you have to remove camera from `configuration.yaml`, restart Home Assistant, add camera config and restart HA again.

After modification of camera's configuration you can reload its settings in [Configuration](https://my.home-assistant.io/redirect/config/) or using `xiaomi_cloud_map_extractor.reload` service.

### Examples

#### Basic
```yaml
camera:
  - platform: xiaomi_cloud_map_extractor
    host: !secret xiaomi_vacuum_host
    token: !secret xiaomi_vacuum_token
    username: !secret xiaomi_cloud_username
    password: !secret xiaomi_cloud_password
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
