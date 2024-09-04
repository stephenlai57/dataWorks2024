# Welcome to ExxonMobil DataWorks Challenge 2024

## About the challenge
Topic: Machine Learning for High Fidelity Physics Based Model Reduction

Submission: 21 September 2024 (Saturday) at 11.00am (GMT +8)

## Folders & files
1. dataset 
```
    |- test                                      = Dataset used to test robustness of the model 
        |- Reservoir{number}_state.csv           = The reservoir's state 
    |- training                                  = Dataset used for the training of machine learning model 
        |- Reservoir{number}                     = The reservoir 
            |- state.csv                         = The reservoir's state 
            |- production.csv                    = The reservoir's production 
    |- validation                                = Dataset used to evaluate the machine learning model performance 
        |- Reservoir{number}                     = The reservoir 
            |- state.csv                         = The reservoir's state 
            |- production.csv                    = The reservoir's production 
    |- Template_Reservoir{Number}_production.csv = The template for reservoir's production 
```
2. submissions 
```
    |- docs                                          = All related documents
        |- {team_name}_video.mp4                     = Team 7 min video on the solution
        |- {team_name}_documentation.pdf             = Team documentation
        |- appendix                                  = Location for all visualization, team photo, teamwork photo (in JPEG/PNG, PPT/Docs)
    |- workspace                                     = Students workspace (free to do anything)
        |- source_code                               = All related source code
        |- models                                    = Machine learning models (.pkl, .keras, .tf, .hd5, etc)
        |- external_files                            = External files (ie. tableau file/power BI file/data source/etcs) 
    |- {team_name}_test_results                      = Reservoir's production prediction results based on the test dataset 
        |- Reservoir{Number}_production.csv          = The reservoir's production 
```

# Submission:
1. 7 minutes video (.mp4) about your findings and/or modeling in `submissions/docs/{team_name}_video.mp4`.
2. Documentation (.pdf) on the following in `submissions/docs/{team_name}_documentation.pdf`.
    - Setup instruction
    - Development process
    - Findings/visualization
    - Special instruction needed to run your project
3. Source codes/machine learning models/files that is used for development, analytics and testing for this challenge in `submissions/workspace`.
4. By using the inputs in `dataset/test`, place the reservoir production prediction result in `submissions/{team_name}_test_results` that follows the naming convention `Reservoir{Number}_production.csv` that utilizes the template of `Template_Reservoir{Number}_production.csv`.
5. Please share your team photo and photos of your team working on the use case in `docs/appendix`.
6. Please zip both the dataset and submissions, name it as `{team_name}.zip` and team lead are required to upload to the ShareFile

# Note/Disclaimer: 
1. The datasets and starter kit are solely for DATAWORKS Challenge 2024 use case only.
2. Teams can focus on either data exploration and/or machine learning modeling using their own tools.
3. Teams are required to clean their own code and ensure readability before submission.
4. Do not clear your workbook results in your `workspace`. 
5. For PowerBI, please use the 2.130.754.0 64-bit (June 2024) and below.
6. For any visualization, please export it to `docs/appendix`.
