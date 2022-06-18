import csv

#function to save the credentials of the user for registration
def save_data(self):
    with open('user_file.csv', mode='a') as user_file:
        if user_file.tell() == 0:
            user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            user_writer.writerow(['Username','Email','Full Name','Password'])
            user_writer.writerow([self.username,self.email,self.full_name,self.hash])
            user_file.close()
        else:
            user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            user_writer.writerow([self.username,self.email,self.full_name,self.hash])
            user_file.close()
        

    