# Neurotrack Vending Machine

Hi there, this was a fun challenge & I hope I did justice and gave you a worthy solution, while adhering to the time limits. I tried to cover what I believe are crucial parts to an effective day of work.

# Environment
- I tested the scripts on 'macOS Big Sur v11.2.1'. There might be a warning thrown if xcode is already installed but that shouldn't bother the overall.

1) On Mac. Download Zip. Extract. 
2) Open Terminal.
3) Change directory to Neurotrack_Challenge ( cd ~/Downloads/Neurotrack_Challenge/VendingMachine )
4) Run './setup' - This will setup your 'vanilla' macOS and get it ready to run the python file.
5) Run './runner' - This executes the program and display the output in the console

Obviously there are a lot of comments + debugging messages + config that can be added. I wanted to remain true to the 2 hours effort that was suggested in the email
Have a nice week :)


# Solution - Issues + TODOs for production

 - I have not added any form of unit tests to verify the different ways that each
   method can be invoked.
 - As of now, it only runs in auto simulation mode. I could have added the manual
   input option but that would have taken around 30 minutes and I wanted to stick
   to your ask.
 - I have not really used/seen a vending machine in a while but I remember them
   having names like A1, A2, ... A99, B1, etc. I did not focus on this naming when
   creating the tray structure.
 - Is there a scenario where they would try to stock the same tray with two
   different types of products? Based on some sort of popularity. I don't believe
   that would be useful so I did not consider this possibility.
 - Credit Card payment (Apple pay, Android pay, Bitcoin perhaps, etc.)
 - Expose the APIs so that machines can be stocked/re-stocked remotely and through
   a uniform-UI
- Can different trays have varying depths?
- There should be a way to specify limits on the vending machine. When these limits
  are reached there should be an alert (api call) made by the vending machine. These
  limits will allow for updates when there is a shortage of any product. Or even if 
  certain types of currency for change are running low. Essentially an alert system 
  that lets the required staff manage the book-keeping of this vending machine without 
  physical monitoring of these machines.
- There are possible scenarios where the cash entered into the machine is not got to
  be made into change correctly after the products are chosen. We could avoid this by 
  taking the order before dispensing but from what I have seen, the dispense happens 
  as soon as a valid selection is made. This scenario needs to be handled better.
- I know the console printing out is not very pretty. :)
