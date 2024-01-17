#!/bin/sh
groupadd -g 1500 media

mkdir data
mkdir data/torrents data/media data/config
mkdir data/config/qbittorrent data/config/prowlarr data/config/radarr data/config/sonarr data/config/lidarr data/config/readarr
mkdir data/torrents/movies data/torrents/tv-series data/torrents/music data/torrents/books
mkdir data/media/movies data/media/tv-series data/media/music data/media/books

chown :media data/ -R
chmod 775 data/ -R
