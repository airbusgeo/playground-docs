# Zones

-----------------

A **<span style="color:#ff9900">zone</span>** corresponds to an AOI (Area of Interest) on selected image(s). More precisely, a zone can be summarized as a list of web map tiles at a certain geographical location and specific satellite images.

![Zone interface](/images/web_ui/zone_interface.png)

1. Enables you to **<span style="color:#ff9900">create</span>** a new zone.
2. Enables you to **<span style="color:#ff9900">delete</span>** the selected zone(s)
3. Enables you to access to zone **<span style="color:#ff9900">option</span>** :
    * Zone Edition
    * To edit zone properties : Name and description

-----------------

### <span style="color:#2980b9">Zone Creation</span>

Before creation you can access to zone creation interface by zone list and you have to select the dataset where your new zone will be save.

![Zone Creation](/images/web_ui/zone_drawing.png)

1. You have to choose the location and an image (or two images for change detection) . When this step is done, you have two possibilies : import a zone or draw a zone.
2. **Import a zone** : For that you have to click on "Select or Drop file" and import a local GeoJSON file (max 100 Mo and one polygon). Example of GeoJSON file format for the import (keep just the **geometry** part) : ![GeoJSON file](/images/web_ui/jobs_new_GeoJSONfile.png)
3. **Draw zone** : On the map you have access to **drawing zone** tools :
    * Draw a polygon : with several points
    * Draw a rectangle : with two points
    * Delete a zone
4. Write a name for your zone and save it.

-----------------

For **zone edition**, the interface is the same. It enables you to update your zone : name or geom.