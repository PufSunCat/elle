def sareizinat_ar_divi(x):
    return 2 * x

print(sareizinat_ar_divi(8))


def say_hello_to(salutation, name):
    print(f"{salutation}. Laba siena {name}!")

say_hello_to("Mjau", "Laura")
say_hello_to('jaj', 'Matis')



#names = ['Kate','Markuss']
#
#for n in names:
#    say_hello_to(n)



def f_to_c(temp_f, skala):
    if skala == 'C':
        
        return(temp_f - 32, skala) * (5/9)


        return(temp_f - 32, skala) * (5/9)


user_import = float(input('enter - ') ("skaka"))
print(f_to_c(user_import))