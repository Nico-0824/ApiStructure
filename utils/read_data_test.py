import yaml

with open("../data/data.yaml", encoding="utf-8") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    # print(data)
    print(data["mobile_belong"])
    # print(data["hero_1"])
    # print(data["hero_list_dict"])
    # print(data["hero_list"])
    # print(data["hero_list_list"])
