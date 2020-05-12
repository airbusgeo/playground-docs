# Intelligence Playground Web Interface

-----------------

![Main Interface](/images/web_ui/launcher.png)

Some **definitions** to explain the main concepts :

- A **<span style="color:#ff9900">project</span>** gather datasets, users and processes.
- A **<span style="color:#ff9900">dataset</span>** gather zones, jobs and records. A Dataset is essentially a list of labelled zones that have been put under the same "namespace", usually because they are related to in either labelling type or geographical location.
- A **<span style="color:#ff9900">zone</span>** corresponds to an AOI (Area of Interest) associated to image(s).
<!--- A **<span style="color:#ff9900">POI</span>** corresponds to an AOI (Area of Interest) which is not associated to image(s).-->
- A **<span style="color:#ff9900">taxonomy</span>** classify records (is associated to a project) with some labels (tags).
- A **<span style="color:#ff9900">record</span>** may be a manually created object representing ground truth or the result of a job.
- A **<span style="color:#ff9900">tile</span>** represents an unique geographical location. Each tile is a 256x256 px jpg or png image associated with a specific satellite image at a specific geographical location.

You will find guidelines about using the Playground Web Interface. In fact, this interface enables you to:

- Run jobs on Intelligence imagery without using the Prediction API
- Monitor the advancement of jobs in real time
- View results and datasets while being directly connected to Intelligence Imagery
- Edit results, tags and create datasets
- Export datasets to a Google Storage bucket in order to train ML models
