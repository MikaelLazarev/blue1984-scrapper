# Blue1984
### Twitter without censorship
### Python microservice for twitter scrapping

![1984v2 008](https://user-images.githubusercontent.com/26343374/83402867-3f7fe600-a410-11ea-9b57-af6149521fff.jpeg)

This anti-censorship app for twitter was designed from scratch especially for Bluzelle hackathon.

Official site: https://blue1984.herokuapp.com/

Video demo: https://youtu.be/O3uLL3kWXAY

Backend: https://github.com/MikaelLazarev/blu1984

Front-end: https://github.com/MikaelLazarev/blue1984

Python microservice for twitter scrapping: https://github.com/MikaelLazarev/blue1984-ts

## How to install

1. Clone repository ```git clone https://github.com/MikaelLazarev/blue1984-ts```

2. Create virtual enviroment: ```python3 -m venv /path/to/new/virtual/environment```

3. Activate environment: ```source /path/to/new/virtual/environment/bin/activate```

4. Install dependecies: ```pip3 install -r requirements.txt```

5. Setup SECRET phrase bys setting SECRET enviroment variable: ```SECRET=<YOUR SECRET>```

6. Run service with ```gunicorn wsgi:app```

7. For testing, open / and get "It works message"

Freedom to share your own thought is a key need for all people. Today, some social nwtworks could block and delete accounts or tweets like censors. This power limits freedom and could be used by goverments / corporations against society.

![Screenshot 2020-06-01 at 00 45 22](https://user-images.githubusercontent.com/26343374/83402860-398a0500-a410-11ea-83d8-ab2566de8fc8.png)

## User Story

Blue1984 scans all accounts you are interested for. It aoutmatically copies them into decentralised Bluzelle DB. If twitter deletes or changes any tweet, it founds differences and hightlights changed / deleted tweets. There is no regitstry flow for providing additional privacy.

![Screenshot 2020-06-01 at 09 39 52](https://user-images.githubusercontent.com/26343374/83402864-3d1d8c00-a410-11ea-97ce-708ca3d69721.png)

Even if your server would be blocked by authority, you could start another one, thanks for Bluzelle all data is stored in decentralised database, so nothing would be deleted!

![Screenshot 2020-06-01 at 12 49 11](https://user-images.githubusercontent.com/26343374/83402866-3e4eb900-a410-11ea-9455-8adb760cbf86.png)

## Web and mobile version

You could connect using web or mobile devices (works both on iOS and Android):

<img src='https://user-images.githubusercontent.com/26343374/83404016-7ce57300-a412-11ea-947b-9be3bbbf07d5.png' width='21%'/>&nbsp;&nbsp;&nbsp;<img src='https://user-images.githubusercontent.com/26343374/83404020-7f47cd00-a412-11ea-9422-ec1211715b1d.png' width='21%'/>&nbsp;&nbsp;&nbsp;<img src='https://user-images.githubusercontent.com/26343374/83404018-7eaf3680-a412-11ea-94cb-321941c54c12.png' width='21%'/>&nbsp;&nbsp;&nbsp;<img src='https://user-images.githubusercontent.com/26343374/83404017-7eaf3680-a412-11ea-90cb-fd732463cc0d.png' width='21%'/>

## Disclaimer

This application is provided "as is" and "with all faults." Me as developer makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this software. There are inherent dangers in the use of any software, and you are solely responsible for determining whether this software product is compatible with your equipment and other software installed on your equipment. You are also solely responsible for the protection of your equipment and backup of your data, and THE PROVIDER will not be liable for any damages you may suffer in connection with using, modifying, or distributing this software product.

## Technical stack

* Typescript
* React / React-native for client
* Nodejs & express for server
* Bluzelle DB
* Node cache

