# SpoonflowerTracking

This is a tool to check if a Spoonflower shop page is showing as expected. It is intended to be used with a cron job on MacOS or Linux.

## Usage

`python3 shopcheck.py <nameofyourshop> <optional mac|linux>`

The name of your shop should be typed as it appears in the h1 heading on your shop that says `Designs by <nameofyourshop>`

An optional second command line argument is the operating system, which is `mac` by default. You may specify `linux`, which will open a zenity information box.