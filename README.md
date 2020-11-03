# baseball-card-processor


## Purpose
This project is meant to be a small Raspberry Pi project (mine is running on a 3 B+) to programmically process my baseball card collection.
I estimate I have close to (if not) 1M+ baseball cards. What I want is a way to take a card from a deck, use OCR to get the data from a card, look up it's value
through some API (a baseball card API, or just eBay), write it to a CSV with the name of the player, year, and value of the card, along with a picture of the card 
(as a way to verify it is truly the card the lookup finds, as well as judging it's condition from a photo).


### How

This project uses 3 main pieces of hardare:

1. Raspberry Pi 3 B+
2. An RPi Night Vision camera (used only as a normal camera for this project)
3. A stepper motor (with a custom attachment for grabbing and dropping cards)

The concept is fairly basic. Given a stack of baseball cards, the stepper motor can programmically pull a card from the deck, and turn to hold the card in front 
of the camera. The camera takes a photo, runs it through an OCR program (we are using Tessaract for this), and lookup it's value (either through eBay, or another API).
After that, the price is taken and written to a CSV along with some other data about the card, and the function then calls itself.


