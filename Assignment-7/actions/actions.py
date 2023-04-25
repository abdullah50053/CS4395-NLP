# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

<<<<<<< HEAD
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
=======
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from f1 import get_season


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_season_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        year = tracker.latest_message['text']
        year = [int(i) for i in year.split() if i.isdigit()]
        year1 = ''.join(map(str, year))
        constructor1, driver1 = get_season(year1)
        # response = f"In the {year} season, {driver} won the drivers championship and {constructor} won the constructors championship."
        # dispatcher.utter_season_info(response)
        # dispatcher.utter_template("utter_season_info", tracker, year=year1, driver=driver, constructor=constructor)
        dispatcher.utter_message(
            template="utter_season_info",
            year=year1,
            driver=driver1,
            constructor=constructor1
        )
        # dispatcher.utter_season_info('utter_season_info', tracker, year=year1, driver=driver, constructor=constructor)

        return []
>>>>>>> d8e8571 (Add Assignments)
