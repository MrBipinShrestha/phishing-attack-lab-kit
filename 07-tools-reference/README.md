# Tools Reference

## SET Commands
```bash
sudo setoolkit
# Menu: 1 > 2 > 3 > 2
```

## Wireshark Filters
```
http
tls
http.request.method == "POST"
```

## DNS Investigation
```bash
whois suspicious-domain.com
dig suspicious-domain.com TXT
nslookup suspicious-domain.com
```
