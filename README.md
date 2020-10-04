# Corporate Social Media by 'While true: hack'
## Hackathon by NVIDIA and Skoltech
This repository shows how projects are recommended to employees on the website.
### GUI
GUI of the website can be found here: <a href="https://dpereponov99.wixsite.com/nvidia">link</a>
### Projects
In `employees.ipynb` we generate a database of
projects. Each project requires 3 specific skills.
### Recommendations
We recommend to an employee the projects that require his skills.
More formally, we use *intersection-over-union (IoU)* to rank
projects for each employee. IoU of employee's skills and
project's skills equals the number of common skills
divided by the number of skills in the union. **Example:**<br />

*employee's skills = {Storytelling, Communication}*<br />
*project's skills = {Communication, Independence}*<br />
*intersection(employee's skills, project's skills) = {Communication}*<br />
*union(employee's skills, project's skills) = {Storytelling, Communication, Independence}*<br />
*IoU(employee's skills, project's skills) = |intersection| / |union| = 1 / 3*<br />

IoU can have values from 0 (no common skills) up to 1 (required skills coincide with employee's skills)

### Usage
* Go to <a href="https://evening-river-41641.herokuapp.com">website</a>
(**disclaimer:** this site is ugly, we use it to show that we can deploy a dynamic website. To see the GUI, go to <a href="https://dpereponov99.wixsite.com/nvidia">link</a>)
* Insert ***any*** full name from `Employees.csv`. Examples: Piper Dingledine, Dennis Cardenas, William Mooney, Ashley Rifkin, Lisa Yruegas
* Hit `submit` and you will see persons' skills and recommended projects with the highes IoU.

### Comments
The code that builds the websites is in `login.py`. HTML code is in `templates` folder.
