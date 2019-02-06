# Import

-----------------

This section enables you to do an import in the OneAtlas Playground. You can see the import list :
![Import Interface](/images/web_ui/import.png)

To do **new import** click on "New import" button :
![New Import](/images/web_ui/import_new.png)

You have to :

1. You can see a default import name but you can change it
2. Select an existing dataset
3. Enter an URL **OR** Select a file. If you want to drop the selected file you can click on :![Drop File](/images/web_ui/import_dropfile.png)
4. Click on "Submit"

-----------------

# Export

-----------------

This section enables you to export data.

## Export Creation

![New Export](/images/web_ui/export_new.png)

You have to :

1. Choose a type between : **Tile**, **Mask**, **Thumbnail**, **Vector**, **Zone**. Then you have to choose the corresponding features, you can see the table below for more details.
2. Choose an Export Name
3. Choose an existing dataset (or several)
4. Click on "Submit"

**_Types Features :_**

|               |Projection       |Zoom             |Padding          |
| ------------- |: -------------: |: -------------: |: -------------: |
|Tile           |![O](/images/web_ui/1.png)|![O](/images/web_ui/1.png)|![O](/images/web_ui/1.png)|
|Mask           |![1](/images/web_ui/2.png)|![O](/images/web_ui/1.png)|![1](/images/web_ui/2.png)|
|Thumbnail      |![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![O](/images/web_ui/1.png)|
|Vector         |![O](/images/web_ui/1.png)|![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|
|Zone           |![O](/images/web_ui/1.png)|![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|

## Export List

![Export View](/images/web_ui/export_view.png)

You can see the export list, with the Information column you can access to the main informations about an export and if you want to download this export you can lick on ![More](/images/web_ui/datasets_more.png), and choose between :

- Copy GS url
- Copy HTTP url

With these URL you can access to the export (with a bucket).