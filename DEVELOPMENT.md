# TODO

# feature changes

## big problems
- make training job stateless so that doesn't depend on shared sqlitedb OR programmatically share the dataset and then mount it in the user's project.....idk
- make training job stateless so no env vars required in target project

## solvable problems
- DOMINO_TRAINING_HARDWARE_TIER_NAME, DOMINO_EDA_HARDWARE_TIER_NAME not used

## other
- we should say that the job name must be unique
- it is hard to run this locally because it depends on domino auth and assets
- how to deal with transient errors in training jobs, which resulted in the job failing? rerun jobs don't appear in extension
- how is local development? requirements would get out of sync with the environment, maybe we should download the 
requirements from the github repo when building the Dockerfile
- i think job config should show what environment and hwt will be used for the job, also project target and user
- information in the extension-design.md makes assumptions about the file paths used, and should probably be generalized

# notes

## big problems
- we use a sqlitedb shared dataset in order to share state between the extension and the target project,
which requires the dataset to be shared with the target project/user and it is not possible to share with all users automatically
- the user must set env vars in their project in order to use the extension in it
- users won't know at first (if ever?) that their datasets are being saved to a shared dataset that everyone who uses
the extension has access to. The user data should probably be PRIVATE/RETAIN USER SPECIFIED PERMISSIONS

## solvable problems
- apt is still available and usable in the app
- the data uploaded to the extension grows endlessly

## other
- got this warning from autogluon in my training job:  WARNING:app.core.trainers.tabular:Could not compute feature importance: Feature importance `dataset` cannot be None if `feature_stage=='original'`. A test dataset must be specified.
- there is an active domino jobs setting...probably useful for the in memory "jobs", for domino jobs though?
- test advanced configuration in job launching
- job creation in sqlite db can fail and result in inconsistent state between domino and local db, job_service.py,
need to verify that test_job_service covers this for create_job_with_context
- refactor remap_shared_path away? we probably want paths to be looked up deterministically to avoid bugs where the wrong
path is used and something is written to or deleted
