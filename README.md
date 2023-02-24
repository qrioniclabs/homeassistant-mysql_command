[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Community Forum][community_forum_shield]][community_forum]
[![Buy me a coffee][buy_me_a_coffee_shield]][buy_me_a_coffee]



[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/qrioniclabs/home-assistant-mysql-command/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor/total

[community_forum_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Forum&style=popout&color=41bdf5&logo=HomeAssistant&logoColor=white
[community_forum]: https://community.home-assistant.io/t/xiaomi-cloud-vacuum-map-extractor/231292

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski


# home-assistant-mysql-command
Home Assistant custom component that creates a Notify service to send a command to a MySQL server.

### Features
- Send commands to a MySQL server using the Notify platform / service

### Inspired by:
https://community.home-assistant.io/t/how-do-i-call-an-insert-sql-command-to-mariadb-addon/

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
