# Import

-----------------

This section enables you to do an import in the Intelligence Playground. You can see the import list :
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

You have to click on **New Export** :

![New Export](/images/web_ui/export_new.png)

You have to :

1. Choose the type of your export between : **Tile**, **Mask**, **Thumbnail**, **Vector**, **Zone**, **Job**, **Dataset**. Then you have to choose the corresponding features, you can see the table below for more details.
2. Choose an Export Name
3. Click on "Submit"

**_Types Features :_**

|               |Projection       |Zoom             |Padding          |Job              |Dataset          |
| ------------- |: -------------: |: -------------: |: -------------: |: -------------: |: -------------: |
|Tile           |![O](/images/web_ui/1.png)|![O](/images/web_ui/1.png)|![O](/images/web_ui/1.png)|![1](/images/web_ui/2.png)|![O](/images/web_ui/1.png)|
|Dataset        |![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![O](/images/web_ui/1.png)|
|Job            |![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![1](/images/web_ui/2.png)|![0](/images/web_ui/1.png)|![1](/images/web_ui/2.png)|

Then, you have to return on Export List :

![Export View](/images/web_ui/export_view.png)

You can see the export list, with the Information column you can access to the main informations about an export and if you want to download this export you can click on ![More](/images/web_ui/datasets_more.png), and choose between :

- Copy GS url
- Copy HTTP url

With these URL you can access to the export (with a bucket).

##### Exported data for each type of exports

![Export Data](/images/web_ui/infos_exports.png)

For more details you can see the global structure of any export individually in the section "[Export Data Format](../parsing/parsing.md)".