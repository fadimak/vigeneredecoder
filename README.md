# Vigenere Decoder
A frequency analysis program that is fairly effective at decoding messages encrypted using the Vigenere cipher when the key is unknown.

Enter the desired message at the bottom of the file.

The keylength must be manually entered, but does not need to be known:
  - run the tool once and observe a pattern in the number of coincidences
  - if you notice a high number every x places in the array, then x is probably the keylength
  - input this keylength on line 52

Ensure this program is run using python 3 (not 2).
