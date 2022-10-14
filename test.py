from verifonePED import verifone_device

my_ped = verifone_device(ip_address='192.168.20.161', username='1113', password='1113')

my_ped.login()

if my_ped.logged_in:
    print('Transaction Status =', my_ped.transaction(1.00))
else:
    print('Error logging in!')
