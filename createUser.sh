#!/bin/sh
useradd -u 1510 -g media qbittorrent
chown qbittorrent /docker/qbittorrent /data/torrents -R

useradd -u 1520 -g media prowlarr
chown prowlarr /docker/prowlarr

useradd -u 1530 -g media radarr
chown radarr /docker/radarr /data/media/movies

useradd -u 1540 -g media sonarr
chown sonarr /docker/sonarr /data/media/tv-series

useradd -u 1550 -g media readarr
chown readarr /docker/readarr /data/media/music

useradd -u 1560 -g media lidarr
chown lidarr /docker/lidarr /data/media/books

useradd -u 1580 -g media jellyseerr
chown lidarr /docker/jellyseerr /data/media
