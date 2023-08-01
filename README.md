# Gryffine

Monitoring and audit login tries system for *nix-like OS (server-side).

## Possibilities
* Monitor and log login attempts in real time
* Determining the level of potential danger according to pre-established rules
* Notofication about login by Telegram or e-mail
* Log export in popular formats (csv, xls)
* Log search and filtering

## How it works
On client side installed [PAM-script](https://github.com/PressXToWin/gryffine-client), which on login try sending json with information about try-out at server endpoint. It doesn't matter which interface using, for example it suitable for local logins by tty or desktop manager, login through ssh or privilege escalation by sudo/su. Next, in case of remote login not from local subnets, that system checking country of remote IP origin (usung database [MaxMind's GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2/)). Next, system checking login try by whitelist/blacklist rules and depending on check results login try being marked as suspicious or trustful.

## Interface
![](docs/webinterface.png?raw=true)

Log records has color difference. In case if successful login is in blacklist rule, record marked with red, in case if successful login is in whitelist rule or login come from local IP range, record marked with green. Successful login tries which not suits any rule marked with yellow. Unsuccessful login tries are gray, despite rules.

It is possible to set notifications through Telegram-bot or email.

![](docs/tg.png?raw=true)

![](docs/email.png?raw=true)

## Installation

## Setting rules and notifications
Rules and notifications setting at admin-panel on address http://127.0.0.1:8080/admin/

It is possible to set the rules by country of IP or by network mask.
![](docs/rules.png?raw=true)

Notifications setting up when user profile being edited. In case when you need notifications by Telegram, you need to write to set Telegram ID in profile, same as email.
![](docs/notify.png?raw=true)

## API
Endpoind ```http://127.0.0.1:8080/api/v1/records/``` accept POST-requests in format:
```
{
    "service": "",          # the service through which the login attempt occurs
    "user": "",             # user login
    "hostname": "",         # hostname of the server
    "rhost": "",            # Remote IP, which trying to log in, may be empty
    "is_successful": false  # If login try is successful
}
```

## LICENSE

[MIT Licensed](https://github.com/PressXToWin/gryffine-server/blob/main/LICENSE)

This product includes GeoLite2 data created by MaxMind, available from [maxmind.com](https://www.maxmind.com).

