import json

def Mapping(video_info):
    dislikes, comments_disabled,ratings_disabled, video_error_or_removed, category =video_info
    enabled={"Yes":1,"No":0}
    comments_disabled=enabled[comments_disabled]
    ratings_disabled=enabled[ratings_disabled]
    video_error_or_removed=enabled[video_error_or_removed]
    catlist=[0]*15
    with open("/Users/harshitarathee/Downloads/youtube_predictor/US_category_id.json") as f:
     categories = json.load(f)["items"]
    cat_dict = {}
    for cat in categories:
        cat_dict[cat["snippet"]["title"]] = int(cat["id"])
    print(cat_dict)
    id_dict=dict(zip(cat_dict.values(),range(len(cat_dict))))
    print(id_dict)
    catlist[id_dict[cat_dict[category]]]=1

    print(catlist)
Mapping([10,"No","No","No","Entertainment"])


