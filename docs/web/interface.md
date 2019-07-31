# Intelligence Playground Web Interface

-----------------
Interface :
![Main Interface](/images/web_ui/interface.png)

Some **definitions** to explain the main concepts :

- A **<span style="color:red">project</span>** [![Link](/images/web_ui/link.png)](project.md) gather datasets, users and processes.
- A **<span style="color:red">dataset</span>**  [![Link](/images/web_ui/link.png)](dataset.md) gather zones, jobs and records.  A Dataset is essentially a list of labelled zones that have been put under the same "namespace", usually because they are related to in either labelling type or geographical location.
- A **<span style="color:red">zone</span>** [![Link](/images/web_ui/link.png)](zone.md) corresponds to an AOI (Area of Interest) associated to image(s).
- A **<span style="color:red">taxonomy</span>** classify records (is associated to a project).
- A **<span style="color:red">record</span>** may be a manually created object representing ground truth or the result of a job.
- A **<span style="color:red">tile</span>** represents an unique geographical location. Each tile is a 256x256 px jpg or png image associated with a specific satellite image at a specific geographical location.

You will find guidelines about using the Playground Web Interface. In fact, this interface enables you to:

- Switch between projects
- Run jobs on Intelligence imagery without using the Prediction API
- Monitor the advancement of jobs in real time
- View results and datasets while being directly connected to Intelligence Imagery
- Edit results, tags and create datasets
- Export datasets to a Google Storage bucket in order to train ML models
