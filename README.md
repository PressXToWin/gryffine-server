# Gryffine

Login Attempts Monitoring and Auditing System for *nix-like OS (server-side).

## Features
* Real-time tracking and logging of login attempts
* Determining the potential danger level based on predefined rules
* Notification about login by Telegram or e-mail
* Exporting logs in popular formats (csv, xls)
* Log search and filtering

## How it works
On client machines, a [PAM-script](https://github.com/PressXToWin/gryffine-client) is installed, which sends JSON with login information to the API endpoint of the server when a login attempt is made. It doesn't matter which interface using, for example it suitable for local logins by tty or desktop manager, login through ssh or privilege escalation by sudo/su. In the case of remote logins from non-local IP ranges, the IP address is used to determine the country of the login attempt (using the MaxMind's GeoLite2 database). Then, the login attempt is checked by predefined rules (whitelist/blacklist), and based on the result, it is either marked as a suspicious login or trustful.

## Interface
![](docs/webinterface.png?raw=true)

Log records has color difference. If a successful login matches the blacklist rules, the entry is marked in red. If it matches the whitelist rules or if the login comes from local IP addresses, it is marked in green. Succesful logins that don't match any rules are marked in yellow. Unsuccessful logins are displayed in gray, regardless of whether they are in the blacklist or whitelist.

It is possible to set notifications through Telegram-bot or email.

![](docs/tg.png?raw=true)

![](docs/email.png?raw=true)

## Installation

 - Clone the repository on the server.

```git clone https://github.com/PressXToWin/gryffine-server.git```

 - Rename the .env.example file to .env and fill in the necessary information.
 - Create and run Docker containers by executing the following command on the server:
```
docker compose up -d
```
- After successful setup, create a superuser:
```
docker compose exec backend python manage.py createsuperuser
```

The server will be accessible at http://127.0.0.1:8080/

## Setting rules and notifications
Rules and notifications can be configured in the admin panel at http://127.0.0.1:8080/admin/

You can set up rules based on the country of the IP or subnet masks.
![](docs/rules.png?raw=true)

Notifications setting up when user profile being edited. In case when you need notifications by Telegram, you need to specify Telegram ID in profile, and the same applies to email notifications.
![](docs/notify.png?raw=true)

## API
The endpoind ```http://127.0.0.1:8080/api/v1/records/``` accepts POST requests in format:
```
{
    "service": "",          # the service through which the login attempt occurs
    "user": "",             # user login
    "hostname": "",         # machine hostname that the login is performed on
    "rhost": "",            # IP from which the request is made, can be empty
    "is_successful": false  # whether the attempt is successful or not
}
```

## LICENSE

[MIT Licensed](https://github.com/PressXToWin/gryffine-server/blob/main/LICENSE)

This product includes GeoLite2 data created by MaxMind, available from [maxmind.com](https://www.maxmind.com).

