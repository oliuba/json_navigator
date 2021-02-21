# Json Navigator

This program is created to navigate in __.json files__.
As a result, user interacts and gets .json file fields and their values.

On each stage of .json file there are two modes the user can choose:
- The first one shows the whole object (dictionary or list) to user.
- The second one shows dictionary keys if the object is dictionary and asks user the list element s/he wants to see.

The module contains *5 functions*, which serve for the problem solving.
The program is created for entartainment and easier navigation in .json files.

There are no special requirements or additional libraries for this module.

## How to use the program?

> To use the program, download json_analysis.py and start it. 
> You will be asked to enter the path to a .json file. Then you will see if the field is dictionary or list.
> You will need to choose whether to see the whole object or only its smaller part.
> This will continue until you reach the end of the navigation (the object will be not a dictionary or list).
> If you make a wrong input on any stage, the program will stop running and you will need to start it again.

### An example of the program use

```sh
>>> python json_analysis.py
Please enter the name of the .json file you would like to navigate in: frienfs_list_Obama.json
This field is a dictionary.
Would you like to see the whole object (1) or only its keys (2)?
Enter a number: 2
['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
Please enter the field you would like to see further information about: users
This field is a list.
Would you like to see the whole object (1) or only its particalar element by number (2)?
Enter a number: 2
Please enter the number (lower than 10) of the list element you would like to see:
7
This field is a dictionary.
Would you like to see the whole object (1) or only its keys (2)?
Enter a number: 2
['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
Please enter the field you would like to see further information about: entities
This field is a dictionary.
Would you like to see the whole object (1) or only its keys (2)?
Enter a number: 1
{'description': {'urls': []}}
Please enter the field you would like to see further information about: description
This field is a dictionary.
Would you like to see the whole object (1) or only its keys (2)?
Enter a number: 2
['urls']
Please enter the field you would like to see further information about: urls
This field is a list.
Would you like to see the whole object (1) or only its particalar element by number (2)?
Enter a number: 1
[]
The object is empty. The navigation is finished.
```

#### Have fun using json_nagigator program!