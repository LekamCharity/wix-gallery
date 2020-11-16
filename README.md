# Wix-gallery
## Author  
  
>[LekamCharity](https://github.com/LekamCharity/wix-gallery.git)  
  
# Description  
This is a wix-gallery app that displays various pictures and a brief description of them and it also allows users to upload images for others to see and be able to share by coping with the image link.
  
##  Live Link  
``` https://wixgallery.herokuapp.com/```

## Figma Link
```https://www.figma.com/file/TK30PJ6mXC5I0A56nfcndA/Untitled?node-id=0%3A1```
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Clone the repository:  
 ```
https://github.com/LekamCharity/wix-gallery.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Wix-gallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django 3.1.3]
* [Heroku]
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [lekamcharity@gmail.com]  

### License
  [MIT](https://github.com/LekamCharity/wix-gallery/blob/master/License) Copyright (c) 2020 Lekam Charity

