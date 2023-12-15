import os
import sys

from backward_chaining import BackwardChaining
from forward_chaining import ForwardChaining
from class_all import *
from class_all import ConvertData

from email.message import EmailMessage
import ssl,smtplib
# biến khởi tạo
person = Person(None, None, None)
validate = Validate()
list_symptom_of_person = []  # list các triệu chứng người dùng khi trả lời là yes
db = ConvertData()
db.convertbenh()  # bang benh
db.converttrieuchung()  # bang trieu chung
db.getfc()
db.getbc()
luat_lui = db.groupbc()
luat_tien = db.groupfc()

#################################################
# 1. câu hỏi chào hỏi
def welcome_question():
    print("-->Chatbot: Xin chào, tôi là chatbot tư vấn khám chữa bệnh thông thường cho trẻ em từ 3 - 10 tuổi!")
    print("-->Chatbot: Để nhận lời khuyên và chuẩn đoán chi tiết, hãy để lại email, tên của bạn")

    print("-->Chatbot: Hãy nhập tên")
    person.name = validate.validate_name(input())
    print(f'-->Người dùng: Tên của tôi là, {person.name}')

    print("-->Chatbot: hãy nhập email")
    person.email = validate.validate_email(input())
    print(f'-->Người dùng: Email của tôi là, {person.email}')

    # print("chúng tôi đã nhận được thông tin của bạn đã cung cấp",person.name)
    print("chúng tôi đã nhận được thông tin của bạn đã cung cấp")

    return person


    # print("-->Chatbot: hãy nhập số điện thoại")
    # person.phoneNumber = validate.validate_phonenumber(input())
    # print(f'-->Người dùng: số điện thoại của tôi là {person.phoneNumber}')

#################################################################
# 2. 1 số câu hỏi đầu tiên ( triệu chứng đặc trưng của từng bệnh nhóm bệnh(truyền nhiễm, hô hấp, tiêu hóa) )
def first_question(list_symptom_of_person, person):
 
    AllSymLst = [db.resulttrieutrung[26], db.resulttrieutrung[16], db.resulttrieutrung[21]
                ]
    
    NewAllSymLst = []
    for i in AllSymLst:
        NewAllSymLst.append(i["idtrieuchung"])

    while (1):
        if (len(list_symptom_of_person) == len(AllSymLst)):
            break
        if (len(list_symptom_of_person) == 0):
            print(f'-->Chatbot: {person.name} có triệu trứng nào ở dưới đây không (Nhập số thứ tự của triệu chứng để chọn)')
        else:
            print(f'-->Chatbot: {person.name} có triệu trứng nào nữa ở dưới đây không (Nhập số thứ tự của triệu chứng để chọn.)')

        count = 1
        for i in AllSymLst:
            if (i not in list_symptom_of_person):
                print(f'{count}. {i["noidung"]} \n')
            count += 1

        print("0. Con tôi không có triệu chứng nào ở trên\n -------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')

        if (answer == '0'):
            break
        elif (int(answer) < 0 or int(answer) > 3):
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 3')
            continue
        else:
            list_symptom_of_person.append(AllSymLst[int(answer)-1])
        print(
            f'-->Chatbot: Danh sách mã các triệu chứng {person.name} đang mắc:')
        print([i['idtrieuchung'] for i in list_symptom_of_person])
    return list_symptom_of_person

#############################################################
# 3. Chuẩn đoán nhóm bệnh đang mắc dựa trên triệu chứng đã chọn
def second_question(list_symptom_of_person, person):


    print('jasdasdasd')
    # Location_StomachAcheSymLst = [db.resulttrieutrung[15]]
    # Location_StomachAcheSymLst2 = [db.resulttrieutrung[19]]
    # Location_StomachAcheSymLst3 = [db.resulttrieutrung[23]]
    
    while (1):
        check = {'idtrieuchung': 'S27', 'noidung': 'Sốt'}
        check2 = {'idtrieuchung': 'S17', 'noidung': 'Hắt hơi nhiều'}
        check3 = {'idtrieuchung': 'S22', 'noidung': 'Đau bụng'}

        if (check in list_symptom_of_person):
            print(f'-->Chatbot: {person.name} đang có triệu chứng sốt  - một trong số các triệu chứng của các bệnh về truyền nhiễm.\n Để có chuẩn đoán chính xác, hãy cho tôi biết chi tiết thêm về triệu chứng khác')
            # print('1. Đau họng')
            # print('0. Triệu chứng khác')
            # print('---------------Câu trả lời của bạn---------------')
            # answer = validate.validate_input_number_form(input())
            # # print("Người dùng: Lựa chọn của tôi ", answer)
            # print(f'-->{person.name}: Lựa chọn của tôi {answer}')
            # if (int(answer) < 0 or int(answer) > 1):
            #     print('-->Chatbot: Vui lòng nhập số từ 0 -> 1')
            #     continue
            # elif (answer == '0'):
            #     break
            # else:
            #     list_symptom_of_person.append(Location_StomachAcheSymLst[0])
            # break
        # else:
        #     break
        
        if (check2 in list_symptom_of_person):
            print(f'-->Chatbot: {person.name} đang có triệu chứng Hắt hơi nhiều - một trong số các triệu chứng của các bệnh về hô hấp.\n Để có chuẩn đoán chính xác, hãy cho tôi biết chi tiết thêm về triệu chứng khác')
            # print('1. Ho, ho khan hoặc Ho có đờm')
            # print('0. Triệu chứng khác')
            # print('---------------Câu trả lời của bạn---------------')
            # answer = validate.validate_input_number_form(input())
            # # print("Người dùng: Lựa chọn của tôi ", answer)
            # print(f'-->{person.name}: Lựa chọn của tôi {answer}')
            # if (int(answer) < 0 or int(answer) > 1):
            #     print('-->Chatbot: Vui lòng nhập số từ 0 -> 1')
            #     continue
            # elif (answer == '0'):
            #     break
            # else:
            #     list_symptom_of_person.append(Location_StomachAcheSymLst2[0])
            #     break
        if (check3 in list_symptom_of_person):
            print(f'-->Chatbot: {person.name} đang có triệu chứng Đau bụng  - một trong số các triệu chứng của các bệnh về tiêu hóa.\n Để có chuẩn đoán chính xác, hãy cho tôi biết chi tiết thêm về triệu chứng khác')
            # print('1. Đi ngoài nhiều lần trong ngày')
            # print('0. Triệu chứng khác')
            # print('---------------Câu trả lời của bạn---------------')
            # answer = validate.validate_input_number_form(input())
            # # print("Người dùng: Lựa chọn của tôi ", answer)
            # print(f'-->{person.name}: Lựa chọn của tôi {answer}')
            # if (int(answer) < 0 or int(answer) > 1):
            #     print('-->Chatbot: Vui lòng nhập số từ 0 -> 1')
            #     continue
            # elif (answer == '0'):
            #     break
            # else:
            #     list_symptom_of_person.append(Location_StomachAcheSymLst3[0])
            break
        else:
            break

    print(f'-->Chatbot: Danh sách mã các triệu chứng {person.name} đang mắc:',
          [i['idtrieuchung'] for i in list_symptom_of_person])
    return list_symptom_of_person

###############################################1
# # 4. Câu hỏi thứ 3 đi sâu nhóm bệnh 
def third_question(list_symptom_of_person, person):
    
    # bệnh truyền nhiễm
    Frequency_StomachAcheSymLst = [
      
        db.resulttrieutrung[1],
        db.resulttrieutrung[3],
        db.resulttrieutrung[6],
        db.resulttrieutrung[9],
        db.resulttrieutrung[12],
    ]

    # bệnh hô hấp
    Frequency_StomachAcheSymLst2 = [
      
        db.resulttrieutrung[17],
        db.resulttrieutrung[20],
     
    ]

    # bệnh tiêu hóa
    Frequency_StomachAcheSymLst3 = [
      
        db.resulttrieutrung[22],
        db.resulttrieutrung[24],
  
    ]
    while (1):
        check = {'idtrieuchung': 'S27', 'noidung': 'Sốt'}
        check2 = {'idtrieuchung': 'S17', 'noidung': 'Hắt hơi nhiều'}
        check3 = {'idtrieuchung': 'S22', 'noidung': 'Đau bụng'}

        if (check in list_symptom_of_person):

            print(
                f'-->Chatbot: Tiếp theo tôi muốn biết chi tiết hơn về các triệu chứng của {person.name}. (Lựa chọn bằng cách nhập số thứ tự)')
            count = 1
            for i in Frequency_StomachAcheSymLst:
                if (i not in list_symptom_of_person):
                    print(f'{count}. {i["noidung"]}')
                count += 1
            print('0. Bỏ qua')
            print('---------------------Câu trả lời của bạn---------------------')
            answer = validate.validate_input_number_form(input())
            print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
            if (int(answer) < 0 or int(answer) > len(Frequency_StomachAcheSymLst)):
                print("-->Chatbot: Vui lòng nhập số trong khoảng 0 -> 6")
                continue
            elif (answer == '0'):
                break
            else:
                list_symptom_of_person.append(
                    Frequency_StomachAcheSymLst[int(answer)-1])
                print(
                    f'-->Chatbot: Danh sách mã các triệu chứng {person.name} đang mắc:', [i['idtrieuchung'] for i in list_symptom_of_person])
      
        if (check2 in list_symptom_of_person):
    
            print(
                f'-->Chatbot: Tiếp theo tôi muốn biết chi tiết hơn về các triệu chứng của {person.name}. (Lựa chọn bằng cách nhập số thứ tự)')
            count = 1
            for i in Frequency_StomachAcheSymLst2:
                if (i not in list_symptom_of_person):
                    print(f'{count}. {i["noidung"]}')
                count += 1
            print('0. Bỏ qua')
            print('---------------------Câu trả lời của bạn---------------------')
            answer = validate.validate_input_number_form(input())
            print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
            if (int(answer) < 0 or int(answer) > len(Frequency_StomachAcheSymLst2)):
                print("-->Chatbot: Vui lòng nhập số trong khoảng 0 -> 6")
                continue
            elif (answer == '0'):
                break
            else:
                list_symptom_of_person.append(
                    Frequency_StomachAcheSymLst2[int(answer)-1])
                print(
                    f'-->Chatbot: Danh sách mã các triệu chứng {person.name} đang mắc:', [i['idtrieuchung'] for i in list_symptom_of_person])
        if (check3 in list_symptom_of_person):
    
            print(
                f'-->Chatbot: Tiếp theo tôi muốn biết chi tiết hơn về các triệu chứng của {person.name}. (Lựa chọn bằng cách nhập số thứ tự)')
            count = 1
            for i in Frequency_StomachAcheSymLst3:
                if (i not in list_symptom_of_person):
                    print(f'{count}. {i["noidung"]}')
                count += 1
            print('0. Bỏ qua')
            print('---------------------Câu trả lời của bạn---------------------')
            answer = validate.validate_input_number_form(input())
            print(f'-->{person.name}: Câu trả lời của tôi là {answer}')
            if (int(answer) < 0 or int(answer) > len(Frequency_StomachAcheSymLst3)):
                print("-->Chatbot: Vui lòng nhập số trong khoảng 0 -> 6")
                continue
            elif (answer == '0'):
                break
            else:
                list_symptom_of_person.append(
                    Frequency_StomachAcheSymLst3[int(answer)-1])
                print(
                    f'-->Chatbot: Danh sách mã các triệu chứng {person.name} đang mắc:', [i['idtrieuchung'] for i in list_symptom_of_person])       
        else:
                break         
    return list_symptom_of_person


################################################################
# 5 phần suy diễn tiến
def forward_chaining(rule, fact, goal, file_name,person):
    fc = ForwardChaining(rule, fact, None, file_name)

    list_predicted_disease = [i for i in fc.facts if i[0] == "D"]
    print(
        f'-->Chatbot: Chúng tôi dự đoán {person.name} có thể bị bệnh :', end=" ")
    for i in list_predicted_disease:
        temp = db.get_benh_by_id(i)
        print(temp['tenBenh'], end=', ')
    print()
    
    print(
        f'-->Chatbot: Trên đây là chuẩn đoán sơ bộ của chúng tôi. Tiếp theo, chúng tôi sẽ hỏi {person.name} một số câu hỏi để đưa ra kết quả chính xác.', end=" ")
    return list_predicted_disease

########################################################################
# 6 phần suy diễn lùi
def backward_chaining(luat_lui,list_symptom_of_person,list_predicted_disease,file_name ):
    predictD=list_predicted_disease
    rule=luat_lui
    all_rule=db.gettrieuchung()
    fact_real=list_symptom_of_person_id
    benh=0
    for g in predictD:
        goal=g
        D=db.get_benh_by_id(goal) #Chứa thông tin của bệnh có id == goal
        print(f"Chúng tôi đã có các triệu chứng ban đầu và có thể bạn mắc bệnh {D['tenBenh']}({goal}) , sau đây chúng tôi muốn hỏi bạn một vài câu hỏi để tìm hiểu về bệnh bạn đang mắc phải")
        all_s_in_D=all_rule[goal]
        all_s_in_D=sorted(set(all_s_in_D)-set(fact_real))
        d=searchindexrule(rule,goal)

        b=BackwardChaining(rule,fact_real,goal,file_name) # kết luận trong trường hợp các luât jtruwowsc đã suy ra đk luôn

        if b.result1==True:# đoạn đầu
            print("Bạn mắc bệnh {}- {}và chúng tôi sẽ gửi thêm thông tin về bệnh này cho bạn qua mail".format(goal,D['tenBenh']))
            print(f"Lời khuyên")
            D['loikhuyen']=D['loikhuyen'].replace("/n","\n")
            print(f"{D['loikhuyen']}")
            print("Cám ơn bạn đã sử dụng chat bot của chúng tôi")
            return goal,fact_real
        
        while(len(all_s_in_D)>0):
            s=db.get_trieuchung_by_id(all_s_in_D[0])
            question=f"Bạn có bị triệu chứng {s['noidung']}({all_s_in_D[0]}) không?"
            print(question)
            answer = validate.validate_binary_answer(input())
            
            print(f"answer: {answer}")
            if answer== True :
                fact_real.append(all_s_in_D[0])
                print('cjccccccccccc', fact_real, goal)
                b=BackwardChaining(rule,fact_real,goal,file_name)
           
                list_no_result,lsD=get_s_in_d(all_s_in_D[0],goal,rule,d,1)
       
                d=sorted(set(d)-set(lsD))
                print('d la abc', d)
                all_s_in_D=sorted(set(list_no_result)-set(fact_real))
                if b.result1==True:
                    benh=1
                    break
            if answer==False :
                list_no_result,lsD=get_s_in_d(all_s_in_D[0],goal,rule,d,0) #S01 S02 S03 S04 S05
                d=sorted(set(d)-set(lsD))
                all_s_in_D=sorted(set(list_no_result)-set(fact_real))
            if len(d)==0: 
                print(f"Có vẻ như bạn không mắc bệnh {goal}-{D['tenBenh']}")
                break
        if benh==1:
            print("Bạn mắc bệnh {}- {} , và chúng tôi sẽ gửi thêm thông tin về bệnh này cho bạn qua mail".format(goal,D['tenBenh']))
            print(f"Lời khuyên")
            D['loikhuyen']=D['loikhuyen'].replace("/n","\n")
            print(f"{D['loikhuyen']}")
            print("Cám ơn bạn đã sử dụng chat bot của chúng tôi")
            
            return goal,fact_real
            break
    if benh==0:
        print(f"Bạn không bị bệnh nào cả")
        return None, fact_real
2
#########################################################################
#7 Gửi thông tin qua email
def send_email(list_symptom_of_person_id,id_benh,person):
    email_sender = 'duc02092002123@gmail.com'
    email_password = 'wvud qdnp ycxt gvau'
    email_receiver = person.email
    print(email_receiver)

    benh=db.get_benh_by_id(id_benh)
    # print(benh)
    nguyen_nhan=benh['nguyennhan']
    loi_khuyen=benh['loikhuyen']
    subject='Medical records'
    body=f"""
        ***Xin chào {person.name}
        ***Chúng tôi nhận được các triệu chứng bạn đã gặp phải là : 
        {[db.get_trieuchung_by_id(i)["noidung"] for i in list_symptom_of_person_id]}
        ***Chúng tôi dự đoán bạn bị bệnh : {benh['tenBenh']}
        ***Nguyên nhân gây ra bệnh này là: 
        {nguyen_nhan}
        ***Lời khuyên của chúng tôi dành cho bạn:
        {loi_khuyen}
        ***Cám ơn vì đã dùng Chatbot
    """
    print(body)
    
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp: 
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
    except:
        print("email không tồn tại")
   

person = welcome_question()
list_symptom_of_person = []  # list các đối tượng triệu chứng

'''
person = Person("None",  "10564165465","huyreeve@gmail.com")
'''
list_symptom_of_person = first_question(list_symptom_of_person, person)
print([i['idtrieuchung'] for i in list_symptom_of_person])  # list các đối tượng

list_symptom_of_person = second_question(list_symptom_of_person, person)


list_symptom_of_person = third_question(list_symptom_of_person, person)
print([i['idtrieuchung'] for i in list_symptom_of_person])



list_symptom_of_person_id = [i['idtrieuchung'] for i in list_symptom_of_person]
list_symptom_of_person_id = list(set(list_symptom_of_person_id))
list_symptom_of_person_id.sort()

list_predicted_disease = forward_chaining(luat_tien, list_symptom_of_person_id, None, 'ex', person)
print(list_predicted_disease)


if len(list_predicted_disease)==0 :
    print("Bạn không có dấu hiệu cảu bệnh nào cả.Cám ơn bạn đã sử dụng ChatBot")
    sys.exit()

'''list_predicted_disease=['D01','D02','D03']
list_symptom_of_person_id=['S01','S02','S04','S09']'''
disease,list_symptom_of_person_id= backward_chaining(luat_lui,list_symptom_of_person_id,list_predicted_disease,"ex")


'''list_symptom_of_person_id= ['S01','S02']
disease="D01"
person = Person("None",  "10564165465","huyreeve@gmail.com")'''

if(disease != None):
    send_email(list_symptom_of_person_id,disease,person)





