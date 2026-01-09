# Python Github and-Testing Practice
---
# Brainstorming improvements to Bevordle

Functionality:
- making sure you can't input the same word twice in one game
- making sure you can't input characters
- making sure you can't input numbers

Improvements:
- adding in a "Hard" version, like real Wordle has
- making sure every word entered is a real, acceptable word
- adding in levels of difficulty
- adding in hints
- adding a timer, and your time would be displayed in results

# What I implemented

1. making sure you can't input the same word twice in one game
1. making sure you can't input characters
1. making sure you can't input numbers
1. adding a timer, and the time is displayed in results

--- 
# How I could've implemented doctesting
I used unit testing because I thought the assertion would work better and because I thought that it makes sense to use doctesting for things that are shorter but unittesting for longer testing, so that it is separate and keeps the original code super legible which makes it easier for me. I think doctesting is great for things like calculators that compute things and are supposed to return set values where those values are concise, but my code is a little chunkier. I think I could've used doctesting for the checking letters and formatting time to check that that works. 
