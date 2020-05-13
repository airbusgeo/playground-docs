# Datasets

-----------------

**<span style="color:#ff9900">Dataset Definition : </span>** [![Link](/images/web_ui/link.png)](interface.md)

This section explains using Datasets. You can access to all of datasets already created. This interface enables you to edit results, [tag](interface.md) and create datasets. You can apply some actions on all of the datasets.

![Interface Datasets](/images/web_ui/datasets_interface.png)

1. Enables you to **<span style="color:#ff9900">create</span>** a new dataset. When your dataset is created, if you want to work on this dataset you have to return on the first page with the list of datasets.
2. Enables you to **<span style="color:#ff9900">merge</span>** two datasets (datas of the second dataset are added to the first dataset). You have to select just two datasets (no more).
3. Enables you to **<span style="color:#ff9900">delete</span>** the selected dataset(s)
4. **<span style="color:#ff9900">Option</span>** list for each datasets :
    * **Object Detection** (![Object detection](/images/web_ui/datasets_objectdetection.png)) : View or Edit
    * **Change Detection** (![Change detection](/images/web_ui/datasets_changedetection.png)) : View or edit
    * **Validation**
    * **More** :
        * Edit : if you want to change the name or the description of the dataset
        * Clone : to duplicate the selected dataset with all data (records, zones, ...)
        * Download as GeoJSON
        * Move to... : this function enables you to move your dataset in another project (that have to be an existing project).

-----------------

## <span style="color:#2980b9">Edit (and view) option</span>

For these options you can choose between **Object Detection** (![Object detection](/images/web_ui/datasets_objectdetection.png)) or **Change Detection** (![Change detection](/images/web_ui/datasets_changedetection.png)). The interface is different, but actions are the same.

This documentation about dataset edition is based on Object Detection interface. This interface enables you to update or create records on existing zones.

![Object detection Interface](/images/web_ui/dataset_objectdetection_interface.png)

In the Object Detection Interface, you can **switch** between all of the **[Zones](zone.md "Zones Page")** that are in the selected dataset.

##### <span style="color:#2980b9">1. To select one or more record(s)</span>

![Select record](/images/web_ui/datasets_selectrecord.png)

##### <span style="color:#2980b9">2. To Create a new record</span>

![Select record](/images/web_ui/dataset_selectrecord.png)

<p style='text-align: justify;'>To draw a record you have to select one or more tag(s). For that you need to open the "Tags" section.</p>

<!--![Draw record](/images/web_ui/datasets_drawrecord.png)-->

<p style='text-align: justify;'>You can see the taxonomy associated, if you want to see all of the tags of this taxonomy you can click on the name of your taxonomy (here it is "Airbus Taxonomy"). You can change de visibility of the tags with the checks.</p>

<p style='text-align: justify;'>To select a tag for the creation record you have to click on "Select tag(s)". That will open a pop up to select tag(s). Or, you can select an existing record. The tag selected will be updated. If you want to delete one of selected tag, click on this tag.</p> 

Then, you have to draw with tools :

|               |       Tools     |
| ------------- |: -------------: |
|![Tools](/images/web_ui/datasets_toolsrecord.png)| <p style='text-align: left;'>Draw Point<br/>Draw Rectangle 2 points<br/>Draw Rectangle 3 points<br/>Draw Polygon<br/>Draw Freehand<br/>Draw Directed Rectangle (back to front)<br/><br/><br/></p>|

##### <span style="color:#2980b9">3. To Duplicate one or more record(s)</span>

You have to select just one tag and click on Duplication tool : ![Duplication2](/images/web_ui/datasets_duplication2.png)

A ghost of the selected record is under the mouse. Click to create the same record where the ghost is. If you want to create **multiple records**, you can click on the ghost several times.

![Duplication3](/images/web_ui/datasets_duplication3.png)
![Duplication5](/images/web_ui/datasets_duplicationmult2.png)

Also while duplicating, you can **rotate** the ghost :

- To rotate left : Press ![Duplication6](/images/web_ui/datasets_duplicationq.png) (for qwerty) or ![Duplication7](/images/web_ui/datasets_duplicationa.png) (for azerty).
- To rotate right : Press ![Duplication8](/images/web_ui/datasets_duplicatione.png)

##### <span style="color:#2980b9">4. To Update an existing record</span>

**4.1. To Merge multiple records :**</span> You have to select more than one record. Then, click on this button : ![Duplication9](/images/web_ui/datasets_duplication4.png)

**4.2. To Modify the structure of a record :** Select only one record and move near an edge or a corner with your mouse. A point will appear on it.

![Structure1](/images/web_ui/datasets_struct.png)

Press ![Structure2](/images/web_ui/datasets_struct1.png) and click on :

- An **edge**, it will create new corners
- A **corner**, it will simply move the corner

And move the mouse while pressing the key and the button

![Structure3](/images/web_ui/datasets_struct2.png)![Structure4](/images/web_ui/datasets_struct3.png)

**4.3. To Translate one or more records :**

Select **at least one** record and move cursor over one of them. The cursor turns into a hand. Press mouse button and drag the selection.

![Translate1](/images/web_ui/datasets_translate1.png)        ![Translate2](/images/web_ui/datasets_translate2.png)

**4.4. To Delete one or more records :** You have to select one or more records. And click on : ![Delete](/images/web_ui/datasets_deleterecord.png)

![Warning](/images/web_ui/warning.png) You can't to delete a record if his state is VERIFIED.

**4.5. To Update tags for the selected record :**</span>

<p style='text-align: justify;'>You can select one or more record(s). Then you can see the tags of the selected record in creation section. If you want to add modifications, you can click on "Manage tag(s)". This button open a pop-up where you can add or remove tag(s) with checks.</p>
![update tag](/images/web_ui/dataset_tag_setting.png)

**4.6. To Add a comment on a record :** You have to select a record. Then you can add a comment with "Record Informations" section :

![Comment](/images/web_ui/dataset_comment.png)

You can see your comment when you put your mouse on the record.

-----------------

The difference between object detection and **<span style="color:#ff9900">change detection</span>** interface for the edition : you can modify just the first image.

-----------------

## <span style="color:#2980b9">Validation option</span>

You can see the [Validation](usecase.md) page for further details. 