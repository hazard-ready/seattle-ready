# seattle-ready
A disaster readiness website specific to the Seattle metro area.


The project is a custom instance of the [Disaster Preparedness](https://github.com/missoula-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/missoula-ready/disaster-preparedness/blob/master/README.md).

# This instance of Hazard Ready uses Webpack to bundle its static files. For that reason, you need these additional steps to set it up:
1. Make sure that you have [Node and NPM installed](https://www.npmjs.com/get-npm)
1. In the same directory (```disasterinfosite```) that contains ```package.json```, run ```npm install```
1. Run ```npm run webpack```


Depending on your server setup, you may want to put these values in settings.py directly.

# Django language customization
Currently, there is no out-of-the box support for language codes cn (an abbreviated version of zh-hans, to make our URLs cleaner), and so (Somali). These instructions allow you to modfiy your Django installation to make it possible to navigate to /so/ and /cn/ to use this site in Somali and Chinese.

1. In ```venv/lib/python3.5/site-packages/django/conf/locale```, create a folder called `cn` and a folder called `so`
1. Copy the contents of the appropriate Chinese language folder into `cn` (curently, zh-Hans). This makes a Simplified Chinese language with the code `cn`.
1. Create a blank file called ``__init__.py`` in the `so` folder. In the `so` folder, create a folder named `LC_MESSAGES` and copy the file named `django.mo` from the equivalent location in any other language's folder. This sets up a dummy Somali translation, which is enough to fool Django into thinking it has a Somali version.

To finish adding languages, we have added `so` and `cn` to `django.conf.locale` in `settings.py`.

# Special data operations
There is one shapefile in disasterinfosite/data that is too big to host on github. It is called LSLD_steepslope.shp - so in this repo, it is LSLD_steepslope.shp.zip. Unzip it before doing a data add- and copy it to the reprojected folder if you don't have one, because that takes a long time.

# Values to put in Django Admin

### Tabs
Note: because this site is translated, you can find the translations for these values in ```admin-strings.xlsx```

######Earthquake
    Display Name: Earthquake
    Order: 0
    Likely Scenario Title:
    Likely Scenario Text:

######Flood
    Display Name: Flood
    Order: 1
    Likely Scenario Title:
    Likely Scenario Text:

######Landslide:
    Display Name: Landslide
    Order: 2
    Likely Scenario Title:
    Likely Scenario Text:

######Fire
    Display Name: Wildfire
    Order: 3
    Likely Scenario Title:
    Likely Scenario Text:

######Volcano
    Display Name: Volcano
    Order: 4
    Likely Scenario Title:
    Likely Scenario Text:

######Winter
    Display Name: Winter Weather
    Order: 5
    Likely Scenario Title:
    Likely Scenario Text:

######Summer
    Display Name: Summer Weather
    Order: 6
    Likely Scenario Title:
    Likely Scenario Text:

### Section orders

###### Snugget Section
  What to expect: 0
  How to prepare: 1
  In Recent History: 2

###### Snugget Subsection
Note that these may appear in different sections or be mutually exclusive, which is why some of them have the same order.

  In Your Lifetime: 0

  Cascadia Quake: 1

  What's the Worst: 2

  Erosion Risk: 3

  Climate Impacts: 3

  If the dams failed: 3

  Tsunami Zone: 3

  Liquefaction: 4

  Unstable Structures: 5

  Warning Signs: 6

  Before: 7

  During: 8

  After: 9

  Local Resources: 10

  What's Happened?: 11

  Historical Images: 12

### Important links
  Title: King County Emergency Management
  Link: ```Find out more about local resources and information at the <a href="http://www.kingcounty.gov/depts/emergency-management.aspx" target="_blank">King County EM website</a>.```

  Title: Alert King County
  Link: ```Get real-time alerts about what's happening in King County. Find out more <a href="http://www.kingcounty.gov/depts/emergency-management/alert-king-county.aspx" target="_blank">here</a>.```

  Title: Alert Seattle
  Link: ```Be the first to know what's happening near you. Find out more <a href="http://alert.seattle.gov" target="_blank">here</a>.```

  Title: Seattle Office of Emergency Management
  Link: ```The <a href="http://www.seattle.gov/emergency-management" target="_blank">Seattle OEM</a> website has many great resources for finding out more.```

### Supply kit

###### days
  10
###### text
Supply kit text goes here

### Location Information

###### Area Name
King County

###### Community Leaders
This section is not used on this site.

### Settings

###### About Text
This site is a collaboration of HazardReady, the University of Montana, King County, and the City of Seattle.

###### Site title
Seattle and King County Ready

###### URL
https://hazardready.org/seattle

###### Site description
A disaster preparedness website

###### Intro Text
A natural disaster could strike your area at any time. Find out about where you live, work, or play in King County, WA.

###### Who Made This
`This is based on <a href="http://www.opb.org/news/widget/aftershock-find-your-cascadia-earthquake-story/" target="_blank">Aftershock</a>, an earthquake preparedness application for Oregon residents. Carson MacPherson-Krutsky and <a href="https://hs.umt.edu/geosciences/faculty/bendick/" target="_blank">Dr. Rebecca Bendick</a>, a graduate student and her advisor at the Unversity of Montana, had the idea to expand it for other locales and types of disasters. <a href="https://github.com/nein09" target="_blank">Melinda Minch</a> and <a href="https://github.com/eldang" target="_blank">Eldan Goldenberg</a> adapted it for that purpose. Source for a general-purpose version of this site is available on <a href="https://github.com/missoula-ready/disaster-preparedness" target="_blank">Github</a>.
<br/>
Content and data are supported by several entities including the <a href="http://www.umt.edu/" alt="logo" target="_blank">University of Montana</a>, <a href="http://www.kingcounty.gov/" alt="logo" target="_blank">King County</a>, and the <a href="http://www.seattle.gov/" alt="logo" target="_blank">City of Seattle</a>.
<br/>
<img class="who-made-this-logo umt-logo" src="static/img/umt_logo.png">
<img class="who-made-this-logo county-logo" src="static/img/kc_logo_bw.gif">
<img class="who-made-this-logo city-logo" src="static/img/seattle_logo_bw.png">`

###### Data Download
https://github.com/hazard-ready/seattle-ready/blob/master/disasterinfosite/data.zip

###### Past Events Photos
Upload photos to show in a photo gallery in the search results, under Past Events. Make sure that the heading you enter here matches the heading that the photos will appear under.

###### Data Overview Images
In the box at the bottom of every page, there's a section called 'Quick Data Overview'. That's where these will show up, as links that open in a new tab or window. The link_text field is what the link says, like 'Earthquakes: Distance from a Fault', and you can upload the appropriate image here.

### Deploying to the web via Apache
There are directories called 'photos' and 'data' in disasterinfosite/img. This is where images go when you upload them via Django Admin, under 'Photos of Past Events' and 'Data Overview Images'. In order for that upload to work, you need to change the owner (chown) those directories to whatever user Apache is running as (www-data, perhaps).

### Deploying to the web via Docker
This repository has a Dockerfile that lets you build a Docker image of the Django app. It needs you to have `DATABASE_URL` and `DJANGO_SECRET_KEY` set in your environment, but it is also able to guess sensible defaults for these values.

Do `docker build . --tag seattle-ready` and you can run it. It will set up the Python environment for you. Depending on the state of the database you're connecting to, you will likely need to start at the `python manage.py migrate` step under "Load some data".

For an example of a working production environment, see the `docker-compose.yml` in the [base repository](https://github.com/hazard-ready/disaster-preparedness)
