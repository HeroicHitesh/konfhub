# Task Overview:

Complete the below mentioned task within 24 hours

Here is an API that provides the list of upcoming technical conferences. When you do a GET call for this REST API, you will get the list of conferences and their details in JSON format: 
```https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences```

The key and values for the JSON entries are self-explanatory. For example, some of the entries are:
```json
"confUrl": "https://futureconevents.com/events/san-antonio/",
"confStartDate": "06 Nov, 2019",
"entryType": "Paid",
```

The task you have in hand is to display the conference details in a webpage with each entry as a tile consisting of only the following entries: poster image, date, name of the conference, is it free or paid & place, and the link to visiting the conference website.

### Technology to use:
- Python or NodeJS

### Task to complete:
- Print the contents in a human readable format, e.g.: “San Antonio CyberSecurity Conference”,  November 6th, 2019, San Antonio, TX, US, Paid. https://futureconevents.com/events/san-antonio/”
- Identify exact duplicates (if any)
- Identify semantic duplicates (i.e., the conferences are same but the details provided are slightly different, e.g., “React Conference 2019” in one entry and “ReactConf ‘19” in another entry but the other fields are same or similar).

### What you should share:
- Submit the GitHub URL once you complete this task.