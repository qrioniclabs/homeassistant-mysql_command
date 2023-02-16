# home-assistant-mysql-command
Home Assistant custom component that creates a Notify service to send a command to a MySQL server.

### Features
- Ability to send commands to a MySQL server using the Notify platform / service

### Configuration
### YAML
In configuration.yaml:
```yaml
notify:
  - platform: mysql_command
    host: 192.168.1.20
    db: my_db
    username: root
    password: your_password
```
