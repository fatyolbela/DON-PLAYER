[app]
title = DON PLAYER
package.name = donplayer
package.domain = org.donplayer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = landscape
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 1
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a
p4a.bootstrap = sdl2
