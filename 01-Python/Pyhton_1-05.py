def vickrey_auction(bids):
    if len(bids) < 2:
        return "not enough bidder"
    sorted_bids = sorted(bids, reverse=True)
    if sorted_bids[0] == sorted_bids[1]:
        return "error : have more than one highest bid"
    winner_bid = sorted_bids[0]
    second_highest_bid = sorted_bids[1]
    return f"winner bid is {winner_bid} need to pay {second_highest_bid}"
input_string = input("Enter All Bid : ")
bids = list(map(int, input_string.split()))
print(vickrey_auction(bids))
