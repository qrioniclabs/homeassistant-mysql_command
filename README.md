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
