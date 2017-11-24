Through Twitch Plays Pokemon you can bet on and influence matches of Pokemon Battle Revolution in chat.


# Matches

Pokemon Battle Revolution matches are being played. The moves are automatically selected based on chat commands. The Pokemon are chosen using a matchmaking system. [Here is all the information of Pokemon that can be selected by the matchmaker and the available sets needed when bidding a match.](https://docs.google.com/spreadsheets/d/1tLIOaxOXgi0zRWlskkAhgyVfUivdrMaYmSIcM0dFVW8/edit#gid=1411011312)


# Pokeyen betting

Pokeyen betting is simple, [SaltyBet](http://twitch.tv/saltybet)-style betting on the outcome of matches and is recommended for new viewers. There is a betting period of about 3 minutes before the match begins when all bets must be placed.

The odds aren't locked in until the betting phase has concluded; until then, the displayed odds serve only as an indication of what the odds would be if no further bets were made. The colored percentage at the top of the screen is the payout multiplier and indicates the odds of the result of the match, 50% means if that team wins the payout will be 50% of the bet amount.

During the betting phase `!bet 100 red` will place a P100 bet on team red. Prefixing the amount with `p` or `P` is optional.

Your balance cannot go lower than P100 (or P500 for subscribers). Therefore, if you lose a bet and your balance becomes P0, your balance will be reset to P100 (or P500 for subscribers) before the next match. Balances can be checked with the balance command, for example: `/w tpp balance` would return your Pokeyen and Token account balances.

Bets larger than P5,000 and P50,000 must be made 20 and 40 seconds ahead of betting closure respectively. Be aware of the stream processing and transmission delay when making last-moment bets. In chat, tpp bot will also announce the remaining betting time at various intervals if you need help accounting for the delay.

The only way to influence the match is through Pokeyen betting, and the amount of your influence is proportional to the size of your bet.

Each move slot is assigned a letter: A, B, C and D, and each Pokemon is assigned a number: 1, 2 and 3. The - character represents no selection. Pokeyen bettors are able to select a move or Pokemon by typing ! followed by the appropriate command, for example: !a will register your preference for the move in the A slot to be selected.

# PBR seasons

Every few months, usually in-between runs, PBR begins a new season. The final leaderboard for the previous season will be displayed after the last match of the season and any bettors with above P2,000 will get rewards. Have a higher balance means you will get more and better rewards. At the start of each season, everyone’s balances reset to P1,000. There will occasionally be multiple seasons in-between runs when new features are rolled out. [A leaderboard for each season can be found here.](https://twitchplayspokemon.tv/leaderboard)

# PBR commentary

During PBR matches, there is occasionally live commentary for 1 or 2 hour blocks, typically happening once or twice a day for six days out of the week. The hours in which this occurs will always vary, so that people in different timezones can have the opportunity to listen. During commentary, the standard PBR announcer is turned off and two people at a time will narrate the events happening on stream, as well as interact with each other and with the members in chat.

[The schedule for the upcoming week of commentary can be found here.](https://calendar.google.com/calendar/embed?src=h2nm0ai4thia6i1hgjop81ahlc%40group.calendar.google.com)

If you are interested in joining commentary, you must have a working mic as well as the capability to install 2 different programs on your computer. Whisper the user BEXXXXXXX here on Twitch in order to join!

# Music bidding

Songs are selected through an automatic collaborative bidding process using tokens as currency.

`/w tpp song` to display the currently playing song.

`/w tpp song pepsi` to search for a song by name (both song and game name).

`/w tpp song more` to display more search results from the previously-made query.

`/w tpp song 1 t1` to place a 1 token bid on the first song returned in the previously-made query.

`/w tpp song katamari t5` to place a 5 token bid on the first song in the search results for the provided query.

`/w tpp song bids` to display the currently winning song in each category.

The amount of tokens is the maximum you're willing to bid, the system will always try to get the best deal possible (overcutting second place by 1 token) so you may end up spending less.

The order of everything after `/w tpp song` doesn't matter, the number of tokens can the first argument for example. Focus on remembering the format of arguments and not their position.

[A full list of songs is also available here.](https://twitchplaysleaderboard.info/pbr/songs/) [You can also submit music here.](https://twitchplayspokemon.tv/music_submission_form)

# Token match bidding

Similarly to songs, token matches where specific pokemon are matched up in a battle can be bid on collaboratively. They can be bid on at any time, but are only visible during the hourly break. After every hourly break, the token match with the most total tokens bid on it will commence.

`/w tpp match a,b,c/d,e,f t1` would place a 1 token bid on a match involving 6 different pokemon with default movesets for each, in the default metagame. The letters can be substituted by either the desired pokemons' pokedex numbers or their names with an optional valid moveset name for each.

There are several metagames, each with thier own selection of pokemon. You can select the metagame to use by typing it before the pokemon like so `/w tpp match ubers a,b,c/d,e,f t1`. If this is done then mons from that metagame can be selected. For a list of the available metagames, type `/w tpp match metagames`.

The valid moveset names can be found in the [PBR Info Guide.](https://docs.google.com/spreadsheets/d/1tLIOaxOXgi0zRWlskkAhgyVfUivdrMaYmSIcM0dFVW8/edit#gid=1127521972)

As an example, `/w tpp match Stadium2 bulbasaur,ivysaur,venusaur/charmander,charmeleon,charizard t2` would place a 2 token bid on a match involving Bulbasaur, Ivysaur and Venusaur on blue team and Charmander, Charmeleon and Charizard on red using the Stadium 2 metagame's default moveset.

The order of the pokemon names or pokedex numbers on either team correspond to the pokemon in slots 1, 2 or 3 respectively. In the last example, Bulbasaur would be in slot 1, Ivysaur in slot 2 and Venusaur in slot 3 for blue team, while Charmander, Charmeleon and Charizard would be in slots 1, 2 and 3 for red team.