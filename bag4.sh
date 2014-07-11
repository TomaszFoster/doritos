#!/bin/bash
gpio write 0 0
gpio write 1 0
gpio write 2 0
gpio write 3 0

gpio write 3 1
sleep 0.5
gpio write 3 0
