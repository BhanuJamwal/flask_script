from flask import Flask
from flask import request
from flask_cors import CORS
from twitter import *
from googleapiclient import discovery
from googleapiclient.errors import HttpError

twitter = Twitter(
    auth=OAuth('286527041-ST0spT2bWWbTLMYuslAvifLUOvUfb2L2NPMF9ku8', 'nZQdVsWxnET4QCOL3ELW2PLp9WUQmUlGBaCPNABPm2SnM',
               '83UTRFqWaX2qDHW5rtWyOMQpA', 'hKZfPzWITuYOTMVtgmBBGpHqavsQqakBvzIdluvnAtHK2ssLKK'))

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    searchTerm = request.args.get('query')
    api_key = "AIzaSyAbAJrY5fK62DnGBZUoH3RfxKTJRtVMr1g"
    youtube = discovery.build('youtube', 'v3', developerKey=api_key)
    req = youtube.search().list(q=searchTerm, part='snippet', type='video', maxResults=3)
    try:
        res = req.execute()
    except HttpError:
        res = {
            "etag": "AGm-Nm_lUVlARtp3XOGs-6IK-04",
            "items": [
                {
                    "etag": "ra1Pqrv1og7z57YvWWNb-i9IMMY",
                    "id": {
                        "kind": "youtube#video",
                        "videoId": "6GGSOVIlhHs"
                    },
                    "kind": "youtube#searchResult",
                    "snippet": {
                        "channelId": "UCTbNOCtAGaqOEnLMeo3JTeg",
                        "channelTitle": "CookingShooking Hindi",
                        "description": "Maggi, hum sabki all time favorite noodles, ab banaye street style me! Veg "
                                       "Masala Maggi ki recipe hindi me woh bhi sirf 5 minutes me. Spicy, tasty, "
                                       "yummy aur ...",
                        "liveBroadcastContent": "none",
                        "publishTime": "2017-04-20T10:35:28Z",
                        "publishedAt": "2017-04-20T10:35:28Z",
                        "thumbnails": {
                            "default": {
                                "height": 90,
                                "url": "https://i.ytimg.com/vi/6GGSOVIlhHs/default.jpg",
                                "width": 120
                            },
                            "high": {
                                "height": 360,
                                "url": "https://i.ytimg.com/vi/6GGSOVIlhHs/hqdefault.jpg",
                                "width": 480
                            },
                            "medium": {
                                "height": 180,
                                "url": "https://i.ytimg.com/vi/6GGSOVIlhHs/mqdefault.jpg",
                                "width": 320
                            }
                        },
                        "title": "Masala Maggi Recipe in Hindi | Indian Street Style Veg Maggie Noodles hindi me |"
                    }
                },
                {
                    "etag": "e9b_-H7ltRUfbnCNyOK9tHwFBGc",
                    "id": {
                        "kind": "youtube#video",
                        "videoId": "EQCHRkGmfRQ"
                    },
                    "kind": "youtube#searchResult",
                    "snippet": {
                        "channelId": "UCfwHP1M0AFSPqTdjzXhV0Zg",
                        "channelTitle": "CookingShooking",
                        "description": "Friends, today let's make our favorite Maggi in 2 ways... Chinese Maggi , "
                                       "and Cheese Chilli Maggi in street style! Do Subscribe to CookingShooking ...",
                        "liveBroadcastContent": "none",
                        "publishTime": "2019-11-16T07:20:12Z",
                        "publishedAt": "2019-11-16T07:20:12Z",
                        "thumbnails": {
                            "default": {
                                "height": 90,
                                "url": "https://i.ytimg.com/vi/EQCHRkGmfRQ/default.jpg",
                                "width": 120
                            },
                            "high": {
                                "height": 360,
                                "url": "https://i.ytimg.com/vi/EQCHRkGmfRQ/hqdefault.jpg",
                                "width": 480
                            },
                            "medium": {
                                "height": 180,
                                "url": "https://i.ytimg.com/vi/EQCHRkGmfRQ/mqdefault.jpg",
                                "width": 320
                            }
                        },
                        "title": "Maggi Recipe - Chinese &amp; Chilli Cheese Maggie Noodles - CookingShooking"
                    }
                },
                {
                    "etag": "k7C9TYcx8X5ukRh86cYw-GZBrUg",
                    "id": {
                        "kind": "youtube#video",
                        "videoId": "PWb1g36R1Qk"
                    },
                    "kind": "youtube#searchResult",
                    "snippet": {
                        "channelId": "UC5rlYCdiAzmDWug9wpx_uqQ",
                        "channelTitle": "STEVE AND MAGGIE ITALIANO",
                        "description": "Steve e maggie stanno giocando con i Monster Trucks oggi! Steve ha 5 "
                                       "gigantesche macchinine Monster truck ma non sa quale di queste sia la più "
                                       "veloce.",
                        "liveBroadcastContent": "none",
                        "publishTime": "2020-04-23T06:00:03Z",
                        "publishedAt": "2020-04-23T06:00:03Z",
                        "thumbnails": {
                            "default": {
                                "height": 90,
                                "url": "https://i.ytimg.com/vi/PWb1g36R1Qk/default.jpg",
                                "width": 120
                            },
                            "high": {
                                "height": 360,
                                "url": "https://i.ytimg.com/vi/PWb1g36R1Qk/hqdefault.jpg",
                                "width": 480
                            },
                            "medium": {
                                "height": 180,
                                "url": "https://i.ytimg.com/vi/PWb1g36R1Qk/mqdefault.jpg",
                                "width": 320
                            }
                        },
                        "title": "Monster trucks per Bambini con Steve e Maggie | Impara l&#39;italiano con Steve and Maggie Italiano"
                    }
                }
            ],
            "kind": "youtube#searchListResponse",
            "nextPageToken": "CAMQAA",
            "pageInfo": {
                "resultsPerPage": 3,
                "totalResults": 1000000
            },
            "regionCode": "IN"
        }
        return res
    print(res)
    return res




@app.route('/twitter-search')
def search_twitter_t():
    query = request.args.get('query')
    # search with query term and return 10
    results = twitter.search.tweets(q=query, count=5, type="popular")

    # return jsonify(results)
    # app.logger.debug(results)
    templateData = {
        'query': query,
        'tweets': results.get('statuses')
    }

    return templateData


if __name__ == '__main__':
    app.run(debug=True)
