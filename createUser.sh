#!/bin/sh
useradd -u 1510 -g media qbittorrent
read qbittorrentpassword
passwd qbittorrent
echo qbittorrentpassword

useradd -u 1520 -g media prowlarr
read prowlarrpassword
passwd prowlarr
echo prowlarrpassword

useradd -u 1530 -g media radarr
read radarrpassword
passwd radarr
echo radarrpassword

useradd -u 1540 -g media sonarr
read sonarrpassword
passwd sonarr
echo sonarrpassword

useradd -u 1550 -g media readarr
read readarrpassword
passwd readarr
echo readarrpassword

useradd -u 1560 -g media lidarr
read lidarrpassword
passwd lidarr
echo lidarrpassword
