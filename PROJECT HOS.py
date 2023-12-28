import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='riddhika',database='hospital')
if conn.is_connected():
    cursor=conn.cursor()
    

    def about():
        print("-----------------------------------------------------")
        print("YOU ARE WORKING IN OUR HOSPITAL MANAGEMENT SYSTEM PROJECT. IT HAS 20 OPTIONS TO RUN.")
        print("-----------------------------------------------------")


    def all_patients_details():
        print("-----------------------------------------------------")
        cursor.execute("Select* from hospital.Patients_table")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("Total no. of rows retrieved in resultset :", count)
        for row in data:
            print(row)
        print("-----------------------------------------------------")

    def all_doctors_details():
        print("-----------------------------------------------------")
        cursor.execute("select * from hospital.doctor")
        data=cursor.fetchall()
        count=cursor.rowcount
        print("Total no. of rows retrieved in resultset :",count)
        for row in data:
            print(row)
        print("-----------------------------------------------------")

    def search_patient():
        print("-----------------------------------------------------")
        iD=input("Enter patient's ID whose details are to be displayed:")
        cursor.execute("select * from hospital.Patients_table where Patients_Id=%s"%(iD))
        dataa=cursor.fetchone()
        if dataa is None:
                print("Not valid ID!")
        else:
                print(dataa)
        print("-----------------------------------------------------")


    def search_doctor():
        print("-----------------------------------------------------")
        Id=input("Enter the doctor's id whose details are required:")
        cursor.execute("select * from hospital.doctor where Doctors_id=%s"%(Id))
        data=cursor.fetchone()
        if data is None:
                print("Not valid ID!")
        else:
                print(data)
        print("-----------------------------------------------------")


    def treatments_available():
        print("-----------------------------------------------------")
        cursor.execute("select * from hospital_.treatment")
        data=cursor.fetchall()
        for i in data:
            print(i)
        print("-----------------------------------------------------")

    def lab_tests_available():
        print("-----------------------------------------------------")
        cursor.execute("select * from hospital.lab")
        data=cursor.fetchall()
        for i in data:
            print(i)
        print("-----------------------------------------------------")

    def adm_and_dis():
        print("-----------------------------------------------------")
        cursor.execute("select * from hospital_.admission_and_discharging")
        dataa=cursor.fetchall()
        for i in dataa:
            print(i)
        print("-----------------------------------------------------")

    def pharmacy():
        print("-----------------------------------------------------")
        cursor.execute("select * from hospital_.pharmacy")
        data=cursor.fetchall()
        for i in data:
            print(i)
        print("-----------------------------------------------------")
        

    def adjoin_patient():
        print("-----------------------------------------------------")
        Patients_id=input('Enter id of patient:')
        Patients_name=input('Enter patient name:')
        Symptoms=input('Enter symptoms of patient(Press l for list of symptoms):')
        if Symptoms=="l":
            sym_list()
            Symptoms=input('Enter symptoms of patient : ')
        Adm_date=input('Enter admission date:')
        disch_date=input('Enter discharge date:')
        Treatment,Disease,Dname,Doctors_id=doctor_assign(Symptoms)
        cursor.execute("select medicines from hospital_.pharmacy where Disease='{}'".format(Disease))
        medicines=cursor.fetchone()[0]
        Ward_no=input('Enter ward no.of patient:')
        cursor.execute("select test from hospital.lab where Disease='{}'".format(Disease))
        Tests=cursor.fetchone()[0]
        sql_insert='insert into hospital.Patients_table(Patients_id,Patients_name,Symptoms,Doctors_ID,Adm_date,disch_date,medicines,Ward_no,Tests,Disease,Treatment) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val=(Patients_id,Patients_name,Symptoms,Doctors_id,Adm_date,disch_date,medicines,Ward_no,Tests,Disease,Treatment)
        cursor.execute(sql_insert,val)
        print('registered new patient')
        conn.commit()
        print("-----------------------------------------------------")

    def adjoin_doctor():
        print("-----------------------------------------------------")
        Doctors_id=input('Enter id of doctor:')
        Doctors_name=input('Enter doctor name:')
        Treatment=input('Enter treatment given by doctor:')
        Consultation_fees=float(input('Enter consultation fees of doctor:'))
        Disease=input('Enter disease treated by doctor:')
        sql_insert='insert into hospital.doctor(Doctors_id,Doctors_name,Treatment,Consultation_fees,Disease) values (%s,%s,%s,%s,%s)'
        val=(Doctors_id,Doctors_name,Treatment,Consultation_fees,Disease)
        cursor.execute(sql_insert,val)
        print('registered new doctor')
        conn.commit()
        print("-----------------------------------------------------")



    def update_doctor():
        print("-----------------------------------------------------")
        while True:
            Doctors_id=input('Enter id of doctor:')
            Doctors_name=input('Enter updated doctors name:')
            Treatment=input('Enter updated treatment given by doctor:')
            Consultation_fees=float(input('Enter updated consultation fees of doctor:'))
            Disease=input('Enter updated disease treated by doctor:')
            val=[Doctors_name,Treatment,Consultation_fees,Disease,Doctors_id]
            upd='update hospital.doctor set Doctors_name=%s,Treatment=%s,Consultation_fees=%s,Disease=%s where Doctors_id=%s'
            cursor.execute(upd,val)
            conn.commit()
            break
        cursor.execute('select * from hospital.doctor')
        data=cursor.fetchall()
        for i in data:
            print(i)
            print('Record Updated')
            conn.commit()


    def update_patient():
        print("-----------------------------------------------------")
        while True:
            Patients_Id=input('Enter id of patient:')
            Patients_name=input('Enter updated patients name:')
            Adm_date=input('Enter updated admission date:')
            disch_date=input('Enter updated discharge date:')
            val=[Patients_name,Adm_date,disch_date,Patients_Id]
            upd='update hospital_.patients_table set Patients_name=\"'+Patients_name+'\",Adm_date=\"'+Adm_date+'\",disch_date=\"'+disch_date+'\"where Patients_id=\"'+Patients_Id+'\" ;'
            cursor.execute(upd)
            conn.commit()
            break
        cursor.execute('select * from hospital.Patients_table where Patients_id=\"'+Patients_Id+'\";')
        data=cursor.fetchall()
        for i in data:
            print(i)
            print('Record Updated')
        conn.commit()
        print("-----------------------------------------------------")

    def sym_list():
        print("-----------------------------------------------------------")
        print("The list of symptoms is-")
        print("1.Back pain,sore muscles")
        print("2.Bloody vomit,fatigue,nausea")
        print("3.Swelling in groin, bulge in groin")
        print("4.Swelling of breasts,nipple discharge")
        print("5.Chest pain,palpitations,abnormal heart rhythms")
        print("6.Bloody urine,swollen extremities,puffy eyes")
        print("7.Vertigo,mental confusion,headaches")
        print("8.Excessive urination,weight loss,increased hunger")
        print("9.Neck swelling,weight gain,breath shortness")
        print("10.Inability to smell & taste,cold & cough,fever")
        print("11.Runny nose,cough,headaches,fever,stomach ache,chicken pox,diarhhoea,dengue")
        print("-----------------------------------------------------------")

    def provide_medication():
        sym_list()
        Symptoms=input("Enter the patient's symptoms:")
        a,b,c,d=doctor_assign(Symptoms)
        print("You are suffering with",b,",the Patient will have to be admitted asap !\nPlease choose option 10.\n the treatment that will be provided to you is",a,"and the doctor apoointed to you is",c)
        
        
    def search_patientopd():
       print("-----------------------------------------------------")
       ppid=input("Enter the patient's id whose details are required:")
       cursor.execute("select * from hospital_.opd where Patients_id=%s"%(ppid))
       data=cursor.fetchone()
       if data is None:
            print("Invalid patient id")
       else :
            print(data)
       print("-----------------------------------------------------")


    def admit_patientopd():
       print("-----------------------------------------------------")
       while True:
           Sno=int(input("Enter the serial no."))
           dID=int(input("Enter doctor's ID:"))
           Name=input("Enter the doctor's name:")
           pid=input("Enter patient's id:")
           pname=input("Enter patient's name:")
           disease_=input("Enter the disease required to be treated:")
           Med=input("Enter the Medicines to treat the respective disease:")
           bill=int(input("Enter the total bill of the medicines:"))
           querry="insert into hospital_.opd values({},{},'{}',{},'{}','{}','{}',{})".format(Sno,dID,Name,pid,pname,disease_,Med,bill)
           cursor.execute(querry)
           conn.commit()
           ch=input("Enter more records?(y/n)")
           if ch in 'Nn':
               break
           cursor.execute("select * from hospital_.opd")
           data=cursor.fetchall()
           for i in data:
               print(i)
           print("-----------------------------------------------------")


    def search_detailsED():
        print("-----------------------------------------------------")
        Id=input("Enter the patient's id whose details are required:")
        cursor.execute("select * from hospital_.Emergency where Patient_ID=%s"%(Id))
        data=cursor.fetchone()
        if data is None:
            print("Invalid patient id")
        else :
            print(data)
        print("-----------------------------------------------------")

            
    
    def add_patientED():
        print("-----------------------------------------------------")
        while True:
            sno=int(input("Enter the serial no."))
            ID=int(input("Enter Patients ID:"))
            name=input("Enter the Patients name:")
            treat_=input("Enter the respective treatment:")
            tests_=input("Enter the required tests:")
            expenses_=input("Enter the expenses of treatment:")
            query="insert into hospital_.Emergency values({},{},'{}','{}','{}',{})".format(sno,ID,name,treat_,tests_,expenses_,)
            cursor.execute(query)
            conn.commit()
            ch=input("Enter more records?(y/n)")
            if ch in 'Nn':
                break
        cursor.execute("select * from hospital_.Emergency")
        data=cursor.fetchall()
        for i in data:
            print(i)
        print("-----------------------------------------------------")
        

    
    def search_adm_and_dis():
        print("---------------------------------------------------")
        P_ID=int(input("Enter the patient's ID whose admission and discharging dates you want to know:"))
        cursor.execute("Select Adm_date,disch_date from hospital_.admission_and_discharging where patients_ID=%s"%format(P_ID))
        data=cursor.fetchall()
        count=cursor.rowcount
        print("Total no. of rows retrieved in resultset :", count)
        for row in data:
            print(row)
        
        else:
            print("Unauthentic Patient ID")
        
        print("-------------------------------------------------")
    def doctor_assign(Symptoms):
        if Symptoms in ["Back pain,sore muscles"]:
            Treatment="Physiotherapy"
            Disease="Arthritis"
            Doctor="Dr. Meera Shah"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Bloody vomit,fatigue,nausea"]:
            Treatment="Radiation therapy"
            Disease="Prostate cancer"
            Doctor="Dr. Rajeev Saxena"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Swelling in groin,bulge in groin"]:
            Treatment="General surgery"
            Disease="Hernia"
            Doctor="Dr. Rahul Jain"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Swelling of breasts,nipple discharge"]:
            Treatment="Chemotherapy"
            Disease="Breast cancer"
            Doctor="Dr. Manish Singh"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Chest pain,palpitations,abnormal heart rhythms"]:
            Treatment="Angioplasty"
            Disease="Heart bypass"
            Doctor="Dr.Chetan Gupta"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Bloody urine,swollen extremities,puffy eyes"]:
            Treatment="Dialysis"
            Disease="Kidney failure"
            Doctor="Dr. Aditi Mishra"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Vertigo,mental confusion,headaches"]:
            Treatment="Neurosurgery"
            Disease="Brain tumour"
            Doctor="Tushar Singh"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Excessive urination,weight loss,increased hunger"]:
            Treatment="Medication"
            Disease="Diabetes"
            Doctor="Dr. Manoj Kumar"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Neck swelling,weight gain,breath shortness"]:
            Treatment="Thyroidectomy"
            Disease="Goiter"
            Doctor="Dr.Priya Sharma"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Inability to smell & taste,cold & cough,fever"]:
            Treatment="ECMO"
            Disease="COVID-19"
            Doctor=" Vipin Rajput"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        elif Symptoms in ["Runny nose,cough,headaches,fever,stomach ache,chicken pox,diarhhoea,dengue"]:
            Treatment="General medication"
            Disease="Basic diseases that can be treated with proper medication"
            Doctor="Dr. Manoj Kumar"
            cursor.execute('select doctors_id from hospital.doctor where doctors_name="'+Doctor+'";')
            Doctors_id=cursor.fetchone()[0]
            return Treatment,Disease,Doctor,Doctors_id
        
    def billing():
        sym_list()
        
        Number_of_days_of_treatment=(int(input("Enter the no. of days for which treatment continued:")))
        Symptoms=input("Enter the patient's symptoms:")
        if Symptoms in ["Back pain,sore muscles"]:
            Treatment="Physiotherapy"
            D="Arthritis"
            Doctor="Dr. Meera Shah"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Bloody vomit,fatigue,nausea"]:
            Treatment="Radiation therapy"
            D="Prostate cancer"
            Doctor="Dr. Lata Mehra"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Swelling in groin,bulge in groin"]:
            Treatment="General surgery"
            D="Hernia"
            Doctor="Dr. Rahul Jain"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Swelling of breasts,nipple discharge"]:
            Treatment="Chemotherapy"
            D="Breast cancer"
            Doctor="Dr. Manish Singh"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Chest pain,palpitations,abnormal heart rhythms"]:
            Treatment="Angioplasty"
            D="Heart bypass"
            Doctor="Dr.Chetan Gupta"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Bloody urine,swollen extremities,puffy eyes"]:
            Treatment="Dialysis"
            D="Kidney failure"
            Doctor="Dr. Aditi Mishra"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Vertigo,mental confusion,headaches"]:
            Treatment="Neurosurgery"
            D="Brain tumour"
            Doctor="Tushar Singh"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Excessive urination,weight loss,increased hunger"]:
            Treatment="Medication"
            D="Diabetes"
            Doctor="Dr. Manoj Kumar"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Neck swelling,weight gain,breath shortness"]:
            Treatment="Thyroidectomy"
            D="Goiter"
            Doctor="Dr.Priya Sharma"
            print("The patient will have to be admitted asap! Please choose option 11")
        elif Symptoms in ["Inability to smell & taste,cold & cough,fever"]:
            Treatment="ECMO"
            D="COVID-19"
            Doctor=" Vipin Rajput"
        elif Symptoms in ["Runny nose,cough,headaches,fever,stomach ache,chicken pox,diarhhoea,dengue"]:
            Treatment="General medication"
            D="Basic diseases that can be treated with proper medication"
            Doctor="Dr. Manoj Kumar"
        else:
            print("Sorry, we're unable to provide you proper treatment in this hospital. Kindly refer somewhere else, we hope u have a healthy life ahead!")
        print("You are suffering with",D
              ,",the treatment that will be provided to you is",Treatment,"and the doctor apoointed to you is",Doctor)
        
        sql="Select lab.Fees,doctor.Consultation_fees from hospital.lab,hospital.doctor where lab.Disease=doctor.Disease and lab.Disease=\""+D+"\";"
        cursor.execute(sql)
        data=cursor.fetchone()
        fees=data[0]
        cfees=data[1]
        cursor.execute("Select Cost from hospital_.pharmacy where Disease='{}'".format(D))
        dataa=cursor.fetchone()
        for i in dataa:
            bill2=i
        cursor.execute("Select Fees from hospital_.treatment where Disease='{}'".format(D))
        dat=cursor.fetchone()
        for a in dat:
            bill3=a
        print(" Consultation fees :\t",cfees)
        print("    LAB FEE        :\t",fees)
        print(" Cost of Medicines :\t",bill2)
        print(" Treatment fees    :\t",bill3) 
        Bill=(fees+cfees+bill2+bill3)*Number_of_days_of_treatment
        print("The total bill of patient is \t",Bill)
        
c="Y"
while c =="Y" or c=="y":
    print("___________________________MENU________________________________")
    print("Welcome to our Hospital")
    print("------------------------------------------------------------------")
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("------------------------------------------------------------------")
    print("1.ABOUT US ")
    print("2.ALL PATIENTS' DETAILS")
    print("3.ALL DOCTORS' DETAILS")
    print("4.SEARCH PATIENT DETAILS")
    print("5.SEARCH DOCTOR DETAILS")
    print("6.TREATMENTS AVAILABLE")
    print("7.LAB TESTS AVAILABLE")
    print("8.ADMISSION & DISCHARGE RECORD")
    print("9.PHARMACY")
    print("10.ADJOIN NEW PATIENT")
    print("11.ADJOIN NEW DOCTOR")
    print("12.UPDATE DOCTOR DETAILS")
    print("13.UPDATE PATIENT DETAILS")
    print("14.PROVIDE MEDICATION")
    print("15.SEARCH PATIENT IN OPD")
    print("16.ADMIT PATIENT IN OPD")
    print("17.SEARCH PATIENT IN ED")
    print("18.ADD PATIENT IN ED")
    print("19.SEARCH ADMISSION & DISCHARGE")
    print("20.BILL DETAILS")
    ch=int(input("Enter your choice:"))
    if ch==1:
        about()
    elif ch==2:
       all_patients_details()
    elif ch==3:
       all_doctors_details()
    elif ch==4:
        search_patient()
    elif ch==5:
        search_doctor()
    elif ch==6:
        treatments_available()
    elif ch==7:
        lab_tests_available()
    elif ch==8:
        adm_and_dis()
    elif ch==9:
        pharmacy()
    elif ch==10:
        adjoin_patient()
    elif ch==11:
        adjoin_doctor()
    elif ch==12:
        update_doctor()
    elif ch==13:
        update_patient()
    elif ch==14:
        provide_medication()
    elif ch==15:
        search_patientopd()
    elif ch==16:
        admit_patientopd()
    elif ch==17:
        search_detailsED()
    elif ch==18:
        add_patientED()
    elif ch==19:
        search_adm_and_dis()
    elif ch==20:
        billing()
    c=input("Do you want to continue?")
    


