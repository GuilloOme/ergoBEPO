# ergodox-infinity bépo layout builder

## Requirements

On Debian/ubuntu distribution, run: `sudo apt-get install git cmake ctags libusb-1.0-0-dev binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi dfu-util`
then
run in the project folder: `git submodule update --recursive --remote` to retrieve dependencies

## Usage

- run `build.bash`
- you'll find the resulting `.dfu.bin` files in the current folder

For installation, see: https://github.com/kiibohd/controller/wiki/Loading-DFU-Firmware