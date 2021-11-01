# PromoEmailSave
Saves all new incoming email sender addresses to a txt or csv file for later use or reference 

## Imports
Imports needed:
```
import time
import datetime
import email
import imaplib
```
If you want to write to csv rather than a txt file
```
import csv
```

## Creating google app password
Follow simple instructions here under "Create and use App Passwords"
> [Google instructions link](https://support.google.com/mail/answer/185833?hl=en)

## Txt file
Make sure the txt file is in the same directory as the code before running!

## Extra
I use keyring
```
import keyring
```
for storing my email and app password so I don't have to hard-code it
