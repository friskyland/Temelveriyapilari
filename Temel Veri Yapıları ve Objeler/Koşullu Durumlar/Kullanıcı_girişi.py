print("""*****************************************************
Kullanıcı Girişi
*****************************************************""")

sys_userid = "onuro"
sys_pw = "12345"

user_id = input("Kullanıcı Adı:")
user_pw = input("Parola:")

if user_id == sys_userid and user_pw != sys_pw:
    print("Hatalı parola girdiniz.")
elif user_id != sys_userid and user_pw == sys_pw:
    print("Kullanıcı bulunamadı.")
elif user_id != sys_userid and user_pw != sys_pw:
    print("Kullanıcı ve parolayı hatalı girdiniz.")
else:
    print("Giriş Başarılı...")