# Assignment 7

## Overview

This program is a chatbot that uses the NLP techniques learned in class that carries a limited conversation in the domain of *Formula 1*. The chatbot is powered by [Rasa](https://rasa.com/docs/rasa/), an open source framework for building chat and voice-based AI assistants. 

In addition to Rasa, the chatbot also talks to the [Ergast API](https://ergast.com/mrd/), which provides data for the Formula One series, from the beginning of the world championships in 1950 all the way until present-day. 

## Setup
To set up the chatbot locally, clone the Github repo or download the files as a zip. Follow the [Rasa documentation](https://rasa.com/docs/rasa/next/installation/installing-rasa-open-source) for instructions on installing Rasa and setting up your environment

Once the environment has been set up, navigate to the root folder of the chatbot. There, run the command:

 `rasa train`

 Wait for the model to finish training. Next, run:

 `rasa shell`

 This will start a chat server where you can ask the chatbot questions. Also run:

 `rasa run actions`

 in a separate terminal to ensure the API calls are made.

## Report
[Report Link](https://github.com/abdullah50053/CS4395-NLP)