[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Community Forum][community_forum_shield]][community_forum]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/qrioniclabs/home-assistant-mysql-command/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor.svg?style=popout

[releases]: https://github.com/qrioniclabs/home-assistant-mysql-command/releases/
[downloads_total_shield]: https://img.shields.io/github/downloads/qrioniclabs/home-assistant-mysql-command/total

[community_forum_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Forum&style=popout&color=41bdf5&logo=HomeAssistant&logoColor=white
[community_forum]: https://community.home-assistant.io/t/xiaomi-cloud-vacuum-map-extractor/231292

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski


# home-assistant-mysql-command
Home Assistant custom component that creates a Notify service to send a command to a MySQL server.

## Features
- Send commands to a MySQL server using the Notify platform / service

## Inspired by:
https://community.home-assistant.io/t/how-do-i-call-an-insert-sql-command-to-mariadb-addon/

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

This integration can be installed using HACS.
To do it search for `Xiaomi Cloud Map Extractor` in *Integrations* section.

### Manual

To install this integration manually you have to download [*xiaomi_cloud_map_extractor.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor/releases/latest/download/xiaomi_cloud_map_extractor.zip) and extract its contents to `config/custom_components/xiaomi_cloud_map_extractor` directory:
```bash
mkdir -p custom_components/xiaomi_cloud_map_extractor
cd custom_components/xiaomi_cloud_map_extractor
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor/releases/latest/download/xiaomi_cloud_map_extractor.zip
unzip xiaomi_cloud_map_extractor.zip
rm xiaomi_cloud_map_extractor.zip

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
| `platform` | string | true | `xiaomi_cloud_map_extractor` | Name of a platform |
| `host` | string | true | `192.168.0.123` | IP address of a vacuum |
| `token` | string | true | `ghjhca3ykg8o2zyyj7xb5adamhgsypel` | Token of a vacuum |
| `username` | string | true | `xiaomi.account@gmail.com` | Username (email or user ID) used to connect to Xiaomi cloud (the account used in the Xiaomi Home app) |
| `password` | string | true | `aVerySecretPassword` | Password used to connect to Xiaomi cloud (the account used in the Xiaomi Home app) |
| `name` | string | false |   | Desired name of camera entity |
| `country` | string | false | One of: `cn`, `de`, `us`, `ru`, `tw`, `sg`, `in`, `i2` | Server used in Xiaomi cloud. Leave empty if you are not sure. |
| `colors` | map | false |  | Colors configuration ([see below](#colors-configuration)) |
| `room_colors` | map | false |  | Room colors configuration ([see below](#room-colors-configuration)) |
| `draw` | list | false |  | List of elements to draw on a map ([see below](#draw-configuration)) |



## Special thanks

This integration wouldn't exist without following projects:
 - [openHAB miIO add-on](https://github.com/openhab/openhab-addons/tree/main/bundles/org.openhab.binding.miio/src/main/java/org/openhab/binding/miio) by [@marcelrv](https://github.com/marcelrv)
 - [valeCLOUDo](https://github.com/Xento/valeCLOUDo) by [@Xento](https://github.com/Xento)
 - [Xiaomi Robot Vacuum Protocol](https://github.com/marcelrv/XiaomiRobotVacuumProtocol) by [@marcelrv](https://github.com/marcelrv)
 - [Valetudo](https://github.com/Hypfer/Valetudo) by [@Hypfer](https://github.com/Hypfer)


<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic
