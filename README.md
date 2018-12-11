# Setting Up the Project (For the Professor):
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

## Dependencies
The python script requires the Google Sheets API and OAuth2 client libraries.
```console
$ pip install --upgrade google-api-python-client oauth2client
```

# Uploader Usage:
```console
$ bash ./run_tests.sh 10 kj2l3k2h34l5kh3ljlkhk2gh34 R11:V75
```
Will run all tests 10 times and upload the results to the range R11:V75 of the google sheet with id kj2l3k2h34l5kh3ljlkhk2gh34.

## How to Find Spreadsheet ID and Range
1. Open the spreadsheet.
2. The URL should look something like this:
   ```
   https://docs.google.com/spreadsheets/d/1AoPWfr7YNP3p0PmFYO_qByrrSuKDcmd-ImII1BVMzIA/edit#gid=542348360
   ```
   We're interested in the part between the '/d/' and '/edit#...'
   In this example, the spreadsheet ID is
   ```
   1AoPWfr7YNP3p0PmFYO_qByrrSuKDcmd-ImII1BVMzIA
   ```
3. Find the table in the spreadsheet where you want to insert your results. The range you need will be in the format AA:BB where AA represents the cell name of the top left cell of the table and BB represents the cell name of the bottom right cell of the table. So a valid range would be something like: *R11:75*
   
   **Do not include the headers or the final Median row in the range. The range should begin and end in cells that will actually hold the values of your results!**

## How to Allow Access to Spreadsheet
1. Run the test script as specified.
2. When the script prompts, copy the URL specified in the terminal and open the URL in the browser on your local machine. **(Not the remote server, because there is no way to open a GUI browser remotely)**
3. Sign in to the account that holds your results spreadsheet and allow access to the script.
4. Close the page after you are done and return to your terminal. The script should now complete and upload the results where you specified. You should now see the values in your spreadsheet.

# What I Changed
To put it simply, in order to make uploading all the values easier, I removed all print statements from the original C files except for the result times themselves, and added code to run_tests.sh to write those to an intermediate file, 'values.txt', which is then fed to the python upload script.

## How it Works
The intermediate file, 'values.txt', will contain a line for every problem size (each column in the spreadsheet) and space-separated values on each line. The python file is designed to be unnecessary to open, so the student would only ever need to modify run_tests.sh, just like the activity was before. The python file uses the python oauth2client library and Google Sheets API to request access from the student and upload the results.
