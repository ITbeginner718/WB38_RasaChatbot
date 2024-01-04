# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import yaml

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        diseasecode_info = tracker.get_slot('disease_code')
        diseasecode_info = diseasecode_info.lower()
        print(diseasecode_info)
        
        try:
          # YAML 파일 로드
          with open('actions\Disease_info.yml', 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)

          # 필요한 데이터 추출
          disease_data= yaml_data[diseasecode_info]['disease']
          cause_data = yaml_data[diseasecode_info]['cause']
          treatment_data = yaml_data[diseasecode_info]['treatment']
          management_data = yaml_data[diseasecode_info]['management']
          
          dispatcher.utter_message(text=disease_data+'\a'+cause_data+'\a'+treatment_data+'\a'+management_data)
          
        except KeyError:
          dispatcher.utter_message(text='keyerror: 해당 질병코드가 없습니다.')
        
          return []
