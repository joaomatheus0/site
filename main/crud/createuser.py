from ..models import Account, SocialAccount
import re
from django.contrib.auth.hashers import make_password

class CreateUser():
    def mainUser(name, email, phone, password, passwordCheck, is_trusty):
        def validation():
            # Validando Senha
            if password != passwordCheck:
                return False, "A senha não atende a todos os requisitos1"

            if len(password) < 8:
                return False, "A senha não atende a todos os requisitos2"
            
            if not re.search("[a-z]", password):
                return False, "A senha não atende a todos os requisitos3"

            if not re.search("[A-Z]", password):
                return False, "A senha não atende a todos os requisitos4"

            if not re.search("[0-9]", password):
                return False, "A senha não atende a todos os requisitos5"

            if not re.search("[_@$]", password):
                return False, "A senha não atende a todos os requisitos6"

            #Decobrir o valor do salt do hash argon2
            p = make_password(password, salt="")

            user = Account.objects.create(
                email = email,
                password = p,
                nome = name, 
                telefone = phone,
                is_trusty = is_trusty,
                username = email
            )
            user.save()

            return True, "Passou"            
        
        verification = validation()

        if verification[0] == False:
            return verification
        else:
            return verification

class Socialuser():
    def user_instagram(login, password, social_network, account):
        
        socialuser = SocialAccount.objects.create(
            login = login,
            password = password,
            social_network = social_network,
        )

        socialuser.account.add(account)
        socialuser.save()