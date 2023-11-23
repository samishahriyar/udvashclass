def getYTClassLink(registrationNumber, password, udvashClassLink):

  import requests, re

  session = requests.session()

  session.post("https://online.udvash-unmesh.com/Account/Login", data = {'RegistrationNumber': registrationNumber, 'Password': password})

  requestHTML = session.get(udvashClassLink).text

  HTMLList = requestHTML.split(";")

  pattern = re.compile("data-youtube-video=['\"][a-zA-Z0-9]+['\"] ")

  if pattern:
    span = pattern.search(requestHTML).span()

    return "https://www.youtube.com/watch?v="+requestHTML[span[0]+20: span[1]-2]

  else:

    return "The class may not be downloaded right now or you may have provided wrong information, sorry for that."

if __name__=="__main__":

  reg = input("Enter your Udvash Registration number: ")

  passw = input("Enter your Udvash Password: ")

  classLink = input("Enter the link of your desired class: ")

  print("\n\nHere is the link of the class:", getYTClassLink(reg, passw, classLink))
