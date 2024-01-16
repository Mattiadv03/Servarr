# Servarr configuration file
Docker compose file and other stuff related to Servarr's Suite

## Folder Tree Structure
data
├── config // Containes all config file for the media docker
│  ├── qbittorrent
│  ├── prowlarr
|  ├── radarr
|  ├── sonarr
|  ├── lidarr
│  └── readarr
├── torrents // Containes all file downloaded by QBitTorrent
│  ├── movies
│  ├── music
|  ├── books
│  └── tv
└── media    // Containes all file moved and renamed by Servarr's Suite. Jellyfin or Plex use this directories.
    ├── movies
    ├── music
    ├── books
    └── tv

## 
