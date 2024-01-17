#!/bin/sh
useradd -u 1510 -g media qbittorrent
passwd qbittorrent

useradd -u 1520 -g media prowlarr
passwd prowlarr

useradd -u 1530 -g media radarr
passwd radarr

useradd -u 1540 -g media sonarr
passwd sonarr

useradd -u 1550 -g media readarr
passwd readarr

useradd -u 1560 -g media lidarr
passwd lidarr
