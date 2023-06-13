# polaris-export-defects-to-azure-boards

**Disclaimer**

This code is provided as a proof of concept and is not intended for production use. It serves as a demonstration of how to integrate Polaris with Azure DevOps and create issues in Azure Boards. Please note the following:
1. Limited Functionality: The code provided may not cover all possible scenarios or handle every edge case. It is meant to showcase a specific functionality and may not be comprehensive.
2. Security Considerations: This proof of concept code may not have undergone a thorough security review. It is essential to assess and enhance the security aspects of the code before deploying it in a production environment.
3. Performance and Scalability: The code has not been optimized for performance or scalability. It is advised to conduct proper testing and optimization if you plan to use similar functionality in a production setting.
4. Compatibility: The code was developed and tested under specific conditions and dependencies. It may not work as expected in different environments or with different versions of the underlying technologies.
5. No Liability: The author(s) of this code and its associated documentation cannot be held liable for any damages or issues arising from the use of this code. Use it at your own risk and exercise due diligence when implementing it in your own projects.
Remember to thoroughly review and modify the code to meet your specific requirements, security standards, and best practices before considering it for production use.


**Functionality**

The executable gets Polaris defects from a project of an app for a given severity level. Then creates issues on Azure Boards for the given project name based on the defects exported from Polaris.   
It supports business scenarios as follows
**Create** issues in Azure Boards from the latest scan results of any project in Polaris based on the severity of the vulnerability   

To run the executable, you may follow the steps below for reference.
1. Navigate to the directory where the executable and config files are stored.
2. Open the config.py file and populate the follwoing variables with appropriate values
    - polaris_url
    - polaris_access_token
    - azure_url
    - azure_organization_name
    - azure_access_token
3. Run the python executable with the following parameters
    - polaris app name
    - polaris project name
    - severity level of the issues to be exported into Azure Boards. accepted values are [low, medium, high, critical]
    - Azure DevOps Project name
4. Run the executable from a terminal. example execution commad:
    - python3 polaris-export-defects-to-azure-boards.py <polaris-app name> <polaris-project name> <severity> <ADOS-Project name>

Test Plan:  

**(1)** Scan a project with previously unknown defects. Follow the steps above, you should see Jira TODO tickets for 
those new defects.  
**(2)** Mark some defects with False Positive / Intentional, then the cov-export-defects-to-jira will automatically 
delete the tickets of those defects in Jira.  
**(3)** Fix some defects. Follow the step above, you should be the status for the tickets of those defects are modified
to "Done" status.  
**(4)** Modify the "--impact" parameter with any combination of high, medium, low, and audit. You should see the defects
exported to Jira are controlled. The customer may focus the defects with high and medium impacts first and the low 
and audit subsequently.

Troubleshooting:  
N.A.  

Updates:

22nd June 2021: Exporting defects to Jira Cloud is enabled.
30th Sept 2021: Add test plan.
