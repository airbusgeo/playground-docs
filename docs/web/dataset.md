# Datasets

-----------------

**<span style="color:red">Dataset Definition : </span>** [![Link](/images/web_ui/link.png)](interface.md)

This section explains using Datasets. You can access to all of datasets already created. This interface enables you to edit results, [tag](interface.md) and create datasets. All of the datasets are described by a name, a description and a creation’s date. You can apply some actions on all of the datasets.

![Interface Datasets](/images/web_ui/datasets_interface.png)

## Create a Dataset

To create a dataset you have to click on this button :
![New Dataset](/images/web_ui/datasets_new.png)

Then, you have to enter the name and the description of the dataset.
If you want to work on this dataset you have to return on the first page with datasets list.

## Edit a Dataset

You can choose between **Object Detection** (![Object detection](/images/web_ui/datasets_objectdetection.png)) and **Change Detection** (![Change detection](/images/web_ui/datasets_changedetection.png)). The editing interface will be different. But actions are the same. You can choose between View, Edit or [Validate](usecase.md "Use Case").

#### <span style="color:red">1. Object Detection</span>

![Object detection Interface](/images/web_ui/dataset_objectdetection_interface.png)

In the Object Detection Interface, you can **switch** between all of the **[Zones](zone.md "Zones Page")** that are in the selected dataset.

##### 1.1. View

For more details on the dataset, you can see zones, images, tags, [records](interface.md)...

##### 1.2. Edit

This option enables you to modify the dataset. If you want to edit the dataset on a new location, **you have to select an image on this location**. You can access to some tools :

- <span style="color:#5472AE">**Drawing zone** :</span>

    - Draw a polygon : with several points
    - Draw a rectangle : with two points
    - Delete a zone
    - Select a zone : enables you to select a created zone

- <span style="color:#5472AE">**Drawing feature(s)** :</span>

<span style="color:#800000">**To Select one or more records :**</span>
![Select record](/images/web_ui/datasets_selectrecord.png)

If you select **more than one record** with different tags or with several tags : You can see the associated tags, click on "Remove tag(s)"
![Select record](/images/web_ui/dataset_selectrecord.png)

Then, you can see in orange the tags which are in the selection of records :
![Select record](/images/web_ui/dataset_selectrecord2.png)

<span style="color:#800000">**To Draw a record :**</span>

You have to select one or more tag(s):
![Draw record](/images/web_ui/datasets_drawrecord.png)

Or, you can select a record. The tag selected will be updated.

Then, you have to draw with tools :

|               |       Tools     |
| ------------- |: -------------: |
|![Tools](/images/web_ui/datasets_toolsrecord.png)| <p style='text-align: left;'>Draw Point<br/>Draw Rectangle 2 points<br/>Draw Rectangle 3 points<br/>Draw Polygon<br/>Draw Freehand<br/>Draw Directed Rectangle (back to front)<br/><br/><br/></p>|

<span style="color:#800000">**To Modify the tag of a record :**</span>

You have to select one record on the map (or more), click on : ![Modify detection](/images/web_ui/datasets_modifyrecord.png) and choose one or more tag(s). If you want to delete one of selected tag, click on this tag.

<span style="color:#800000">**To Duplicate one or more tag(s) :**</span>

You have to select just one tag ![Duplication1](/images/web_ui/datasets_duplication1.png)

Click on Duplication tool : ![Duplication2](/images/web_ui/datasets_duplication2.png)

A ghost of the selected record is under the mouse. Click to create the same record where the ghost is. If you want to create **multiple records**, you can click on the ghost several times.

![Duplication3](/images/web_ui/datasets_duplication3.png)
![Duplication5](/images/web_ui/datasets_duplicationmult2.png)

<!---->

Also while duplicating, you can **rotate** the ghost :

- To rotate left : Press ![Duplication6](/images/web_ui/datasets_duplicationq.png) (for qwerty) or ![Duplication7](/images/web_ui/datasets_duplicationa.png) (for azerty).
- To rotate right : Press ![Duplication8](/images/web_ui/datasets_duplicatione.png)

<span style="color:#800000">**To Merge :**</span>

You have to select more than one record. Then, click on this button : ![Duplication9](/images/web_ui/datasets_duplication4.png)

<span style="color:#800000">**To Modify the structure of a record :**</span>

Select only one record and move near an edge or a corner with your mouse. A point will appear on it.

![Structure1](/images/web_ui/datasets_struct.png)

Press ![Structure2](/images/web_ui/datasets_struct1.png) and click on :

- An **edge**, it will create new corners
- A **corner**, it will simply move the corner

And move the mouse while pressing the key and the button

![Structure3](/images/web_ui/datasets_struct2.png)![Structure4](/images/web_ui/datasets_struct3.png)

<span style="color:#800000">**To Translate one or more records :**</span>

Select **at least one** record and move cursor over one of them. The cursor turns into a hand. Press mouse button and drag the selection.

![Translate1](/images/web_ui/datasets_translate1.png)        ![Translate2](/images/web_ui/datasets_translate2.png)

<span style="color:#800000">**To Delete one or more records :**</span>

You have to select one or more records. And click on : ![Delete](/images/web_ui/datasets_deleterecord.png)

![Warning](/images/web_ui/warning.png) You can't to delete a record if his state is VERIFIED.

<span style="color:#800000">**To Activate grid :**</span>

Click on : ![Grid button](/images/web_ui/datasets_grid.png)

Then,

![Grid](/images/web_ui/datasets_grid2.png)

You can choose the color and spacing for grid lines.

<span style="color:#800000">**To Add a new tag :**</span>

Select this button : ![New Tag](/images/web_ui/datasets_newtag.png)

<span style="color:#800000">**To Add a comment on a record :**</span>

You have to select a record. Then you can add a comment with "Record Informations" section :

![Comment](/images/web_ui/dataset_comment.png)

You can see your comment when you put your mouse on the record.

#### <span style="color:red">2. Change Detection</span>

For object detection you have to choose just one image but for change detection you need two images. The interface is different : ![Change Detection Interface](/images/web_ui/datasets_changedetection_interface.png)

**"View"** and **["Validate"](usecase.md "Use Case")** function in the same way as for object detection. For **"Edit"** : You can modify just the first image. You can use same tools and same functions than object detection. You can access to a new button : “Cancel selection” (![Cancel Selection](/images/web_ui/datasets_changedetectionc.png)) if you want to change your selection.

#### <span style="color:red">3. More</span>

- Edit : if you want to change the name or the description of the dataset
- Clone
- Download as GeoJSON
- Move to... : this function enables you to move your dataset in another project (that have to be an existing project).

## Merge two Datasets

To merge two Datasets, you have to select just two datasets (no more) and click on ![Merge](/images/web_ui/datasets_merge.png)

## Delete one or more Dataset(s)

You have to select one or more datasets and click on ![Delete](/images/web_ui/datasets_delete.png)