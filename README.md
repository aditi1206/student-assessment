# Students Assessment Project
This project automate providing any number of Students Progress files
and receiving the desired results in an output file

```markdown
Note:
This project includes multiple Python libraries are used to
demonstrate usage and variants of Python coding practices.
```
# Architecture
The entire projects Architecture can be followed with the comments in "execute()" function.

```markdown
students_assessments.automated_class_report.execute
```


# Coding Practices and PEP8 Conventions Used:
* Modular Design
* Handling edge case scenarios
* Cleaner and Concise code
* PEP8 Standards are followed though out the project
* Exception Handling
* Project Structure
* Modules and package Creation
* Attention to Detail
* Scalable Application

# Time Constraints

* Convert functions to classes where necessary
* Spent more time on Architecture and make code efficient

## Improvements In the Future
Can be a full scale Django/Flask/Falcon Application with features like
* REST API
* DATABASE and data models for the Data Frame Created with Pandas
* User interface with Dashboard(can be any of the Javascript Libraries)

## **Dependencies**
#### Install python 3 Based on Operating System

#### Install/Upgrade `pip`
```bash/cmd/powershell/IDE
pip3 install --upgrade pip
pip3 install --upgrade setuptools
```

#### Install python testing tools
```bash/cmd/powershell/IDE
pip3 install virtualenv
```

### Create Virtual Env
You can create a virtual environment if you would like to


### Execution
The Files Path for the Input CSV Files need to be in the Root of the Project,
you can specify an Environmental Variable for the path "FILES_PATH"

```markdown
python students_assessments/run.py
```




# OUTPUT
                  SCHOOL REPORT



                ClassA
Total number of students within the class: 10
The number of students used to calculate the class average: 9
The names of students who were discarded from consideration: ['Edith Adkins']
Class Average: 79.4
Additional Data:




=======================================================================================

                ClassB
Total number of students within the class: 10
The number of students used to calculate the class average: 10
The names of students who were discarded from consideration: []
Class Average: 80.2
Additional Data:


*** 
ClassB Highest Class Average compared to others 
***



=======================================================================================

                ClassC
Total number of students within the class: 10
The number of students used to calculate the class average: 10
The names of students who were discarded from consideration: []
Class Average: 80.1
Additional Data:




=======================================================================================


   ADDITIONAL STATS
All Classes Average: 79.9
