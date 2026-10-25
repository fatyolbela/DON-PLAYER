[app]
title = DON PLAYER
package.name = donplayer
package.domain = org.donplayer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = landscape

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a
