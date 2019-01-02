Got something to spare? See an item you desire? Items can be sold to and bought from others at a price in tokens you specify using chat commands.

## Buying items

*/w tpp buyitem 1 emoterain t5* (buy 1 emoterain for 5 tokens or less)

*/w tpp buyitem 2 emoterain t5* (buy 2 emoterains for 5 tokens or less each)

Some items only buy/sell in packs:

*/w tpp buyitem 1 5pack noisemaker t5* (buy 1 5-pack of noisemakers for 5 tokens or less)

If the item you want isn't currently sold at the desired price, you can place a buy offer for it:

*/w tpp buyitem 1 emoterain t5 7d* (place a buy offer for 1 emoterain at 5 tokens or less; this offer expires in 7 days)

*/w tpp listbuyitem* (list all your offers to buy items)

*/w tpp cancelbuyitem emoterain* (cancel all your buy offers for emote rains)

## Selling items

To sell an item, use its id number from your inventory, prefixed by a #.

*/w tpp sellitem 1 #3 t5* (sell 1 of your 3rd item for 5 tokens)

*/w tpp sellitem 2 #3 t5* (sell 2 of your 3rd item for 5 tokens each)

Some items only buy/sell in packs:

*/w tpp sellitem 1 5pack #2 t5* (sell 1 5-pack of your 2nd item for 5 tokens)

If the item you want isn't currently bought at the desired price, you can place a sell offer for it:

*/w tpp sellitem 1 #2 t5 7d* (place a sell offer for 1 of your 2nd item for 5 tokens; this offer expires in 7 days)

*/w tpp listsellitem* (list all your offers to sell items)

*/w tpp cancelsellitem #1* (cancel all your sell offers of your 1st item)
