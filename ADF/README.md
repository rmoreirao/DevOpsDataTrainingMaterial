<h1>LAB 1</h1> 

*Goals*

Deploying Azure Data Factory resources, libraries and notebooks with multi-stage YAML pipelines in Pipelines.

1. Create your own branch from master and make a GIT clone
2. Deploy your own resources (Keyvault, Data Factory, SQL Database, Storage account). To save time, only deploy one environment (for example, dev) 
3. Build Data Factory artifacts
4. Publish artifacts to Data Factory

<h2>Goal 1 - steps: </h2>

1. Navitage to Repos.
2. On the right blade, click on the branch name (master) with a dropdown menu.
3. Click on '+ New Branch'
4. Create a new branch name based on your group name, for example, "dev_group1". Make sure that "based on" has "master" selected.
5. Once the new branch has been created, click on "Clone" in the top right corner.
6. If you're using VSCode, click on the "Clone in VSCode" button. If you're using another IDE, follow the steps to clone the branch for that IDE.
7. Do the changes for following steps in your own branch.  

<h2>Pushing changes to Git</h2>

1. Save the files you've been working on.
2. In Visual Studio Code, click on  "Source control" in the left menu
3. You should see all the changed files in the "Changes" dropdown.
4. When you hover over the files, a "+" icon appears next to it. Clicking on it will move the file to the "staging" area. Click on all the changed files to the staging area.
5. From the top, write a commit message. Try to be as descriptive as possible on what you changed!
6. Next to the blue "Commit button", open the dropdown menu.
7. Click on "Commit & Push"

<h2>Goal 2 - steps:</h2>

``Make sure you're starting to work in your own teams branch``

1. Open ``pipeline.yaml`` from the ADF folder.
2. Change the values in the places marked with comments with corresponding values for your group. 
3. Although there are not many places to change, take a look at all the jobs, tasks and steps that the pipeline has defined in it. There are a lot of comments explaining the different steps to complete the whole pipeline.
4. Once you've read through and changed the values in the yaml, commit and push the changes in to your branch.
5. Go back to Azure DevOps GUI.
6. Click on ``Pipelines`` and also the subheading ``Pipelines``.
7. Click on "New Pipeline" on the top right.
- Choose "Azure Repos" as the code location
- Choose the "DataPrimeDevOps" repository
- Select "Existing Azure Pipelines YAML file"
- From the popup, select your branch and your own ``pipeline.yaml`` file from the /ADF/ folder. Click continue. 
- Click "run" from the top right corner.
8. Let the instructor know you have clicked "run", as the pipeline needs admin permissions to run.
9. Now you're resources are deploying, great! 

<h3>Extras - if you want to find out how to do them on your own:</h3>

1. Create a trigger for the pipeline, so that it runs automatically every time your branch has a change.

<h2>Notes:</h2>

- Do not modify the python libraries, files or notebooks for this exercise.
- Do not modify anything in databricks.json 
- Remember, that YAML is a real stickler for the syntax!