import os
import json
import openai
import requests

from dotenv import load_dotenv
load_dotenv()

"""
Helper
"""
def authenticate():
  """
  helper to authenticate into the API using .env key
  :return:
  """
  openai.api_key = os.getenv("PROJECT_API_KEY")


def model_list():
  """
  prints a list of all available models within the OpenAI Model
  :return: none
  """
  json_output = json.dumps(openai.Model.list(), indent=4)
  print(json_output)


def model_retrieve(model_name):
  """
  prints out detail of a particular model within the OpenAI Model
  :param model_name: string of the model name
  :return: none
  """
  print(openai.Model.retrieve(model_name))


def download_image(image_url, file_path):
  """
  downloads the image of the image url and saves it on the local directory.
  image extension can be set with file_path
  :param image_url: string of the url
  :param file_path: string of the file name
  :return: none
  """
  response = requests.get(image_url)
  with open(file_path, "wb") as f:
    f.write(response.content)


"""
Completion 
"""

default_model = "text-davinci-003"

#to-do: default parameters, more parameter specification, etc.
def completion(model, prompt):
  """
  Completes the prompt using the specified model
  :param model: string of the model name
  :param prompt: string of the prompt to enter
  :return: none
  """
  json_output = openai.Completion.create(model=model, prompt=prompt)
  print(json_output["choices"][0]["text"])


def edits(model, prompt):
  pass


#to-do: default parameters, more parameter specification, etc.
def generate_image(prompt):
  """
  generates an image following the prompt of the user.
  downloads the image generated and then saves the image.
  name of the image downloaded follows the user's prompt.
  :param prompt: string of the users prompt
  :return: none
  """
  url = str(prompt)
  json_output = openai.Image.create(prompt=prompt)
  download_image(json_output["data"][0]["url"], url+".jpg")


def edit_image():
  pass


def generate_image_var():
  pass




