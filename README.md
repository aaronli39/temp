# Caesar Cipher

## Warm-up

Secret messages are RAD! See if you can decode this message below, where each letter actually represents a different letter. The hint you'll get is that M's are actually meant to be L's.

<details>
  <summary>click for solution <br> Encoded: Ifmmp Xpsme  <br>  Decoded:  _ _ L L _ &nbsp;&nbsp; _ _ _ L _ </summary><br>


  Each letter has been encoded by moving just one further down the alphabet than the original letter. Since L changed to M by going one further down, we can undo the message by going one letter backwards up the alphabet.

  * That means the first letter, I, should actually be an H.
  * The F should be an E.
  * The P's should be O's.
  * The X should be a W.
  * The S should be an R.
  * The E should be a D.

  The fully decoded message will be HELLO WORLD.
</details><br>

![Encrypt this!](https://media.giphy.com/media/A06UFEx8jxEwU/giphy.gif)

This type of code is called a Caesar Cipher, and it's one of the oldest methods of encryption ever used. The message used in the example had an offset of 1, since each letter was one further down the alphabet than the original, but you can offset a caesar cipher by any number - you'll just move that much further along the alphabet for any letter you wish to encode.

## The Goal

There are a couple of different ways to do this, but the goal is simple: create two functions, one called encode, the other called decode. Each method should take two arguments (the string you'd like to encode, and the offset of the cipher).

Try writing lines of code to test your file in the testcipher.py file:

###### Code to test your encode method.

```python
print(cipher.encode("Python is fun", 8)) # => prints out the string "Xgbpwv qa ncv"
```

###### Code to test your decode method.

```python
print(cipher.decode("Xgbpwv qa ncv", 8)) # => prints out the string "Python is fun"
```

## Push Yourself!

Here are some questions you can ask yourself for when your code is finished - if the answer to any of them inspires you to add some functionality to your program, then go for it!

* Does your cipher handle upper and lowercase letters well?
* What does your cipher do with punctuation? Is that what you want?
* What does your cipher do if the user doesn't KNOW the offset? Can you think of a way to write a decode message that can work with the user to crack an unknown code?
