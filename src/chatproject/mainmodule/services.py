from loginmodule.models import Login

def getUserConfig(userEmail):
          user = Login.objects.filter(email = userEmail)
          if user:
              print("getUserConfig: user = "+Login.__str__(user[0]))
              return user[0]
          else:
              #python equivalent for null object.Ref : https://www.pythoncentral.io/python-null-equivalent-none/
              return None