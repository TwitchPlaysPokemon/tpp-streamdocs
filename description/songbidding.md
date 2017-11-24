##Songs and song bidding

TwitchPlaysPokemon has a big database of songs from various games that play in the background. There are 5 song categories: *betting, warning, battle, result, break*, each appropriate for the phase they describe.  
For your convenience the argument order after `/w tpp song` doesn't matter for any song commands.

* `/w tpp song` returns the song currently playing
* `/w tpp song random` returns a random song from the database
* `/w tpp song keyword1 keyword2 ...` returns a list of songs that match some keywords

###bidding on songs
You can bid on a song with tokens to be played. Such a song will be played in the next appropriate category (e.g. if you bid on a betting song, it will be played during the next betting phase).
Other people can outbid you with more tokens. Also multiple people can bid on the same song, effectively outbidding a single bigger bid on another song. Use these commands for song bidding:

* `/w tpp song bids <category>` returns current bidding information on that category. Example: `/w tpp song bids battle` returns bidding information for the next battle phase
* `/w tpp song tX Y` bid X tokens on the Yth result of the previous keyword search. Example: `/w tpp t1 2` bids 1 token on the 2nd search result.
* `/w tpp song tX random <category>` bid X tokens on a random song for that category. Multiple bids on `random` mean the same random song, not distinct ones. Example: `/w tpp song t1 random betting` bids 1 token on a random song for the next betting phase.

If you make a new bid in the same category, your previous bid in that category gets replaced. You can however bid for songs in different categories simultaneously.
