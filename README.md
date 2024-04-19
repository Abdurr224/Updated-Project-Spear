# Updated-Project-Spear

This is an update to the Orignal Project Spear. It includes true machine learning and role based datasets to increase effectivness.


 Role(program):
    - Import role dataset 
    - From the staff name given from input, get the relevant role directory
    - Based on role:
        a. Run Accountant Engine
        b. Run Generic Engine

Accountant Engine(program):
    - Imports accountant dataset to process
    - If detection is true:
        a. Write contents to an external file.
    - If no detection:
        a. Its clean, End
        b. Optional: Generic Engine(program) to get a second scan

Generic Engine(program):
    - Imports nonspecialised/ generic dataset to process
    - If detection is true:
        a. Write contents to an external file.





![Spear Flow](https://github.com/Abdurr224/Updated-Project-Spear/assets/166424757/0327753f-0e42-44e1-a606-07c262f51716)





In this scenario, the system is specifically tailored to address risks related to the exposure of data in a job role, which in this case is financial data from accountants. It operates with specialised dataset containing around 200 entries and 5000 entries for the generic dataset. Despite the relatively small size of the specialised dataset, they are of high quality. They are crafted to simulate real-world scenarios by impersonating various entities that accountants commonly interact with, including suppliers, banks, customers, investors, potential investors, and tax authorities. Moreover, they incorporate social engineering tactics from phishing attacks to enhance their effectiveness.
Having a two datasets allows one being the generic dataset, act as default dataset relvent to all roles whilst, those with high data exposure will have unique and specialised datasets for extra precaution.



