
Playground provided access to its services throw REST APIs.

When available, Playground APIs are specialized implementations of the generic Airbus DS Geo APIs.
This allows partners to migrate from Playground to other Airbus DS systems with minimal efforts.

Intelligence Playground uses and provides the following APIs.

<!-- ### Geo Process API

* To be implemented by image processing algorithms
* Playground manages only the synchronous part of the Airbus DS API
* Playground manages kind of algorithms with templates

Playground defines the following templates for Geo Process API :

* tile-object-detection
* tile-change-detection -->

# Authentication API

To access Playground APIs, users have to be authenticated using the OAuth2 protocol.
As Playground OAuth2 is managed by Google, thus you have to authenticate using a Google account.

# Geo Processes Manager API

* Processing algorithms management and job execution
* Playground implementation extends the Airbus DS generic API with the concept of project
* Playground defines input templates for the king of managed jobs

Playground defines the following templates for Geo Process Manager API :

* object-detection
* change-detection

# Geo Data Manager API

API for management of Playground data :

* **Projects** gathers datasets, users and processes.
* **Datasets** gathers zones, jobs and records.
* **Zones** are geographical regions associated to image(s).
* **Records** may be a manually created object representing ground truth or the result of a processing.
