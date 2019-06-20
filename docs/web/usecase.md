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
- Select one or more tag to apply. You can see the [Dataset Page](dataset.md "Dataset Page") for further details.
- Choose a tool in drawing feature(s). You can see the [Dataset Page](dataset.md "Dataset Page") for further details.

![Ground Truth Result](/images/web_ui/usecase1.png)

Then, you can draw all records as you want to create your ground truth.

The last step is the Validation.

If you want to rename your zone, you can see the [Zone Page](zone.md "Zone Page") for further details.

-----------------

### <span style="color:red">2. Validation</span>

-----------------

#### From Dataset List or Job list

This section enables you to change the status of a record. The edition of records or zones is not possible in this interface. You can access to this function in dataset list or job list.

Validation interface :
![Validation interface](/images/web_ui/validation_interface.png)

There is always one record selected. You can validate or invalidate the state of a record.The style of a valid record is green and for invalid records that's red. Some tools are given to help you for validation work :

1 - **Color** :
If you want to update the color of records (without state valid or invalid) for better view.

2 - **Selection footprint** :
To deactivate he selection footprint for better view.

3- **Shortcuts** :
To help you with keyboard shortcuts.

4 - **"Auto Next" option** :
Active : to jump automatically to the following record.
Deactive : to stay focus on the record after validation action.

5 - **Focus** :
If you move on the map and if you click on this button, the map focus automatically on the selected record.

6 - **Arrows** :
To jump to the following record if you deactive the "auto next" option or if you don't want to validate or invalidate the record now.


#### States Definitions

<span style="color:#800000">ADDED</span> - for "records" manuals<br/>
<span style="color:#800000">PREDICTED</span> - for "records" that created by processes<br/>
<span style="color:#800000">MODIFIED</span> - if you do modifications on the structure of your record <br/>
<span style="color:#800000">VERIFIED</span> - Validate, if your record has this state you can't change anything (add tag, delete tag, modify the structure of the record, delete the record...) in Edit section<br/>
<span style="color:#800000">INVALID</span> - Invalidate<br/>