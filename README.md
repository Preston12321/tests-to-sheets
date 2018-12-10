# How to Set Up the Project

## For the Professor:
1. Copy the code from this repository into your project directory and make whatever modifications are necessary for making the project class-worthy.
2. Visit the Google Cloud Platform Console at <https://console.cloud.google.com> and create a new empty project.
3. Add the Google Sheets API to the new project:
   1. From the navigation menu, select **APIs & Services**.
   2. Near the top of the page, click **ENABLE APIS & SERVICES** and search for the Google Sheets API.
   3. After selecting the Google Sheets API, click **ENABLE** to add it to your project.
4. Add OAuth2 credentials to your project so students can authorize access to their spreadsheets.
   1. After adding the Google Sheets API to your project, there should be a prompt saying you may need credentials. Click **CREATE CREDENTIALS**.
   2. Fill in the dropboxes selecting *Google Sheets API* for the API, *Other UI (e.g. Windows, CLI Tool)* for where you will be calling the API from, and *User data* for the kind of data you will be accessing.
   3. Click **What credentials do I need?**
   4. Give the credentials a name and click **Create OAuth client ID**.
   5. In *Product name shown to users*, type 'Sheets Uploader' or some other appropriate name and click **Continue**.
   6. Download the new credentials and save them in the activity directory. Make sure the file is called **client_id.json**.

## Uploader Usage:
```console
bash ./run_tests.sh 10 kj2l3k2h34l5kh3ljlkhk2gh34 R11:V75
```
Will run all tests 10 times and upload the results to the range R11:V75 of the google sheet with id kj2l3k2h34l5kh3ljlkhk2gh34.

### How to Find Spreadsheet ID and Range
1. Open the spreadsheet.
2. The URL should look something like this:
   ```
   https://docs.google.com/spreadsheets/d/1AoPWgr7YNP3p0PmFYO_qByrrSuKDcmd-ImII1BVMzIA/edit#gid=542348360
   ```
   We're interested in the part between the '/d/' and '/edit#...'
   In this example, the spreadsheet ID is
   ```
   1AoPWgr7YNP3p0PmFYO_qByrrSuKDcmd-ImII1BVMzIA
   ```
