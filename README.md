# SQIP 
(Pronounced as 'skip')

SQIP is a Python application aimed at generalize/standardize the interactions with QLDB so that the applications have a common interface for writing auditable data.  

The developer interface for interacting with qldb is a message queue not the SQIP application itself.  By using a message queue the application will be able to dump the data and have confidence their data is completed.  SQIP will be able to pull off the message queue, format the payload to write to QLDB and mark the message queue as job complete.  The gaurantees you get are: 
- gauranteed eventual consistency
- common interface for developers
- tooling agnostic
- standardization of logging and managing auditable data
- scalability and confidence in your audits

![SQIP-Architecture](SQIP-Architecture.svg)

# Code

#### Python Environment
The development workflow uses [pipenv](https://github.com/pypa/pipenv "pipenv repository") to manage the virutal environments.  

#### File Structure

|--.github - github actions
├── app - sqip application
│   └── providers - integration providers
└── infrastructure - all environment deployments
    ├── helm 
    │   └── SQIP
    │       ├── charts
    │       └── templates
    │           └── tests
    └── terraform

# Future
In the future we would love to have a provider system that allows for different queue mechanisms and backend database's or services.  