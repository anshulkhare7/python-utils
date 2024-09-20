import csv
import json

# Your JSON data
json_data = '{"list":[{"shortId":"aplive","platform":14,"platformAccount":0,"platformSection":17},{"shortId":"m00001","platform":5,"platformAccount":0,"platformSection":0},{"shortId":"m00002","platform":6,"platformAccount":0,"platformSection":0},{"shortId":"m00003","platform":12,"platformAccount":0,"platformSection":0},{"shortId":"m00004","platform":10,"platformAccount":19,"platformSection":16},{"shortId":"m00005","platform":10,"platformAccount":20,"platformSection":16},{"shortId":"m00006","platform":11,"platformAccount":0,"platformSection":0},{"shortId":"m00007","platform":2,"platformAccount":9,"platformSection":6},{"shortId":"m00009","platform":2,"platformAccount":9,"platformSection":8},{"shortId":"m00010","platform":2,"platformAccount":10,"platformSection":6},{"shortId":"m00012","platform":2,"platformAccount":10,"platformSection":8},{"shortId":"m00013","platform":4,"platformAccount":13,"platformSection":11},{"shortId":"m00014","platform":4,"platformAccount":13,"platformSection":12},{"shortId":"m00015","platform":4,"platformAccount":14,"platformSection":11},{"shortId":"m00016","platform":4,"platformAccount":14,"platformSection":12},{"shortId":"m00017","platform":3,"platformAccount":11,"platformSection":9},{"shortId":"m00018","platform":3,"platformAccount":11,"platformSection":10},{"shortId":"m00019","platform":3,"platformAccount":12,"platformSection":9},{"shortId":"m00020","platform":3,"platformAccount":12,"platformSection":10},{"shortId":"m00021","platform":1,"platformAccount":1,"platformSection":1},{"shortId":"m00022","platform":1,"platformAccount":1,"platformSection":2},{"shortId":"m00023","platform":1,"platformAccount":1,"platformSection":3},{"shortId":"m00024","platform":1,"platformAccount":1,"platformSection":4},{"shortId":"m00025","platform":1,"platformAccount":1,"platformSection":5},{"shortId":"m00026","platform":1,"platformAccount":2,"platformSection":1},{"shortId":"m00027","platform":1,"platformAccount":2,"platformSection":2},{"shortId":"m00028","platform":1,"platformAccount":2,"platformSection":3},{"shortId":"m00029","platform":1,"platformAccount":2,"platformSection":4},{"shortId":"m00030","platform":1,"platformAccount":2,"platformSection":5},{"shortId":"m00031","platform":1,"platformAccount":3,"platformSection":1},{"shortId":"m00032","platform":1,"platformAccount":3,"platformSection":2},{"shortId":"m00033","platform":1,"platformAccount":3,"platformSection":3},{"shortId":"m00034","platform":1,"platformAccount":3,"platformSection":4},{"shortId":"m00035","platform":1,"platformAccount":3,"platformSection":5},{"shortId":"m00036","platform":1,"platformAccount":4,"platformSection":1},{"shortId":"m00037","platform":1,"platformAccount":4,"platformSection":2},{"shortId":"m00038","platform":1,"platformAccount":4,"platformSection":3},{"shortId":"m00039","platform":1,"platformAccount":4,"platformSection":4},{"shortId":"m00040","platform":1,"platformAccount":4,"platformSection":5},{"shortId":"m00041","platform":1,"platformAccount":5,"platformSection":1},{"shortId":"m00042","platform":1,"platformAccount":5,"platformSection":2},{"shortId":"m00043","platform":1,"platformAccount":5,"platformSection":3},{"shortId":"m00044","platform":1,"platformAccount":5,"platformSection":4},{"shortId":"m00045","platform":1,"platformAccount":5,"platformSection":5},{"shortId":"m00046","platform":1,"platformAccount":6,"platformSection":1},{"shortId":"m00047","platform":1,"platformAccount":6,"platformSection":2},{"shortId":"m00048","platform":1,"platformAccount":6,"platformSection":3},{"shortId":"m00049","platform":1,"platformAccount":6,"platformSection":4},{"shortId":"m00050","platform":1,"platformAccount":6,"platformSection":5},{"shortId":"m00051","platform":1,"platformAccount":7,"platformSection":1},{"shortId":"m00052","platform":1,"platformAccount":7,"platformSection":2},{"shortId":"m00053","platform":1,"platformAccount":7,"platformSection":3},{"shortId":"m00054","platform":1,"platformAccount":7,"platformSection":4},{"shortId":"m00055","platform":1,"platformAccount":7,"platformSection":5},{"shortId":"m00056","platform":1,"platformAccount":8,"platformSection":1},{"shortId":"m00057","platform":1,"platformAccount":8,"platformSection":2},{"shortId":"m00058","platform":1,"platformAccount":8,"platformSection":3},{"shortId":"m00059","platform":1,"platformAccount":8,"platformSection":4},{"shortId":"m00060","platform":1,"platformAccount":8,"platformSection":5},{"shortId":"m00061","platform":7,"platformAccount":15,"platformSection":13},{"shortId":"m00062","platform":7,"platformAccount":16,"platformSection":13},{"shortId":"m00063","platform":9,"platformAccount":0,"platformSection":14},{"shortId":"m00064","platform":9,"platformAccount":0,"platformSection":15},{"shortId":"m00065","platform":8,"platformAccount":17,"platformSection":0},{"shortId":"m00066","platform":8,"platformAccount":18,"platformSection":0},{"shortId":"m00067","platform":13,"platformAccount":0,"platformSection":0},{"shortId":"m00068","platform":3,"platformAccount":11,"platformSection":18},{"shortId":"m00069","platform":3,"platformAccount":12,"platformSection":18},{"shortId":"m00070","platform":14,"platformAccount":0,"platformSection":19},{"shortId":"m00071","platform":14,"platformAccount":0,"platformSection":20},{"shortId":"m00072","platform":9,"platformAccount":0,"platformSection":21},{"shortId":"m00073","platform":1,"platformAccount":1,"platformSection":22},{"shortId":"m00074","platform":1,"platformAccount":2,"platformSection":22},{"shortId":"m00075","platform":15,"platformAccount":0,"platformSection":0}]}'

# Load JSON data
data = json.loads(json_data)

# Extract the list of dictionaries
data_list = data['list']

# Mapping of platform values
platform_mapping = {
    1: "MKTPlatformYoutube",
    2: "MKTPlatformFacebook",
    3: "MKTPlatformInstagram",
    4: "MKTPlatformWhatsapp",
    5: "MKTPlatformEmail",
    6: "MKTPlatformTelegram",
    7: "MKTPlatformTwitter",
    8: "MKTPlatformKoo",
    9: "MKTPlatformApp",
    10: "MKTPlatformLinkedIn",
    11: "MKTPlatformGoogleAds",
    12: "MKTPlatformQuora",
    13: "MKTPlatformFacebookAds",
    14: "MKTPlatformWebsite",
    15: "MKTPlatformWhatsappChannel",
}

platform_account_mapping = {
    1: "MKTPlatformAccountYTMainHindi",
    2: "MKTPlatformAccountYTMainEnglish",
    3: "MKTPlatformAccountYTSadho",
    4: "MKTPlatformAccountYTShastraGyan",
    5: "MKTPlatformAccountYTYuvaMitra",
    6: "MKTPlatformAccountYTFreshBlades",
    7: "MKTPlatformAccountYTSaintsAndScriptures",
    8: "MKTPlatformAccountYTNotEvenOne",
    9: "MKTPlatformAccountFBMainHindi",
    10: "MKTPlatformAccountFBMainEnglish",
    11: "MKTPlatformAccountInstaMainHindi",
    12: "MKTPlatformAccountInstaMainEnglish",
    13: "MKTPlatformAccountWhatsAppOutreach",
    14: "MKTPlatformAccountWhatsAppRP",
    15: "MKTPlatformAccountTwitterHindi",
    16: "MKTPlatformAccountTwitterEnglish",
    17: "MKTPlatformAccountKooHindi",
    18: "MKTPlatformAccountKooEnglish",
    19: "MKTPlatformAccountLinkedInAPProfile",
    20: "MKTPlatformAccountLinkedInPAFPage",
}

platform_section_mapping = {
    1 :"MKTPlatformSectionYTDescription",
    2 :"MKTPlatformSectionYTPinnedComment",
    3 :"MKTPlatformSectionYTCard",
    4 :"MKTPlatformSectionYTEndSlide",
    5 :"MKTPlatformSectionYTCommunity",
    6 :"MKTPlatformSectionFBPage",
    7 :"DeprecatedMKTPlatformSectionFBAd",
    8 :"MKTPlatformSectionFBStories",
    9 :"MKTPlatformSectionInstaStories",
    10:"MKTPlatformSectionInstaProfileLink",
    11:"MKTPlatformSectionWhatsappBroadcast",
    12:"MKTPlatformSectionWhatsappStories",
    13:"MKTPlatformSectionTwitterFeed",
    14:"MKTPlatformSectionAppWisdomFeedH",
    15:"MKTPlatformSectionAppWisdomFeedE",
    16:"MKTPlatformSectionLinkedInPage",
    17:"MKTPlatformSectionWebsiteGrace",
    18:"MKTPlatformSectionInstaBroadcast",
    19:"MKTPlatformSectionWebsiteArticles",
    20:"MKTPlatformSectionWebsiteHome",
    21:"MKTPlatformSectionAppGitaFeed",
    22:"MKTPlatformSectionYTCommentReply"
}

# Replace "platform" values
for row in data_list:
    row['platformSection'] = platform_section_mapping.get(row['platformSection'], row['platformSection'])
    row['platformAccount'] = platform_account_mapping.get(row['platformAccount'], row['platformAccount'])
    row['platform'] = platform_mapping.get(row['platform'], row['platform'])

# Specify the CSV file path
csv_file_path = 'output.csv'

# Write to CSV
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = data_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    for row in data_list:
        writer.writerow(row)

print(f'CSV file "{csv_file_path}" has been created.')
