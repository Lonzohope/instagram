from django import forms


class SignUpForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    def validate(self):
        try:
            self.username = self.args[0]["username"]
            self.password = self.args[0]["password"]
            self.email = self.args[0]["email"]

        except Exception as e:
            return self.error("Malformed request, did not process.") 

        if not re.match('^[a-zA-Z0-9_]+$', self.username):
            return self.error("Invalid username, must be fit [a-zA-Z0-9_]")
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            return self.error("Invalid email syntax.")
        if len(self.username) < 4 or len(self.username) > 20:
            return self.error("Username must be between 3 and 20 characters long.")
        if len(self.password) < 6 or len(self.password) > 32:
            return self.error("Password must be between 6 and 32 characters long.")
        if len(self,email) < 6 or len(self.email) > 140:
            return self.error("Email must be between 6 and 32 characters long.")
        if User.objects.filter(username=self.username).exists():
            return self.error("Username already in use.")
        

        if User.objects.filter(username=self.username).exists():
            return self.error("Username already in use.")
        
        if User.objects.filter(email=self.email).exists():
            return self.error("Email address already in use.")

        u = User(username=self.username, password=make_password(self.password), email=self.email)
        u.save()

        return self.success("Account Created!")

    def error(self, message):
        return json.dumps({ "Status": "Error", "Message": message }, ensure_ascii=)


    def success(self, message):
        return json.dumps({ "Status": "Success", "Message": message }, ensure_ascii=)

    
    def items(self, json):
        return json

    
    def output(self):
        return self.validate()



    



# class AjaxLogin(Ajax):

#     def validate(self):
#         try:
#             self.username = self.args[0]["username"]
#             self.password = self.args[0]["password"]
#             self.email = self.args[0]["email"]

#         except Exception as e:
#             return self.error("Malformed request, did not process.") 

#         if not re.match('^[a-zA-Z0-9_]+$', self.username):
#             return self.error("Invalid username, must be fit [a-zA-Z0-9_]")
#         if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
#             return self.error("Invalid email syntax.")
#         if len(self.username) < 4 or len(self.username) > 20:
#             return self.error("Username must be between 3 and 20 characters long.")
#         if len(self.password) < 6 or len(self.password) > 32:
#             return self.error("Password must be between 6 and 32 characters long.")
#         if len(self,email) < 6 or len(self.email) > 140:
#             return self.error("Email must be between 6 and 32 characters long.")

        
#         if not User.objects.filter(email=self.email).exists():
#             return None, self.error("Email or password is incorrect.")

#         if not check_password(self.password, User.objects.filter(email=self.email)[0].password():
#             return None, self.error("Email or password is incorrect.")

        
#         u = User.objects.filter(email=self.email)[0]

#         return u, self.success("User logged in!")
        