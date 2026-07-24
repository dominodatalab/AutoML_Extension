# Manual Production Installation

Use these steps to manually install AutoML Studio as a Domino Extension.

## Prerequisites

Enable Extended Identity Propagation so the viewing user's identity is attached to requests they send when interacting with apps.

Set this Central Config value:

```text
com.cerebro.domino.apps.extendedIdentityPropagationToAppsEnabled=true
```

## Create the Extension Project

1. Log in as a SysAdmin Domino user.
2. Navigate to **Develop > Projects**.
3. Open the **Create Project** modal.
4. Create a private Git-backed project with these settings:
   - Project name: `AutoML_Extension`
   - Git hosting provider: GitHub
   - Input URL: `https://github.com/dominodatalab/AutoML_Extension.git`
   - Credentials: none required

The project must be named `AutoML_Extension`.

## Create the Domino Environment

1. Navigate to **Govern > Environments**.
2. Open the **Create Environment** modal.
3. Create an environment named `AutoML Domino Environment`.
4. Set **Base Environment / Image** to the required Domino environment base image from the repository `Dockerfile`: `python:3.10-slim-bullseye`.
5. Clear the **Automatically make compatible with Domino** checkbox.
6. Set visibility to **Globally Accessible**.
7. Click **Customize Environment**.
8. Paste the repository `Dockerfile` into the **Dockerfile Instructions** input.
9. Set the build argument to your chosen release tag or branch:

   ```dockerfile
   ARG EXTENSION_VERSION=<release tag or branch name>
   ```

10. Click **Build**.

## Create the Domino App

After the environment finishes building, create the app that will be published as the Domino Extension.

1. In the `AutoML_Extension` project, navigate to **Settings** and set the environment variable `DATABASE_URL=sqlite:////mnt/data/AutoML_Extension/automl.db`
2. Navigate to **Deployments > Apps & Agents**. Create an app with these settings:
   - Name: `AutoML`
   - Enable deep linking and query parameters: checked
   - Git reference type: Branch
   - Git reference: your chosen release branch
   - App file: `app_prod.sh`
   - Environment: `AutoML Domino Environment`
   - Environment revision: latest active revision
   - Hardware tier: choose a tier that matches expected usage
   - Autoscaling: off
   - Access & sharing visibility: Anyone in Domino
   - Allow App to act for viewers in Domino: checked

Autoscaling is not compatible with this extension.

Wait for the app to reach the **Running** state before continuing.

## Publish the Domino Extension

In the **Apps & Agents** table, open the action menu for the `AutoML` app in the `AutoML_Extension` project and select **Create Extension**. This publishes the extension for all users so they can access it from their project side navbar.
