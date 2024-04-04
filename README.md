# CS432
# Group Name : QueryCrafters
# Dispensary Management System

## Installation

Installation requirements to run this project:

```bash
  python3 -m venv myenv1
```
```bash
  pip install flask
```
```bash
  pip install pymysql
```

    
## Modules used

To run this project, the following modules need to be added

`from flask import Flask, render_template, jsonify, request, redirect, url_for`
`import pymysql`
`import config`


Note: MySQL Server(workbench) should be installed on the PC. Dump the “dispensary1.sql” in the same directory.



#### Steps to Launch the website:


- Move all the files in one folder. Open folder as code in VS Code.
- Create virtual environment "myenv" using command “python -m venv myenv1”
- Activate environment using command “myenv1/Scripts/activate”
- Install required libraries (mentioned above)
- Run the “app.py” file using command “python app.py”
- Click on the URL 
