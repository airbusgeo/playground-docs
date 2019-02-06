# Use Case

-----------------

### <span style="color:red">1. Ground Truth Creation</span>

Steps to create a ground truth :

- [Create a dataset](dataset.md "Dataset Page")
- In the Datasets list find your dataset and click on Edit

![Edit Dataset](/images/web_ui/usecase_dataset_edit.png)

- Select a Location
- Select an Image

![Interface Datasets](/images/web_ui/usecase_dataset.png)

- Draw a zone with drawing zone tools. You can see the [Dataset Page](dataset.md "Dataset Page") for further details.
- Create one or more tags (Tags settings), you can choose the colors of them, for that you have to click on the existings color and choose the new.

![Tags colors](/images/web_ui/usecase_tagscolors.png)

- Select one or more tag to apply
- Choose a tool in drawing feature(s). You can see the [Dataset Page](dataset.md "Dataset Page") for further details.

![Ground Truth Result](/images/web_ui/usecase1.png)

Then, you can draw all records as you want to create your ground truth.

The last step is the Validation.

If you want to rename your zone, you can see the [Zone Page](zone.md "Zone Page") for further details.

-----------------

### <span style="color:red">2. Validation</span>

-----------------

#### From Dataset List or Job list

This section enables you to change the status of a zone or a record. You can draw zones or records in this section too. You can access to this function in dataset list or job list.

![Validate](/images/web_ui/datasets_validate1.png)

<p style='text-align: justify;'><span style="color:#5472AE">Zone setting</span> - You can change the statusof the selected zone and more precisely you can choose between Pending, Labellized or Reserved :</p>

![Validate Zone Settings](/images/web_ui/datasets_validate3.png)

<p style='text-align: justify;'><span style="color:#5472AE">Records State</span> - You can select a record and see his state (added, predicted, modified, verified, invalid...). Then, you can change this state between verified (Validate button) and invalid (Invalidate button) :</p>

![Validate Records State](/images/web_ui/datasets_validate2.png)

#### States Definitions

<span style="color:#800000">ADDED</span> - for "records" manuals<br/>
<span style="color:#800000">PREDICTED</span> - for "records" that created by processes<br/>
<span style="color:#800000">MODIFIED</span> - if you do modifications on the structure of your record <br/>
<span style="color:#800000">VERIFIED</span> - Validate, if your record has this state you can't change anything (add tag, delete tag, modify the structure of the record, delete the record...) in Edit section<br/>
<span style="color:#800000">INVALID</span> - Invalidate<br/>

![Warning](/images/web_ui/warning.png)The state change if you merge two records with different state.