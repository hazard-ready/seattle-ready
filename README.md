# NOTES FOR THIS BRANCH

This branch represents an abortive attempt to add the ability to import rasters directly.  In case we decide to pick this up later, the following may be helpful:

1) Django doesn't currently seem to have a method to look up the data value from a raster at a given point.  `pixel_value_from_point` in [the django-raster source](https://github.com/geodesign/django-raster/blob/ea6f5aa94dd8d9ff8fab9e13d675905c787d78c6/raster/utils.py#L135) looks like it would do the trick
2) But the reason we didn't just go ahead and implement that was difficulty seeing how it would fit in to the general data model this project uses.
3) The string method for GDALRaster.bands appears to be broken, so don't rely on inspecting that to see if data's been loaded.
4) The code generation in import.py will be easier the more of the differences between vector & raster methods we can offload to generic ShapeManager and RasterManager classes.
5) If you end up making the database query a raster with vector (including point) data, it tries to polygonise the raster first, so takes AGES.  Take care to avoid this.  At the time of writing, Django's built in methods do not avoid this.


# seattle-ready
A disaster readiness website specific to the Seattle metro area.


The project is a custom instance of the [Disaster Preparedness](https://github.com/missoula-ready/disaster-preparedness) project, which is an adaptation of [a pioneering project from Oregon](https://github.com/Oregon-Public-Broadcasting/earthquake-preparedness) but has been generalized to make it easy to clone and tailor to other regions.

# To set it up, follow the instructions in the [Disaster Preparedness project README](https://github.com/missoula-ready/disaster-preparedness/blob/master/README.md). But instead of DJANGO_SECRET_KEY, use DJANGO_SECRET_KEY_SEATTLE, and instead of DATABASE_URL, use DATABASE_URL_SEATTLE.

Depending on your server setup, you may want to put these values in settings.py directly.

# Django language customization
Currently, there is no out-of-the box support for language codes cn (an abbreviated version of zh-hans, to make our URLs cleaner), and so (Somali). These instructions allow you to modfiy your Django installation to make it possible to navigate to /so/ and /cn/ to use this site in Somali and Chinese.

1. In ```venv/lib/python3.5/site-packages/django/conf/locale```, create a folder called `cn` and a folder called `so`
1. Copy the contents of the appropriate Chinese language folder into `cn` (curently, zh-Hans). This makes a Simplified Chinese language with the code `cn`.
1. Create a blank file called ``__init__.py`` in the `so` folder. In the `so` folder, create a folder named `LC_MESSAGES` and create a blank file named `django.mo` inside it. This sets up a dummy Somali translation, which is enough to fool Django into thinking it has a Somali version.

To finish adding languages, keys for `so` and `cn` are added to `django.conf.locale` in `settings.py`.

# Special data operations
There is one shapefile in disasterinfosite/data that is too big to host on github. It is called LSLD_steepslope.shp - so in this repo, it is LSLD_steepslope.shp.zip. Unzip it before doing a data add- and copy it to the reprojected folder if you don't have one, because that takes a long time.

# Values to put in Django Admin

### Tabs

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

### Supply kit

###### days
  3
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

