# Jobs

-----------------

You have to choose between "New" and "List".

## Job Creation

![Jobs Interface](/images/web_ui/jobs_new_interface.png)

**To change Map Settings :** Click on ![Map Settings](/images/web_ui/jobs_mapsettings.png)

**To create a new job :** You have to enter a location.
Then, in "Global Parameters" you have to:

![Jobs Global Parameters](/images/web_ui/jobs_new_global_parameters.png)

- Choose a job's name
- Choose a process to apply : you have a list with all processes and you have to choose one of them.
- Choose an existing dataset

When this step is done, you have two possibilies :

- **Choose an image** (or two images for a process of **change detection**). You can select constellation(s) between PLEIADES, SPOT, ZEPHYR, SENTINEL-2 and DEIMOS 2. You can choose a date (start or end to select a category of image). ![Jobs Image Selection](/images/web_ui/jobs_new_image_selection.png)

- **Choose a zone**. For that you have to click on "Select or Drop file" and import a local GeoJSON file (max 100 Mo and one polygon). ![Jobs Zone Selection](/images/web_ui/jobs_new_zoneimport.png)

If you want to select a zone to apply the processC click on ![Jobs Edit](/images/web_ui/jobs_new_edit.png). Or you can apply the process on full image.

For selecting a zone : on the map you have access to tools for **drawing zone**.
When you have your zone you can click on *Launch* to apply the process. You can see the number of estimated [tiles](interface.md) and the estimated cost.

![Jobs Launch](/images/web_ui/jobs_launch.png)

## Job List

In this section you can access to all of the jobs already created. For that you have different functions : **Search**, **Create**, **Delete**, **Refresh**.

![Jobs List](/images/web_ui/jobs_list.png)

For all jobs you can choose an action on the column "Actions" :

![Jobs Actions](/images/web_ui/jobs_actions.png)

- **Visualize job** : You can see results of the selected job and the details about the status of them.
- **Object Detection** :
    - View : You can see zones and records of the selected job.
    - Edit : It enables you to modify the job, you can access to all of drawing tools of the map. You can see the [Dataset Page](dataset.md "Dataset Page") for further details.
    - [Validate](usecase.md "Use Case")
    - Duplicate
    - Download as GeoJSON
    - Download as KML