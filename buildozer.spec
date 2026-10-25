name: Build DON PLAYER APK

on: [push]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip openjdk-17-jdk unzip libffi-dev libssl-dev
          pip install --upgrade pip
          pip install buildozer cython==0.29.36

      - name: Build APK
        run: |
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/tools/bin
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $HOME/.[STRIPPED 71 bytes]"d56f5187479451eabf01fb78af6dfcb131a6481e" >> $HOME/.[STRIPPED 76 bytes] android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: DON-PLAYER-APK
          path: bin/*.apk
