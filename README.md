
# NLP_Paragraph_Summariser_WebApp
A simple to no use no-fuss webapp to summarise your paragraphs. Think TL;DR.

Request live demo if http://107.22.27.124:8501/ is down! I am cutting on some server cost, the slug size for this app > 1Gb.

![Demo](demo.gif)

1. Create a Git Repo

_Note: Heroku allows deployment using Git or Docker._

```sh
git init
```

2. Build your App

The code is in main.py

3. Test your App (Local Environment)

```sh
~$ streamlit run main.py
```

4. Create your requeriments.txt file

This file contains the libraries that your code needs to work. To do this, you can use ```pipreqs```.

```sh
pipreqs /path/to/your/app/
```
After this command, a requirements.txt will be created in the folder of your app

```
streamlit
sentencepiece
torch
transformers
```

5. Setup.sh and Procfile

Heroku needs these files for starting the app

    - setup.sh : create a streamlit folder with both credentials.toml and config.toml files.
    - Procfile : This file executes the setup.sh and then call streamlit run to run the app

```sh
# Setup.sh
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
```sh
# Procfile
web: sh setup.sh && streamlit run main.py
```

6. Create a Heroku Account

Create a free account

7. Install Heroku CLI

[Follow these steps](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

8. Login into Heroku CLI

Move to your App folder and execute ```heroku login```

9. Deploy the App

Deploy your app by running ```heroku create``` in your app folder

10. Check it

Check your app by running ```heroku ps:scale web=1```

After that, push your code

```sh
git add .
git commit -m "message"
git push heroku master
```

11. Open it

Open your app using ```heroku open```




# Deploy on AWS EC2 Instance

## Step 1: Launch an instance<a name="ec2-launch-instance"></a>

You can launch a Linux instance using the AWS Management Console as described in the following procedure\. This tutorial is intended to help you quickly launch your first instance, so it doesn't cover all possible options\. For information about advanced options, see [Launch an instance using the new launch instance wizard](ec2-launch-instance-wizard.md)\. For information about other ways to launch your instance, see [Launch your instance](LaunchingAndUsingInstances.md)\.

**To launch an instance**

1. Open the Amazon EC2 console at [https://console\.aws\.amazon\.com/ec2/](https://console.aws.amazon.com/ec2/)\.

1. From the EC2 console dashboard, in the **Launch instance** box, choose **Launch instance**, and then choose **Launch instance** from the options that appear\.

1. Under **Name and tags**, for **Name**, enter a descriptive name for your instance\.

1. Under **Application and OS Images \(Amazon Machine Image\)**, do the following:

   1. Choose **Quick Start**, and then choose Amazon Linux\. This is the operating system \(OS\) for your instance\.

   1. From **Amazon Machine Image \(AMI\)**, select an HVM version of Amazon Linux 2\. Notice that these AMIs are marked **Free tier eligible**\. An *Amazon Machine Image \(AMI\)* is a basic configuration that serves as a template for your instance\.

1. Under **Instance type**, from the **Instance type** list, you can select the hardware configuration for your instance\. Choose the `t2.micro` instance type, which is selected by default\. The `t2.micro` instance type is eligible for the free tier\. In Regions where `t2.micro` is unavailable, you can use a `t3.micro` instance under the free tier\. For more information, see [AWS Free Tier](https://aws.amazon.com/free/)\.

1. Under **Key pair \(login\)**, for **Key pair name**, choose the key pair that you created when getting set up\.
**Warning**  
Do not choose **Proceed without a key pair \(Not recommended\)**\. If you launch your instance without a key pair, then you can't connect to it\.

1. Next to **Network settings**, choose **Edit**\. For **Security group name**, you'll see that the wizard created and selected a security group for you\. You can use this security group, or alternatively you can select the security group that you created when getting set up using the following steps:

   1. Choose **Select existing security group**\.

   1. From **Common security groups**, choose your security group from the list of existing security groups\.

1. Keep the default selections for the other configuration settings for your instance\. 

1. Review a summary of your instance configuration in the **Summary** panel, and when you're ready, choose **Launch instance**\.

1. A confirmation page lets you know that your instance is launching\. Choose **View all instances** to close the confirmation page and return to the console\.

1. On the **Instances** screen, you can view the status of the launch\. It takes a short time for an instance to launch\. When you launch an instance, its initial state is `pending`\. After the instance starts, its state changes to `running` and it receives a public DNS name\. If the **Public IPv4 DNS** column is hidden, choose the settings icon \( ![\[Image NOT FOUND\]](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/settings-icon.png) \) in the top\-right corner, toggle on **Public IPv4 DNS**, and choose **Confirm**\.

1. It can take a few minutes for the instance to be ready for you to connect to it\. Check that your instance has passed its status checks; you can view this information in the **Status check** column\.

## Step 2: Connect to your instance<a name="ec2-connect-to-instance-linux"></a>

There are several ways to connect to your Linux instance\.

**Important**  
You can't connect to your instance unless you launched it with a key pair for which you have the `.pem` file and you launched it with a security group that allows SSH access from your computer\. 

## Step 3: Clean up your instance<a name="ec2-clean-up-your-instance"></a>

After you've finished with the instance that you created for this tutorial, you should clean up by terminating the instance\. 

**Important**  
Terminating an instance effectively deletes it; you can't reconnect to an instance after you've terminated it\.

Step 2 -
Select your instance, and copy the  **_Public DNS(IPv4) Address_**  from the description. It should be something starting with ec2.
Once you have that run the following commands in the folder you saved the  `streamlit.pem`  file.

```bash
chmod 400 streamlit.pem

ssh -i "streamlit.pem" ubuntu@<Your Public DNS(IPv4) Address>
```
Installing Miniconda
```bash
sudo apt-get update

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

bash ~/miniconda.sh -b -p ~/miniconda

echo "PATH=$PATH:$HOME/miniconda/bin" >> ~/.bashrc

source ~/.bashrc
```

Installing Dependencies
```python
pip install streamlit==0.65.2
pip install torch==1.9.0
pip install transformers==4.20.1
```
Getting a copy of app from GitHub
```bash
git clone https://github.com/siddharthksah/NLP_Paragraph_Summariser_WebApp

cd NLP_Paragraph_Summariser_WebApp

streamlit run main.py
```
This should give the external URL which will look something like http://107.22.27.124:8501/
> To make sure the webapp is live even when we exit the terminal, we will use tmux. First, we stop our app using  `Ctrl+C`  and install  `tmux`.


```bash
sudo apt-get install tmux
```
```bash
tmux new -s StreamSession
```
```python
streamlit run main.py
```
You will be able to see your app at the [External URL](http://107.22.27.124:8501/). The **_next step is to detach our TMUX session_** so that it continues running in the background when you leave the SSH shell. To do this just press `Ctrl+B and then D` (Don’t press Ctrl when pressing D).

That's it, done!
