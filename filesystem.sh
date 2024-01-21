#!/bin/sh
groupadd -g 1500 media

mkdir /docker/qbittorrent /docker/prowlarr /docker/radarr /docker/sonarr /docker/lidarr /docker/readarr -p
mkdir /data/torrents/movies /data/torrents/tv-series /data/torrents/music /data/torrents/books -p
mkdir /data/media/movies /data/media/tv-series /data/media/music /data/media/books -p

chown :media /data/ /docker/ -R
chmod 775 /data/ /docker/ -R
