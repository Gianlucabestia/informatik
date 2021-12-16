jahreseinkommen = float(input(str("Wie viel Jahreseinkommen haben sie: ")))
if jahreseinkommen<=10.000:
    print(jahreseinkommen*0.009)
if jahreseinkommen<=40.000:
    print(jahreseinkommen*0.211)
if jahreseinkommen<=60.000:
    print(jahreseinkommen*0.271)
if jahreseinkommen>60.000:
    print(jahreseinkommen*0.331)