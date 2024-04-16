# CS432
# Group Name : QueryCrafters
# Dispensary Management System

### Saurabh Kumar Sah 21110188
### Shreya Patel 21110155
### Riya Jain 21110178
### Twinkle Devda 21110228
### Ishika Raj 21110081
### Saumya Jaiswal 21110186
### Darsh Dalal 21110049
### Het Trivedi 21110226


## Installation

Installation requirements to run this project:

```bash
  pip install flask
```
```bash
  pip install pymysql
```
```bash
  pip install config
```
```bash
  pip install authlib
```
```bash
  pip install requests
```
```bash
  pip install re
```

## Modules used

To run this project, the following modules need to be added

from flask import Flask, render_template, jsonify, request, redirect, url_for`
import pymysql`
import config`
from flask import Flask, redirect, url_for, session, request`
from authlib.integrations.flask_client import OAuth`
import re`

Note: MySQL Server(workbench) should be installed on the PC. Dump the “dispensary1.sql” in the same directory.



#### Steps to Launch the website:


- Move all the files in one folder. Open folder as code in VS Code.
- Create virtual environment "myenv1" using command:
```bash
  python -m venv myenv1
```

- Activate environment using command:
  
```bash
  myenv1/Scripts/activate
```

- Incase the previous command does not work, use this command before the previous command:
```bash
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- Install required libraries (mentioned above)
- Insert the mySQL credentials(root,host,password,database) in config.py file
- Run the “app.py” file using command:
  
```bash
  python app.py
```

- Click on the URL 
