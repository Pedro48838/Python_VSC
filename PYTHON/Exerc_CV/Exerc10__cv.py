#Crie um conversor de moedas 

print("Conversor de moedas!")

money= float(input("Digite a quantia desejada em reais: "))
dol= money / 4.99
eur= money / 5.48
lib= money / 6.23
fran= money / 5.57

print(f"A quantia informada em dolares é ${dol:.2f}.")
print(f"Em euros fica: €{eur:.2f}.")
print(f"Em libras seria: £{lib:.2f}.")
print(f"E por fim em francos suíços: {fran:.2f} Fr.")
print(f"E para demonstrar mais os conhecimentos em programação, iremos entrelaçar as moedas!!")
print(f"A quantida já convertida em dolares, para euros seria {dol / eur}.")

