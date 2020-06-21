# Blue1984
### Twitter without censorship
### Python microservice for twitter scrapping

![1984v2 008](https://user-images.githubusercontent.com/26343374/83402867-3f7fe600-a410-11ea-9b57-af6149521fff.jpeg)

This anti-censorship app for twitter was designed from scratch especially for Bluzelle hackathon.

Official site: https://blue1984.herokuapp.com/

Video demo: https://youtu.be/O3uLL3kWXAY

## Project repostories

Server: https://github.com/MikaelLazarev/blu1984 (core repository)

Mobile apps: https://github.com/MikaelLazarev/blue1984-mobile

Front-end: https://github.com/MikaelLazarev/blue1984-web

Twitter scrapper microservice: https://github.com/MikaelLazarev/blue1984-scrapper

## How to install

1. Clone repository ```git clone https://github.com/MikaelLazarev/blue1984-ts```

2. Create virtual enviroment: ```python3 -m venv /path/to/new/virtual/environment```

3. Activate environment: ```source /path/to/new/virtual/environment/bin/activate```

4. Install dependecies: ```pip3 install -r requirements.txt```

5. Setup SECRET phrase up as enviroment variable: ```export SECRET=<YOUR SECRET>```

6. Run service with ```gunicorn wsgi:app```

7. For testing, open / and get "It works message"

Freedom to share your own thought is a key need for all people. Today, some social nwtworks could block and delete accounts or tweets like censors. This power limits freedom and could be used by goverments / corporations against society.

![Screenshot 2020-06-01 at 00 45 22](https://user-images.githubusercontent.com/26343374/83402860-398a0500-a410-11ea-83d8-ab2566de8fc8.png)

## Disclaimer

This application is provided "as is" and "with all faults." Me as developer makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this software. There are inherent dangers in the use of any software, and you are solely responsible for determining whether this software product is compatible with your equipment and other software installed on your equipment. You are also solely responsible for the protection of your equipment and backup of your data, and THE PROVIDER will not be liable for any damages you may suffer in connection with using, modifying, or distributing this software product.

## Technical stack

* Python 3.8
* Flask
* Twitter scrapperlib

