Token betting is an advanced betting system that has similarities to the stock market, it is very complicated and not recommended for new viewers who are recommended to start with Pokeyen betting (explained above).

Token betting is accomplished through the trading of "bets" which can be thought of as promises to pay tokens in the event that a specified team wins.

Trading is accomplished by placing "orders" to buy or sell one or more bets at a specified price, when two people have placed orders that can fulfill each other the bets are traded.

Unlike Pokeyen betting it is possible to continue to bet after the match has begun. It is possible to resell bets (for a profit or loss). It is possible to bet on both teams simultaneously.

`/w tpp order buy red t5 2` will place an order to buy 2 bets at T5 each, everything after the `/w tpp order` part can be in any order, it's the format of each part that is important.

It is possible to make and fulfill a sell order without holding any bets. When a sell order is fulfilled T10 tokens are held on your account to cover the bet's potential payout.

By default an order will expire after 1 minute, you can specify the number of minutes before expiring, for example: `/w tpp order sell blue t1 10 5m` will expire after 5 minutes, `/w tpp order sell red t1 5 persist` will make an order that never expires.

`/w tpp orders` will list all the orders you've made that are currently active in the market. `blue: 3ST7x1 4ST8x2 red: 5ST4x3` is an example of the response, each order is represented in a compact string such as `3ST7x1`, the following is that string broken down into its components and explained:

* `3` - The ID number of the order, this is used when manually cancelling a specific order.

* `S` - The type of order, for sell orders it is `S` for buy orders it is `B`.

* `T7` - The price of each bet in tokens.

* `x1` - The remaining quantity of bets that the order can fulfill.

`/w tpp cancel all` cancels all orders. `/w tpp cancel 1` would cancel order #1, use the `orders` command to list the IDs of your orders.

Everyone's token bets are displayed on-screen at the bottom of each team's bet list. `T50T5C1S1B1H1` is an example of the format the user's token betting information is displayed in, the following explains each of the parts:

* `T50` - The user's balance.

* `T5` - Number of tokens spent on bets, minus any tokens earned from resale.

* `C1` - Number of bets created.

* `S1` - Number of bets sold.

* `B1` - Number of bets bought.

* `H1` - Number of bets currently held.