# heroku-notepad
Project Name: "This is How We Roll"

This repository was used for Heroku App Deployment

Group Members
- Morgaine Bowers
- Trumane Lee
- Sydney Cavallaro
- Ana Linda Penny

Project Goals:
- Tell a story using data visualizations and provide an interactive means to explore the data itself.

Specific Project Requirements
- Your visualization must include a Python Flask–powered API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).
- Your project should fall into one of the below four tracks:
- A custom “creative” D3.js project (i.e., a nonstandard graph or chart).
- A combination of web scraping and Leaflet or Plotly.
- A dashboard page with multiple charts that update from the same data.
- A “thick” server that performs multiple manipulations on data in a database prior to visualization (must be approved)
- Your project should include at least one JS library that we did not cover.
- Your project must be powered by a data set with at least 100 records.
- Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
- Your final visualization should ideally include at least three views. 

Project Name Ideas:
- Roller Coaster Ups and Downs.
- This is How We Roll
- Coasters, Roll Out!
- Rockin’ Roller Coasters

Datasets Used
- Roller Coaster Database: https://rcdb.com/ via web scraping through flask.
- Scraping Site Homepage, Record Holder page, Census page, and Worldview page.
- Add web-scraped data to MongoDB.


New Javascript Library
- Chartist.js: http://gionkunz.github.io/chartist-js/ 

Visualizations
- Heatmap comparing populations vs number of roller coasters (Leaflet & Mapbox)
- Random coaster displayed with stats year built, speed, and height on homepage on refresh.
- International map outlining countries and detailing the number of coasters per country. (Leaflet & Mapbox)
- Pie chart comparing types of roller coasters by sit down, inverted, suspended, wing, flying, stand-up, and bobsled. (Chartist.js)
- Record Holder on Maps with pins that detail city, state, country, and indicated records speeds vs. height (Leaflet & Mapbox).

Core Tasks
- Brainstorm and select a “title” for the project Check!
- Write code to web-scrape the Roller Coaster Database Website (Python) Check!
- Write flask app code for database connection (Python) Check!
- Build Website (Templates): Sydney
- Create Index.html: Check!
- Introduction of the Team page - A. Linda
- May include on this page a section to indicate what data, languages & libraries were used along with a brief ETL description --OR-- depending on the volume, we may want to consider having this info on it’s own separate page.  - A. Linda
- Build CSS: Check!
- Visualization Dashboards 
- Write D3.js code for interactive graph (Javascript) - Trumane
Interactions
    - Year built vs. Speed
    - Year Built vs. Height
    - Year Built vs. Length
    - Year Built vs. Drop
- Write Chartist.js code for Pie Chart comparison of roller coaster type.(Javascript) Sydney
- Random scraped coaster on homepage (Python) Sydney & Trumane
- Heat map of roller coaster vs. population density (Leaflet & Mapbox) 
- Map of countries with roller coaster information pop ups (Leaflet & Mapbox) Morgaine
- Find a GeoJSON for countries: https://datahub.io/core/geo-countries
- Record Holders map with markers & popups (Leaflet & Mapbox) Morgaine
Heroku Deployment - Trumane

Ambitious Tasks
- Reactivity when changing the size of the window
- Add Latest/Upcoming Roller Coasters (5 Newest)
- Footers on every page?
- Scrape World View Statistics for index.html page
- Plots comparing year built to speed, height, length, and drop (D3.js for each) with interactive D3-tip.js.

Create a glossary
Coaster Type
Steel - a roller coaster with tracks consisting of steel.
Wood - a roller coaster with tracks consisting of layers of wood. Occasionally wooden roller coasters will use steel structures to support the wooden track, this does not have an affect on its wooden status.
Thrill-Scale
Tame: Small, Compact Roller Coasters and Kiddie Coasters
For Riders: kids, parents with their kids, novices, and desperate coaster enthusiasts trying to increase their coaster count
Examples: Taxi Jam at Kings Dominion, Percy’s Railway at Six Flags Magic Mountain, Blackbeard’s Lost Treasure Train at Six Flags Great Adventure, Catwoman’s Whip at Six Flags New England
Traditional: Old-School Run of the Mill Woodies & Smaller Steel Coasters
For Riders: A large portion of the general public as well as all coaster fans will be candidates for these roller coasters.
Examples: Thunderhead at Dollywood, Racer at Kings Island, Phoenix at Knoebels, Twister at Knoebels, Big Thunder Mountain Disney World
Thrilling: Contains 1 Thrill Factor (Loops, Launch)
For Riders: General public visitors with a little more bravery.
Examples: Mindbender at Six Flags Over Georgia, Anaconda at Kings Dominion, Italian Job (Backlot Stunt) Coasters at Kings Dominion & Kings Island, Carolina Cobra at Carowinds, Pony Express at Knott’s Berry Farm
Intense: Contains 2 Thrill Factors (High Speeds, Loops, G-Forces, Height) 
For Riders: Expect fewer general public riders on these coasters. 
Examples: Stormrunner at Hersheypark, Griffon at Busch Gardens Europe, Volcano at Kings Dominion, Goliath at Six Flags Over Georgia & Magic Mountain, Superman Ride of Steel at Six Flags America, Millennium Force at Cedar Point
Extreme: Contains 3 Thrill Factors (High Speeds, Loops, G-Forces, or Height)
For riders: Only thrill seekers and coaster enthusiasts need apply.
Examples include X2 at Six Flags Magic Mountain, Kingda Ka at Six Flags Great Adventure, Tatsu at Six Flags Magic Mountain, Top Thrill Dragster at Cedar Point
Coaster Design
Sit Down - a traditional roller coaster ridden while sitting down.
Inverted - a roller coaster in which the train runs under the track with the seats directly attached to the wheel carriage. This latter attribute is what sets it apart from the older suspended coaster, which runs under the track, but swings via a pivoting bar attached to the wheel carriage. Inverted coasters are notable for their reversed orientation compared to a traditional roller coaster, with the legs rather than the arms exposed.
Suspended - a roller coaster using trains which travel beneath the track and pivot on a swinging arm from side to side, exaggerating the track's banks and turns.
Wing - Coaster differs from many traditional steel roller coasters in that its trains are not located above or below the track but rather on the sides, a configuration that gives riders the impression of free flight.
Flying - roller coaster meant to simulate the sensations of flight by harnessing riders in a prone position during the duration of the ride. The roller coaster cars are suspended below the track, with riders secured such that their backs are parallel to the track.
Stand Up - a coaster ridden while standing up instead of sitting down.
Bobsled - designed like a bobsled run -- without a fixed track. The train travels freely through a trough.
Pipeline - a coaster where riders are positioned between the rails instead of above or below.
Coaster Status
Operating: Currently, fully functional and operating coaster for riders to enjoy the thrill.
In-Storage: Currently not operational and potentially being set for relocation or re-engineering.
Under Construction: Currently being engineered and preparing for future.
SBNO: Standing but no longer operational.
Relocated: Coaster has been relocated to another amusement park.
Unknown: Status of coaster is unknown due access to amusement park data.


