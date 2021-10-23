# Czech utf16 encoder
Web application to translate czech special signs into UTF16 encoding. I found the use for this when working with R Markdown, which could not handle the czech signs, so the input had to be given in UTF16 encoding:

![image](https://user-images.githubusercontent.com/79012119/138562494-585862ef-d825-454b-a0d8-ff72a936ec78.png)

## Deployment
The application was deployed using AWS Elastic Beanstalk. I also use AWS RDS MySQL server to store and display past encoded messages.
