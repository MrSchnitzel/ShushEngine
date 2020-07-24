__author__ = 'ZJAllen'

# Define SPI Chip Select pin for each motor using RPi GPIO
# Define enable pins to enable/disable motor

# TODO: Update these values once the PCB is designed.
# Any other pin definitions neede?
#   m   |  mod  | cs#  |  BCM
#   0   |   1   |  0   |  8
#   1   |   2   |  3   |  24
#   2   |   3   |  1   |  7
#   3   |   4   |  4   |  23
#   4   |   5   |  2   |  25
#   5   |   6   |  5   |  18


m0_cs = 8
m0_enable = 2

# Need to update these as the board is developed.
# Numbers are only placeholders
m1_cs = 24
m1_enable = 3

m2_cs = 7
m2_enable = 4

m3_cs = 23
m3_enable = 17

m4_cs = 25
m4_enable = 27

m5_cs = 18
m5_enable = 22
