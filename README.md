# autophotouploadgphoto
Using gphoto and Google API, a python controlled DSLR can continually take photos, rename them, save them to the raspberry pi, and then upload them to the google drive account of the user's choice. 
You can display photos by uncommenting out the code. I do not recommend, because at it's current stage, it will only close via alt-f4. I recommend running in Geanie. 
You will need to change the code according to your directories, as well as the name you set your JSON file to from your own google API project (you will need to create your own client key, but the code will work regardless).
You will need a few libraries installed to your RPi. Gphoto2, and several google libraries. 
Here are links to some resources I used:
https://developers.google.com/api-client-library/python/apis/drive/v2
https://developers.google.com/drive/api/v3/quickstart/python
http://www.gphoto.org/proj/libgphoto2/support.php
https://www.youtube.com/watch?v=1eAYxnSU2aw

