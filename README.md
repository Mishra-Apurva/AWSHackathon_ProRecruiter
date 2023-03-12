# ProRecruiter

### Problem Identified
HR Recruiters juggle similar emails from numerous applicants. Switching between these different types of emails has productivity costs — a recruiter may add a new applicant to database, rearrange an interview, and cycle back to the previous task. 
Emails inform upcoming tasks to-do, but existing email filters do not classify based on specific content categories unless it is spam. 

### Solution Design
Batching similar tasks together saves time and reduces stress, much like an operating system reduces context switch overhead. As recruiters receive few standard formats of emails from applicants, what makes sense is an automated email classifier that leverages NLP to offload organisation work. 

## Implementation
### 1. Web-scraping to create dataset
Select 30+ images of email examples per category to improve performance more than the minimal model requirement of 10 images. These are uploaded onto a S3 bucket.
### 2. Data Preparation
Use AWS TextExtract to extract the email text body from images using and convert to required csv format. 5 labels { cold email, acceptance, rejection, follow up, interview acceptance } are assigned for supervised training data. The working for this is in textract.ipynb
### 3. ML model
AWS Comprehend CustomClassifier in multiclass mode labels emails as one of 5 classes. 10% of data is used for testing, which results in 85% model accuracy. The code for our model is in ourCustomClassifier.

![image](https://user-images.githubusercontent.com/99139582/224537550-8eff0010-353b-4ad3-a5d8-e3a61cf62199.png)
### 4. Email Notification (Amazon SNS - Simple Notification Service)
We deploy a AWS Lambda function that is triggered by SNS's email notifications. This function makes an API call to our custom classifier to classify the email text and add a label/tag that helps email services such as OutLook to redirect emails to appropriate folders. The code for the AWS Lambda function is in classifyEmailsAPI.py

![image](https://user-images.githubusercontent.com/99139582/224537444-78939d73-5928-446c-a5ca-5ca31c83794e.png)

## Future Works 
### Technical Improvements 
- Integrate with Amazon SES or WorkMail to generalise across email clients (constraint for setup during short hackathon duration) 
- Allow client for customisation of categories 
### Wider industry application 
- Students: As individuals transitioning into the workforce, organizing professional and academic emails based on context provide clarity and categorization for productivity. 
- SME / Client-facing roles: For Start-up and SME Owners who play multiple roles and communicate with all stakeholders, organizing the channel of communication will save on time that's already short




