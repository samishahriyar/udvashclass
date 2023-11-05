def getYTClassLink(registrationNumber, password, udvashClassLink):

  import requests

  session = requests.session()

  session.post("https://online.udvash-unmesh.com/Account/Login", data = {'RegistrationNumber': registrationNumber, 'Password': password})

  requestHTML = session.get(udvashClassLink).text

  HTMLList = requestHTML.split(";")

  for eachPart in HTMLList:

    if "let videoId" in eachPart:

      requestWithVideoID = eachPart

      break

  return "https://www.youtube.com/watch?v="+requestWithVideoID.split("'")[-2]



if __name__=="__main__":
  reg = input("Enter your Udvash Registration number: ")

  passw = input("Enter your Udvash Password: ")

  classLink = input("Enter the link of your desired class: ")

  print("Here is the link of the class in youtube:", getYTClassLink(reg, passw, classLink))
