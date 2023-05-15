# Databricks notebook source
import subprocess
subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

# COMMAND ----------

os.chdir("/Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test")
!git log

# COMMAND ----------

import os
import subprocess

os.chdir("/path/to/repository")
commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()


# COMMAND ----------

git ls-remote https://github.com/KrishnachaithanyaThummala


# COMMAND ----------

import subprocess
def is_git_repository():
    try:
        subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])
        return True
    except subprocess.CalledProcessError:
        return False
def get_git_commit_id():
    if not is_git_repository():
        return None
    try:
        commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return commit_id
    except subprocess.CalledProcessError:
        return None
# Get the Git commit ID
commit_id = get_git_commit_id()
# Print the commit ID
if commit_id:
    print("Git commit ID:", commit_id)
else:
    print("Unable to retrieve Git commit ID.")

# COMMAND ----------

import os
import subprocess

os.chdir("/Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test")
commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()


# COMMAND ----------

# MAGIC %sh
# MAGIC pwd

# COMMAND ----------

import subprocess
def is_git_repository():
    try:
        output = subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree']).strip().decode('utf-8')
        return output == 'true'
    except subprocess.CalledProcessError:
        return False
# Check if the current directory is inside a Git repository
if is_git_repository():
    print("Current directory is inside a Git repository")
else:
    print("Current directory is not inside a Git repository")

# COMMAND ----------

import os
import subprocess

git_dir = "/Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test"
os.chdir(git_dir)

commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test
# MAGIC git fsck

# COMMAND ----------

# MAGIC %sh
# MAGIC export GIT_DISCOVERY_ACROSS_FILESYSTEM=1
# MAGIC cd /Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test
# MAGIC git fsck

# COMMAND ----------

# MAGIC %sh
# MAGIC git init

# COMMAND ----------

import requests
admin_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
databricks_instance = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
headers = {"Authorization": f"Bearer dapifc3d096b06e3a1a11d355369e3e218ea"}
requests.get(databricks_instance + "/api/2.0/repos/441901742310101", headers=headers)

# COMMAND ----------

# MAGIC %sh
# MAGIC curl --netrc --request GET \
# MAGIC   https://adb-6491134404419862.2.azuredatabricks.net/api/2.0/repos/441901742310101 \
# MAGIC   --header "Authorization": f"Bearer dapifc3d096b06e3a1a11d355369e3e218ea" \

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -n \
# MAGIC -X GET -H 'Content-Type: application/json' \
# MAGIC -H = 'Authorization': f'Bearer dapifc3d096b06e3a1a11d355369e3e218ea' \
# MAGIC -d '{ "<repo-id>": 441901742310101 }' https://adb-6491134404419862.2.azuredatabricks.net/api/2.0/repos/repo_id \

# COMMAND ----------

import requests
admin_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
databricks_instance = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()

headers = {"Authorization": f"Bearer {admin_token}"}

requests.get(databricks_instance + "/api/2.0/repos/604119180", headers=headers).json()

# COMMAND ----------

# MAGIC %sh
# MAGIC TOKEN="dapifc3d096b06e3a1a11d355369e3e218ea"
# MAGIC WORKSPACE_URL="https://adb-6491134404419862.2.azuredatabricks.net"
# MAGIC NOTEBOOK_PATH="/Users/<your-username>/<path-to-notebook>"
# MAGIC NOTEBOOK_PATH="/Users/krishnachaithanya.thummala@databricks.com/Workspace/Repos/krishnachaithanya.thummala@databricks.com/databricks-test/git_Problem"
# MAGIC curl -H  "Authorization: Bearer $TOKEN" "$WORKSPACE_URL/api/2.0/workspace/export" \
# MAGIC   --data-urlencode "path=$NOTEBOOK_PATH" \
# MAGIC   --data "format=SOURCE" | grep 'CommitId'
# MAGIC   

# COMMAND ----------

# MAGIC %sh
# MAGIC ls
# MAGIC pwd

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -s -H "Accept: application/vnd.github.VERSION.sha" \
# MAGIC   https://api.github.com/repos/KrishnachaithanyaThummala/databricks-test/commits/main

# COMMAND ----------

# MAGIC %sh
# MAGIC curl --location 'https://adb-6491134404419862.2.azuredatabricks.net/api/2.0/repos/441901742310100' \
# MAGIC --header 'Authorization: Bearer dapifc3d096b06e3a1a11d355369e3e218ea'

# COMMAND ----------

# MAGIC %sh
# MAGIC curl --location 'https://adb-6491134404419862.2.azuredatabricks.net/api/2.0/repos' \
# MAGIC --header 'Authorization: Bearer dapifc3d096b06e3a1a11d355369e3e218ea'

# COMMAND ----------


