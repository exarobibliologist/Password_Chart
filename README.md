# Password_Chart
 A Python program for designing a Password Chart, similar to the one seen on passwordchart.com

## Dependencies
Requires Python 3.11 or greater, and Python libraries TKinter and Pillow.

To install those type
```
pip install tkinter
pip install pillow
```
## Instructions
![](https://i.imgur.com/iInwA1z.png)

When opening program, you will see a blank password chart. Enter a keyphrase into the Chart Selection Phrase box, and click Generate Chart.

![](https://i.imgur.com/dz5FhCs.png)

This is a sample image showing the password chart using the keyphrase "Sample"

## How It Works

There is no magic snake oil here, its a simple substitution cipher. Here is how the algorithm works:

1. An MD5 hash of the chart selection phrase is performed and the first 4 bytes of the hash is used as a random number seed to a Mersenne Twister pseudo-random number generator.

2. The password chart is then filled using sequences of 2 to 3 random characters by grabbing successive numbers generated from the Twister. The reason for the random sequence length is to make reversing the substitution cipher a bit harder.

3. The alphanumeric characters in the password is then converted using the chart. 

I offer no proof that the method of generating the chart is "secure". It is really just meant as a simple and fun substitution cipher that will help people maintain a little more secure set of passwords.