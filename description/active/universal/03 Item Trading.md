Got something to spare? See an item you desire? Items can be sold to and bought from others at a price in tokens you specify using chat commands.
**Buy/sell items** with: **buyitem**, **listbuyitem**, **cancelbuyitem**, **sellitem**, **listsellitem**, **cancelsellitem**.

## Buying Items

- **!buyitem 1 emoterain t5**: Buy 1 emoterain for 5 tokens or less
- **!buyitem 2 emoterain t5**: Buy 2 emoterains for 5 tokens or less each

Some items only buy/sell in packs:
- **!buyitem 1 5pack noisemaker t5**: Buy 1 5-pack of noisemakers for 5 tokens or less

If the item you want isn't currently sold at the desired price, you can place a buy offer for it:
- **!buyitem 1 emoterain t5 7d**: Place a buy offer for 1 emoterain at 5 tokens or less; this offer expires in 7 days
- **!listbuyitem**: List all your offers to buy items
- **!cancelbuyitem emoterain**: Cancel all your buy offers for emote rains

## Selling Items

To sell an item, use its id number from your inventory, prefixed by a #.
- **!sellitem 1 #3 t5**: Sell 1 of your 3rd item for 5 tokens
- **!sellitem 2 #3 t5**: Sell 2 of your 3rd item for 5 tokens each

Some items only buy/sell in packs:
- **!sellitem 1 5pack #2 t5**: Sell 1 5-pack of your 2nd item for 5 tokens

If the item you want isn't currently bought at the desired price, you can place a sell offer for it:
- **!sellitem 1 #2 t5 7d**: Place a sell offer for 1 of your 2nd item for 5 tokens; this offer expires in 7 days
- **!listsellitem**: List all your offers to sell items
- **!cancelsellitem #1**: Cancel all your sell offers of your 1st item

## Gifting Items

- **!giftitem #[id number] [item amount] [username]**: Where id number is the item number in your inventory, item amount is the amount of the item you chose to gift, username is the person you want to gift to
- **!giftitem #3 1 tppsimulator**: Gift 1 of the third item in your inventory to the user tppsimulator