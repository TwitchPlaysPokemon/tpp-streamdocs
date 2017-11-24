### Pokémon badges

Obtained Pokémon badges can be displayed next to your name in the overlay.

To list your badges, use the `/w tpp badges` command. To list the badges of someone else, use the `/w tpp badges <username>` command.

Badges are won by being in the chat when a Pokemon is captured in Pokemon Pinball. When this happens, a badge of the captured Pokemon is given to one random user in chat. They can also be won during runs; when the first of a Pokemon species is caught, its badge is also randomly given to a user in chat.

If you have multiple badges you can select the badge you want with the `/w tpp selectbadge <badge>` command.

#### Pokémon badge trading

Pokémon badges can be sold to and bought from others at a price in tokens you specify using chat commands. [More information on individual badges, like quantity, asking and selling prices, can be found here.](https://twitchplaysleaderboard.info/badges/)

The commands are explained in detail below. The commands for badge trading are: `buybadge`, `sellbadge`, `listbuybadge`, `listsellbadge`, `cancelsellbadge`, `cancelbuybadge`, `checkbadge`.

##### Buying Pokémon badges

`/w tpp buybadge pikachu` to see the price of Pikachu badges being sold (if any).

`/w tpp buybadge pikachu t5` to purchase one Pikachu badge for T5 tokens or less.

`/w tpp buybadge pikachu t5 2` to purchase two Pikachu badges for T5 tokens or less each.

`/w tpp buybadge pikachu t5 7d` to place a buy offer for one Pikachu badge at T5 tokens or less, the offer expires in 7 days (you can choose a longer or shorter expiration limit, the longest limit is 90 days and the shortest limit is 1 second).

`/w tpp listbuybadge` to list all your offers to buy Pokémon badges.

`/w tpp cancelbuybadge pikachu` to cancel all your buy offers for Pikachu.

##### Selling Pokémon badges

`/w tpp sellbadge pikachu` to see buy offers for Pikachu badges.

`/w tpp sellbadge pikachu t5` to sell your Pikachu badge for T5 tokens.

`/w tpp sellbadge pikachu t5 2` to sell two of your Pikachu badge for T5 tokens each.

`/w tpp listsellbadge` to list all your offers to sell Pokémon badges.

`/w tpp cancelsellbadge pikachu` to stop selling all of your Pikachu badges.

##### Badge transmutation

You can transmute multiple badges in order to get a new badge with a possible higher rarity and (usually) increased market value. This can be used to gain new generation 1 and 2 badges for a one token fee. Use `/w tpp transmute <specie>, <specie>, <specie>, …, t1` in order to transmute. Transmutation requires at least three badges, although using additional badges will logarithmically increase the rarity of the obtained badge. The transmutation and its result (there are six displayed choices of badges when you transmute) will be shown on screen, and tpp bot in chat will tell you what you get as well.

##### Other badge trading commands

You can check how many badges of one species are circulating with the `/w tpp checkbadge pikachu` command.

You can see how many unique badges you own by using the `/w tpp pokedex` command. You can also use `/w tpp pokedex <username>` to see someone else's unique badge count. This only counts badges currently owned, not previously owned badges.

### Participation badges

Participation badges are displayed next to usernames on the overlay; these indicate the first run a user participated in, and their total number of runs participated in after that. For example, someone with a “4|14” participation badge indicates that the first run they participated in was the 4th run, and they participated in a total of 14 different runs after that.

"Participation" means that a message was said in chat during the run.

Due to incomplete logs a small percentage of people from the first run did not get their participation badge for that run.

You can check what runs you participated in with the `/w tpp participation` command. If you don't like the color in which your participation badge gets shown, you can select another participation badge's color with the `/w tpp selectparticipationbadge <run number>` command.

### Secondary color

You can have a secondary color around your username on the stream. To do this, pay a one-time one-token fee by using `/w tpp unlocksecondarycolor` and then use `/w tpp setsecondarycolor <color>` with the hexadecimal value of the color you want to highlight your name. 