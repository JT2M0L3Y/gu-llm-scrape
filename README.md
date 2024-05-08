# CPSC 324: BIG DATA - FINAL PROJECT
## Author: Jonathan Smoley (JT2M0L3Y)
## Project: LLM Context Preparation

## Table of Contents:
- [Introduction](#introduction)
- [Services Used](#services-used)
- [Additional Information](#additional-information)

## Introduction
This project is an application of the tools and techniques learned during the 6th homework assignment of the Spring 2024 Big Data course. The goal of this project is to prepare a set of contextual clues for any open-source large language model accessed through the Ollama framework. This of this as providing a script to the LLM actor which requires some additional context to play its role.

In particular, this project provides data from Gonzaga University's public domain, [www.gonzaga.edu](www.gonzaga.edu), to prepare an LLM trained on knowledge about Gonzaga University. To accomplish this, a number of Google Cloud Platform (GCP) services are used to scrape the website, process the data, and prepare the data for use in the LLM. These are discussed in more detail below.

## Services Used
To accomplish this project, the following GCP services were used:
- Cloud Storage: to store the raw data from the website
- Cloud Functions: to scrape the website and store the data in Cloud Storage
- Cloud Pub/Sub: to trigger the Cloud Function to scrape the website
- Cloud Scheduler: to schedule the scraping of the website at regular intervals

### Cloud Storage
Cloud Storage is used to store the raw data from the website. This data is stored in a bucket named `llm-context-preparation`. The data is stored in a folder named `www.gonzaga.edu` to keep the data organized.

### Cloud Functions
Cloud Functions is used to scrape the website and store the data in Cloud Storage. The function is triggered by a message published to a Pub/Sub topic. The function scrapes the website and stores the data in the `llm-context-preparation` bucket in the `www.gonzaga.edu` folder.

### Cloud Pub/Sub
Cloud Pub/Sub is used to trigger the Cloud Function to scrape the website. A message is published to the `llm-context-preparation` topic to trigger the function.

### Cloud Scheduler
Cloud Scheduler is used to schedule the scraping of the website at regular intervals. The scheduler is configured to publish a message to the `llm-context-preparation` topic every 12 hours. This notifies a Pub/Sub topic and triggers the Cloud Function to scrape the website (a subscriber to this topic).

## Additional Information
Included is a write-up with further information about the purpose and results of this project available under the name `write-up.pdf`.