import os
import logging
from flask import Flask, request, jsonify
from twitter_scraper import Profile, get_tweets

app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


secret = os.getenv('SECRET', '1234')


@app.route('/')
def index():
    return 'it works!'


@app.route('/profile/<account>')
def profile(account=None):
    
    if 'Authorization' not in request.headers or request.headers['Authorization'] != 'Basic ' + secret:
        response = jsonify({'error': 'Wrong token'})
        response.status_code = 403
        return response

    if account is None:
        response = jsonify({'error': 'Incorrect id'})
        response.status_code = 403
        return response

    app.logger.info('Getting profile for ' + account)

    try:
        tw_profile = Profile(account)
    except IndexError:
        response = jsonify({'error': 'ID NOT FOUND'})
        response.status_code = 404
        return response

    prof = tw_profile.to_dict()

    app.logger.info('Got profile for ' + account);

    return jsonify({
        'screenName': prof['username'],
        'profileImage': prof['profile_photo'],
        'name': prof['name'],
        'bio': prof['biography'],
        'tweetCount': prof['tweets_count'],
        'followingCount': prof['following_count'],
        'followerCount': prof['followers_count'],
        'likeCount': prof['likes_count'],
    })


@app.route('/timeline/<account>')
def timeline(account=None):
   
    # if 'Authorization' not in request.headers or request.headers['Authorization'] != 'Basic ' + secret:
    #     response = jsonify({'error': 'Wrong token'})
    #     response.status_code = 403
    #     return response
    #
    # if account is None:
    #     response = jsonify({'error': 'Incorrect id'})
    #     response.status_code = 403
    #     return response

    result = []
    app.logger.info('Getting timeline for ' + account)

    for tweet in get_tweets(account, pages=3):
        result.append({
            'id': tweet['tweetId'],
            'screenName': tweet['username'],
            'text': tweet['text'],
            'time': tweet['time'],
            'urls': tweet['entries']['urls'],
            'hashtags': tweet['entries']['hashtags'],
            'images': tweet['entries']['photos'],
            'favoriteCount': tweet['likes'],
            'replyCount': tweet['replies'],
            'retweetCount': tweet['retweets'],
            })

    app.logger.info('Got result for ' + account + '\n' + result);
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=os.getenv('PORT', 5000))
