<div align="center">

![](static/img/leaveit2givit.jpg)

</div>

# background & vision

“Givit”is a non-profitable organization which operated by IDC student and aiming to help economically struggling students(“friends”) by helping them to furnish their apartments.

Givit web-application will automate the procces of gathering our friends demands, findind the furniture online and get thier approval for coordinate and transfer.

# app components

<div align="center">

![](static/img/overview.png)

</div>

## Backend

implemted with Django the following components:

1. Demand controller-manage the friends requests and the demand DB.
2. Found controller-get updates from found-DB mange the verification and coordination procces.

3. Gatherer Controller:
   - automated system that will iterate the relevant sites(firat step Agora site second step facbook groups).
   - get requests from the Demand DB and updete the found DB.
   - operate details: we open vm in google cloud and using crontab run our script every hour, how create json file with our new searches.

DB- TBD.

## Frontend

implemented with bootstrap the following components:

1. friends:

   - private Feed - tracks the furniture which was found by the app, waits for the friend approval.
   - request box - a form which the friends will fill in order to request new items.

2. coordinte: track all the items that was approved by our friends.

## login system

- two users groups: friends, coordinates.
- technology- TBD.

## CI/CD- TBD

## issues & dillemas

- online feed is good ides with server-sdie rendering (or its better clieant side? how to avoid react in first stage?)
- DB?

# Getting started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them:

- Download and Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/) on your local computer
- Clone/ Download the zip file from the Groot repository to your local computer

### Initializing Project Groot Virtual Environment

A step by step series that tell you how to get Project Groot up and running

1. Clone + Fork the repository
2. Open command prompt and navigate to the local directory where all the files are
3. Spin the environment using:

```
   vagrant up
   vagrant ssh
```

4. navigate to the sync repo in vm

```
   cd /vagrant/givitsite/
```

5. Creating an admin user

First we’ll need to create a user who can login to the admin site. Run the following command:

```
   python3 manage.py createsuperuser
```

Enter your desired username and press enter.
You will then be prompted for your desired email address
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

6.

```
   python3 manage.py runserver 0:8000
```

5. open your browser and nevigate to http://localhost:8000/Hello/

6. When finished, tear down the environment using:

```
exit
vagrant destroy -f
```

# Dependencies

1. We supply a requirement.txt and a bootstrap.sh file that will install all the needed libraries when you do **vagrant up**, with this command:

```
pip3 install -r /vagrant/requirements.txt
```

2. If you want to see all the needed libraries for GIVIT-app you can find in **requirment.txt**

3. Finally, we create requirements.txt file to make it easier for other developers to install the correct versions of the required Python libraries for our project.

   if you a develper and you want to create or update this file, you need to do:

   - after we do **vagrant up** and **vagrant ssh**
   - and then **cd /vagrant/givitsite/**
   - when you finish to "pip3 install" all the new library, do the following command:

```
pip3 freeze > /vagrant/requirements.txt
```

for more information:

https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e#:~:text=In%20short%2C%20we%20generate%20and,Python%20code%20we've%20written.

# team members:

### -Rotem Ben Zvi

### -Nadav Shoshan

### -Matan Sinai

### -Tal kind

### -Lior Sidi
