def check_rate_card_logic(sorted_rates):
    if len(sorted_rates) <= 0:
        print("length of sorted rates <= 0")
        return False
    if sorted_rates[0]["Age"] < 18:
        print("One adult is compulsory")

    # Counting kids & adults
    kids = 0
    adults = 0
    for sorted_rate in sorted_rates:
        if sorted_rate["Age"] < 18:
            kids += 1
        else:
            adults += 1
    if kids > 4:
        print("Kids > 4 not allowed")
    if adults > 2:
        print("Adults > 2 not allowed")

    return True


def calculate_premium(rates):
    premiums = list()
    discount = 0

    if len(rates) <= 0:
        print("No parameter for calculate_premium()")
        return premiums
    sorted_rates = sorted(rates, key=lambda x: x['Age'], reverse=True)

    if not check_rate_card_logic(sorted_rates):
        print("Logic failed")
        return

    premiums = list()
    discount = 0
    for i in range(len(sorted_rates)):
        persons_premium = dict()
        if i > 0:
            discount = 0.5

        persons_premium["Base Rate"] = sorted_rates[i]["Rate"]
        persons_premium["Floater Discount"] = str(discount * 100) + "%"
        persons_premium["Discounted Rate"] = sorted_rates[i]["Rate"] - (sorted_rates[i]["Rate"] * discount)
        premiums.append(persons_premium)

    return premiums


def convert_bson_to_python(db_response):
    ans = list()

    for resp in db_response:
        row = dict()
        for k, v in resp.items():
            if k != "_id":
                row[k] = v
        ans.append(row)

    return ans


if __name__ == "__main__":
    data = [{"Age": 10, "InsuredPattern": 1000, "PlanCode": "NSS01103", "PlanName": "SilverSmart", "ProductCode": "HSP",
             "Rate": 7073, "SumInsured": 500000, "Tenure": 1, "TierID": 1},
            {"Age": 35, "InsuredPattern": 1000, "PlanCode": "NSS01128", "PlanName": "SilverSmart", "ProductCode": "HSP",
             "Rate": 9441, "SumInsured": 500000, "Tenure": 1, "TierID": 1},
            {"Age": 46, "InsuredPattern": 1000, "PlanCode": "NSS01139", "PlanName": "SilverSmart", "ProductCode": "HSP",
             "Rate": 14676, "SumInsured": 500000, "Tenure": 1, "TierID": 1}]

    print(calculate_premium(data))
