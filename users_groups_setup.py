import os


class UserGroupSetup:
    def __init__(self, root_dir='/'):
        self.root_dir = root_dir
        os.system('sudo groupadd media -g 13000')

    def create_config_dir(self, service_name):
        os.system(
            f'sudo mkdir -p {self.root_dir}/config/{service_name}-config'
            f' ; sudo chown -R {service_name}:media {self.root_dir}/config/{service_name}-config'
            f' ; sudo chown $(id -u):media {self.root_dir}/config'
        )

    def sonarr(self):
        os.system(
            '/bin/bash -c "sudo useradd sonarr -u 13001'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/tv -m 775'
            ' ; sudo chown -R sonarr:media ' + self.root_dir + '/data/{media,usenet,torrents}/tv'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('sonarr')
        os.system('sudo usermod -a -G media sonarr')

    def radarr(self):
        os.system(
            '/bin/bash -c "sudo useradd radarr -u 13002'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/movies -m 775'
            ' ; sudo chown -R radarr:media ' + self.root_dir + '/data/{media,usenet,torrents}/movies'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('radarr')
        os.system('sudo usermod -a -G media radarr')

    def lidarr(self):
        os.system(
            '/bin/bash -c "sudo useradd lidarr -u 13003'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/music -m 775'
            ' ; sudo chown -R lidarr:media ' + self.root_dir + '/data/{media,usenet,torrents}/music'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('lidarr')
        os.system('sudo usermod -a -G media lidarr')

    def readarr(self):
        os.system(
            '/bin/bash -c "sudo useradd readarr -u 13004'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/books -m 775'
            ' ; sudo chown -R readarr:media ' + self.root_dir + '/data/{media,usenet,torrents}/books'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('readarr')
        os.system('sudo usermod -a -G media readarr')

    def mylar3(self):
        os.system(
            '/bin/bash -c "sudo useradd mylar -u 13005'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/comics -m 775'
            ' ; sudo chown -R mylar:media ' + self.root_dir + '/data/{media,usenet,torrents}/comics'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('mylar')
        os.system('sudo usermod -a -G media mylar')

    def audiobookshelf(self):
        os.system(
            '/bin/bash -c "sudo useradd audiobookshelf -u 13009'
            ' ; sudo mkdir -pv ' + self.root_dir + '/data/{media,usenet,torrents}/audiobooks -m 775'
            ' ; sudo chown -R audiobookshelf:media ' + self.root_dir + '/data/{media,usenet,torrents}/audiobooks'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data'
            ' ; sudo chown $(id -u):media ' + self.root_dir + '/data/{media,usenet,torrents}"'
        )
        self.create_config_dir('audiobookshelf')
        os.system('sudo usermod -a -G media audiobookshelf')

    def prowlarr(self):
        os.system('sudo useradd prowlarr -u 13006')
        self.create_config_dir('prowlarr')
        os.system('sudo usermod -a -G media prowlarr')

    def qbittorrent(self):
        os.system('sudo useradd qbittorrent -u 13007')
        os.system('sudo usermod -a -G media qbittorrent')

    def overseerr(self):
        os.system('sudo useradd overseerr -u 13009')
        self.create_config_dir('overseerr')
        os.system('sudo usermod -a -G media overseerr')

    def plex(self):
        os.system('sudo useradd plex -u 13010')
        self.create_config_dir('plex')
        os.system('sudo usermod -a -G media plex')

    def sabnzbd(self):
        os.system('sudo useradd sabnzbd -u 13011')
        self.create_config_dir('sabnzbd')
        os.system('sudo usermod -a -G media sabnzbd')

    def jellyseerr(self):
        os.system('sudo useradd jellyseerr -u 13012')
        self.create_config_dir('jellyseerr')
        os.system('sudo usermod -a -G media jellyseerr')
