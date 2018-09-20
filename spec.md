
# Radius Interview Python Programming Task

## Purpose

The purpose of this task is for you to demonstrate a basic knowledge of the Python programming language and general programming techniques.

## Task 

Write an interactive version of the popular card game Blackjack using the Python programming language. The game should enable a dealer and a single player to play a game of Blackjack using a standard 52 card pack (or deck). There is no requirement to create a graphical user interface, using simple command line prompts to enable the player to interact with the game is sufficient. Use of class based objects is preferable although using functions instead (or a combination of both) is acceptable. If you are unfamiliar with the Blackjack game you can find an overview of the rules below, which can also be found by searching online. 

Although you are free to implement as many rules of the game as you wish you are not required to implement all of them, just those that enable a user to play a game of Blackjack against a dealer in its most basic form will be sufficient, providing the ability to place a stake or bet on a hand in a game is also not required. 

Some of the rules vary globally so if you are familiar with the Blackjack game feel free to implement the version you are comfortable with. Note that we are not looking for the perfect solution but one that demonstrates your programming experience. 

Finally, you should provide a few sentences and/or bullet points detailing what you would do to improve your given solution should you be given the opportunity to develop it further.

## Blackjack Rules

In Blackjack, your objective is to get the value of your hand closer to 21 than the
 dealer's hand. However, if you exceed 21 you lose automatically (go bust).

Really there are two ways of winning: 
Get the value of your hand closer to 21 than the dealer by drawing more cards
Stick with your hand and see if the dealer goes bust (in most Blackjack variants the dealer cannot stick on less than 17). 

Once you have placed your stake you are dealt 2 cards and the dealer is dealt 1 face up card. 

Blackjack - If you are dealt 21 on your initial hand, it is referred to as a natural Blackjack and you are paid 2.5x your stake. Unless the dealer also shows Blackjack (note a natural Blackjack is the highest hand, worth more than 21, made from 3 or more cards). 
 
Assuming you have not been dealt a Blackjack you can then: 

### Stand/Stick

Stand is when you refuse anymore cards, do this when you feel you have a high hand say 17 or more. Or when the dealer shows a low card, (as the dealer must 'hit' on 16 and lower hands), hence there is a fair chance of the dealer going 'BUST' if the dealer were to draw a high card.

### Hit/Twist

Accept an additional card to get your hand value closer to 21, you may do this as many times as you wish as long as your hand remains under 21. However if the additional card you receive takes your hand above 21 you go BUST and lose immediately.

### Additional options (Not required/Optional for this task)

If your initial hand is between 9-11 you may also be able to Double or if you have been dealt 2 matching cards you can Split. If the dealer's face up cards is an Ace you will be offered Insurance. 

Once the player has finished the dealer reveals/draws their 2nd card. The dealer must stand on a hand 17 and HIT on hands totalling 16 and less. If the dealer exceeds 21 after a HIT, they go BUST and automatically lose and the player wins. Once the dealer has finished, whoever has the hand closest to 21 wins unless it ends in a draw.

Notes:
Kings, Queens, and Jacks are worth 10
Ace cards can be treated as either a 1 or 11

### Doubling

In Blackjack when your initial hand is of a certain value you are offered the option to double. If you choose this option your stake is doubled and you are dealt one additional card then your turn ends (you are not allowed to hit afterwards). 

Typically you are allowed to double when your initial hand value is between 9-11, although this depends on the Blackjack variant (some variants will allow you to double on any hand).

### Splitting

When you are dealt a pair of the same cards you are offered the option of splitting. If you choose this option your cards are split into two new hands and an additional card is dealt for each of the two new hands. Your stake is also doubled, one for each hand and these are played independently. Hence if you lose/bust on one hand you may yet win on the other.

Typically you are not allowed to split again or double on a split hand, but again this depends on the Blackjack rules your game is played by.
 
### Insurance

When the dealer is dealt a face up Ace card, the player is offered the option of taking insurance. Insurance protects the player in the event of the dealer drawing Blackjack. 
If you do take insurance you place a bet half the value of your current stake. 

Assuming the dealer does draw Blackjack (and assuming you don't have Blackjack) you lose your stake on your cards but you win the insurance bet which pays out at 2x the stake - basically you walk away with neither a win or a loss. 

If the dealer does not draw Blackjack, your insurance bet is lost and the game proceeds normally.

Never take insurance! (it increases the house advantage by 5.8-7.5%).

### Surrender

Some casinos will offer the player the option to surrender on their initial hand by forfeiting half their stake if the player does not like their prospects.

### Blackjack Rules Variations

The most common variation of Blackjack rules is Altantic City blackjack rules:
8 decks
The deck is re-shuffled after each hand 
Dealer stands on all soft 17s 
Dealer hits on 16 and less
Doubling after splitting allowed 
No re-splitting of cards allowed 
No surrender 
Only one additional card allowed on each ace when splitting a pair of aces

Key variations:
Number of decks
Dealer receives 2nd card after the player has finished
No doubling after splitting
Single bet position or multi-hand 

Casino operators generally publish their specific blackjack rules online. 

### Blackjack Jargon


Hit - take a card

Stand - end their turn

Double - double wager, take a single card and finish

Split - if the two cards have the same value, separate them to make two hands

Surrender - give up a half-bet and retire from the game

Push? - tied score, known as "push" or "standoff",

Soft - an ace and card with a value lower then 10 is referred to as a 'soft' hand, because the value is flexible, i.e. a ace & 7 can equal 18 or 8.

Hard - a hand without aces are referred to as 'hard' hands, because their values are definite.

"twist" (hit), "stick" (stand) and "buy" (double the bet)

