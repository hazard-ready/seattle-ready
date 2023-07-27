# seattle-ready
A disaster readiness website specific to the Seattle metro area.

The project is a custom instance of the [Disaster Preparedness](https://github.com/hazard-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/hazard-ready/disaster-preparedness/blob/master/README.md).
Information that is unique to Seattle Ready, as opposed to any other Hazard Ready instance, is below.

# Django language customization
Currently, there is no out-of-the box support for language codes cn (an abbreviated version of zh-hant, to make our URLs cleaner), and so (Somali). These instructions allow you to modfiy your Django installation to make it possible to navigate to /so/ and /cn/ to use this site in Somali and Chinese.

1. In ```venv/lib/python3.5/site-packages/django/conf/locale```, create a folder called `cn` and a folder called `so`
1. Copy the contents of the appropriate Chinese language folder into `cn` (curently, zh-Hant). This makes a Traditional Chinese language with the code `cn`.
1. Create a blank file called ``__init__.py`` in the `so` folder. In the `so` folder, create a folder named `LC_MESSAGES` and copy the file named `django.mo` from the equivalent location in any other language's folder. This sets up a dummy Somali translation, which is enough to fool Django into thinking it has a Somali version.

To finish adding languages, we have added `so` and `cn` to `django.conf.locale` in `settings.py`.

# Special data operations
There is one shapefile in disasterinfosite/data that is too big to host on github. It is called LSLD_steepslope.shp - so in this repo, it is LSLD_steepslope.shp.zip. Unzip it before doing a data add- and copy it to the reprojected folder if you don't have one, because that takes a long time.

### Deploying to the web via Docker
This repository has a Dockerfile that lets you build a Docker image of the Django app. It needs you to have `DATABASE_URL` and `DJANGO_SECRET_KEY` set in your environment, but it is also able to guess sensible defaults for these values.

Do `docker build . --tag seattle-ready` and you can run it. It will set up the Python environment for you. Depending on the state of the database you're connecting to, you will likely need to start at the `python manage.py migrate` step under "Load some data".

For an example of a working production environment, see the `docker-compose.yml` in the [base repository](https://github.com/hazard-ready/disaster-preparedness)


# Values to put in Django Admin

### Shapefile Groups
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

### Snugget Sections
  What you can expect: 0
  What's the worst that could happen: 1
  Be ready, get prepared: 2
  Other important details for your location: 3, collapsible
  During a flood: 4, collapsible
  During an earthquake: 4, collapsible
  During a landslide: 4, collapsible
  During a wildfire: 4, collapsible
  During a volcanic eruption: 4, collapsible
  During a winter storm: 4, collapsible
  During a heat wave: 4, collapsible
  Past earthquakes in King County: 5, collapsible
  Past summer events in the region: 5, collapsible
  Past winter storms in the region: 5, collapsible
  Past wildfires in the region: 5, collapsible
  Past eruptions in the Pacific Northwest: 5, collapsible
  Past landslides in Washington: 5, collapsible
  Past floods in the region: 5, collapsible

### Site Settings

###### Area Name
King County, Washington

###### About Text
This site is a collaboration of HazardReady, the University of Montana, King County, and the City of Seattle.

###### Contact Email
info@hazardready.org

###### Site title
Seattle and King County Ready

###### Site URL
https://hazardready.org/seattle

###### Site description
A disaster preparedness website

###### Intro Text
A natural disaster could strike your area at any time. Find out about where you live, work, or play in King County, WA.

###### Who Made This
Have questions? View the <a href="/about" target="_blank">About</a> page or <a href="mailto:software@hazardready.org">email the Hazard Ready creators</a> for more information.

###### Data Download
https://github.com/hazard-ready/seattle-ready/blob/master/disasterinfosite/data.zip
