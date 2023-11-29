# Employees Lookup (emploo)

[![Test & Checks](https://github.com/4383/emploo/actions/workflows/main.yml/badge.svg)](https://github.com/4383/emploo/actions/workflows/main.yml)
![PyPI](https://img.shields.io/pypi/v/emploo.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/emploo.svg)
![PyPI - Status](https://img.shields.io/pypi/status/emploo.svg)
[![Downloads](https://pepy.tech/badge/emploo)](https://pepy.tech/project/emploo)
[![Downloads](https://pepy.tech/badge/emploo/month)](https://pepy.tech/project/emploo/month)

OSINT tool to list employees of a given company. Profiles discovering
based on Linkedin data.

<img src="https://github.com/4383/emploo/blob/main/disclaimer.png" width="600"
alt="This tool is for educational purposes only, I am not responsible for its use." />

## 📋 Description

During an OSINT audit discovering company's employees can lead security
experts to a valuable source of information. The goal of this tool is to
give you automation to discover this kind of data. The JSON output
can be used in your OSINT toolchain to automatize your reports generation by
being piped with other tools.

This tool, is a command line tool who give you company profiles research
results in JSON format.

This tool is compatible with Windows, Linux and Mac operanting systems.

## ✅ Prerequisites

To run emploo:
- you must own a valid google account.
- install python 3.9 or higher versions

## 💾 Install

```
$ pip install emploo
```

## ⚙️  Init your environment - First run only

Employees Lookup (emploo) is based on the Google Programmable Search Engine
(GPSE). More info about GPSE are available here:
https://developers.google.com/custom-search/docs/tutorial/creatingcse

Firstly, you must create a new empty GPSE by using the
[control panel] (https://programmablesearchengine.google.com/controlpanel/all).

Once the new GPSE is create you should run the command `$ emploo init` and,
by using the GPSE control panel, then, you should import the output of this
previous command as an annotation of your fresly created GPSE.

Now copy the GPSE ID corresponding to your fresly created GPSE. It will be
passed to the emploo commands later.

At this point you should visit https://developers.google.com/custom-search/v1/overview
and click on the "Get a Key" button to obtain your google API key. It will be
passed to the emploo commands later.

Store your credentials to reuse them later during your researches.

## 🚀 Usage

Simply run the following command and obtain your results at the json format:

```
$ emploo search <company name> -i <google-gpse-id> -k <google-api-key> -o /tmp/example
```

The previous command search for the given company name by using the given
credentials, and output its results into the `/tmp/example` file.

Replace `<company name>` by the name of the company that you want to lookup.
Replace `<google-gpse-id>` and `<google-api-key>` by your own credentials.

## ⚠️  Warnings

Google API usages are limited to 100 results max. Even if you own a premium
Google account this threshold still apply. In other words, for now, you can't
collect more than 100 profiles with this tools, but 100 profiles is still a
good starting point to ignit your investigations.

Also you should notice that the Google GPSE queries are limited to a quotas
allowed by days. You are not able to proceed researches against an infinite
number of companies each days. You should perform your researches on a daily
basis.

## 😉 Contribute

If you want to contribute to this project
[please first read the contribution guidelines](https://github.com/4383/emploo/blob/main/CONTRIBUTING.md)
