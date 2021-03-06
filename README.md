## :octocat: Github CLI application
[![Build Status](https://travis-ci.org/miskopo/github_cli_app.svg?branch=master)](https://travis-ci.org/miskopo/github_cli_app)
[![codecov](https://codecov.io/gh/miskopo/github_cli_app/branch/master/graph/badge.svg)](https://codecov.io/gh/miskopo/github_cli_app)
![GitHub](https://img.shields.io/github/license/miskopo/github_cli_app.svg)
![Platform](https://img.shields.io/badge/platform-linux-%23FCC624.svg?logo=linux)
![Python versions](https://img.shields.io/badge/python-3.4|3.5|3.6|3.7-3776AB.svg?logo=python)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/miskopo/github_cli_app.svg)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/miskopo)

Ever wanted to browse your repos through CLI? Or create a new one without the hassle of opening the browser? Now you can!

#### What is this project? :camel:
This project uses Github v4 API and Python to provide you with command line interface. Thus you don't have to leave Guake (or you other favourite terminal) in order to
create new repo for your next project, or to see URL of you existing projects, or do whatever the API allows you.

Focus of this project is on simplicity - arguments are intuitive and provided as keywords (some flags are also available).

#### Requirements :rocket:
All you have to do (except installing this application, of course) is to register you API key within Github. To do so, navigate to your settings and choose `Developer settings`.
There, in `Personal access tokens` section, create new token with full rights (you can actually omit rights you know you don't want to use). Copy this token and save it to file 
`api_key` in project directory. **Beware, make sure no one shady gains access to it, as this key enables anyone to do anything with your Github account.**

### Features :construction:
(thick marks implemented features)
- [x] list-my-repositories
- [x] list-user-repositories USERNAME
- [ ] create-new-repo

more to come!

#### Author:
@miskopo

#### Disclaimer:
This project is in no way affiliated with Github and it's not official part of Github per se (yet).
