# tag-pool
This simple project is created as an answer to growing amount of logistics within the control of the reach for the social media. Personally, I have noticed if you use the same tags with your post (by just copy/pasting them), social media such as instagram limits the number of people that come from these tags. My solution: create a pull of tags that are related to your instagram account, and pick random ones from the pool.

The application has logistic not to select the same tags within this iteration, but also the tags will not repeat the next time you generate the new ones.

It is still up to you to fillout the tags that you want to use inside the `hashes.txt` document.

If you uncomment the line 58 you can send these to your phone using the adb command. To do this make sure that adb is set to your path and you have phones connected and authenticated to use USB debuggin via Developer Settings of your phone.

To run, use: `python tags.py`
