# Heroku Hipchat
 
## Overview
 
Send heroku webhook notification using Hipchat API v2

## Installation

First ensure you have installed [heroku-toolbelt](https://toolbelt.heroku.com/). 
You can test success of installation with following command:

    heroku --version
    
### Webhook service

Create and deploy application using source code from this repository:

    heroku create
    git push heroku master
    heroku ps:scale web:1

and configure your notification:

    heroku config:set HIPCHAT_ROOM=<ROOM_ID>
    heroku config:set HIPCHAT_TOKEN=<TOKEN>

Your webhook service is now deployed and ready to use. To retrieve url for notification check on heroku admin panel or
type:

    heroku domains

### Your application

After webhook is installed change folder to your application and configure deployhooks addon like this:

    heroku addons:add deployhooks:http --url=https://<webhook.domain>/deployed
