#
# Complete the 'subscription_summary' function below.
# user input needed input(".....")
# for  (i) and while .....
# dictionaty = {}
# users select single months with ad =$7
# users select video on demand  =$27.99
## users select single months without ad =$9
# users select video on demand  =$27.99
# user needed 3
#   #bundle discount 3months therefor if.....
# months_subscribed = 7
# ad_free = 9
# video_on_demand = 27.99

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print("Ada+ Streaming Service")


package_list = []
months_list = []
while len(package_list) <= 3 and len(months_list) <= 3:
    print("Packages")
    print("A: Monthly subscription is $7")
    print("B: Monthly subscription is and Ad free is $9")
    print("C: Video_on_Demand is $27.99")
    selection = input("Which package would you like?")
    print(selection)
    print("How many months would you like this package for?")
    months_selected = input("Number of months")
    print(months_selected)

    bundle = 'yes'
    if months_subscribed == 3:
        print("3 months can be purchased as a bundle for $18.00, would you like this option?")
        bundle = input("Enter yes or no to purchase 3 month bundle ")
        if bundle == 'yes':
            print("3 month bundle Selected")
            print("Month Subscription purchased for 3 months, $18.00! ")
        else:
            print("Bundle option not available")

    monthly_sub = 7
    ad_free = 9
    vid_on_demand = 27.99
    # how do we equate for the 18$ bundle?
    print("Earnings for Monthly Subscription")
    monthly_sub = 7
    result = float(monthly_sub)
    print('$', result)
    # total earning of all customers
    print("Earnings for All Customers")
    result = float(monthly_sub) + float(ad_free) + float(vid_on_demand)
    print('$', result)
    # total earning for ad-free and vid on demand
    print("Earnings for Ad-free and Video on demand")
    result = float(ad_free) + float(vid_on_demand)
    print('$', result)
    # most profitable customer(how do we find that)

# this is where the .append will go
# another loop, and some math and if statments
# if statment for the price

# packge_list.append(Selection)this will the code to end
# months_list.append(months_selected)
# if maximam occupency


if __name__ == '__main__':
    months_subscribed = []
    ad_free_months = []
    video_on_demand_purchases = []

    header = input().strip()

    while header == "months_subscribed:":
        line = input().strip()
        try:
            months_subscribed.append(int(line))
        except ValueError:
            header = line

    while header == "ad_free_months:":
        line = input().strip()
        try:
            ad_free_months.append(int(line))
        except ValueError:
            header = line

    while header == "video_on_demand_purchases:":
        try:
            line = input().strip()

            video_on_demand_purchases.append(int(line))
        except EOFError:
            header = None

    subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)