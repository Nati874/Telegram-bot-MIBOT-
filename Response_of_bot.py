greet_list=['hi','hey','hello','good morning','good evening','good afternoon','sup','what\'s up']
help_list=['what is this bot','help','what should i do with this bot','what is your use']
info_list=['what are you','who are you']
thank_list=["tnx","tysm","ty","10q","thanks", "thank you", "thanks for your help", "thank you very much","thanks very much", "thank you so much", "thanks for you help", "thanks so much", "appreciated"]
tip_list=['prefixes and suffixes are usually short so you can easliy distinguish them','if you see a medical term written as "-word", this means it is a suffix and "word-" is for preffix','Medical terms are usually derived from Latin and Greek words. Therefore studying basic word in Greek may improve your skills','Terms are very important in Biology, but the opposite is also true. so focus on biology']
MT_dict={
 'abrasion': 'A cut or scrape that typically isn\'t serious.',
 'abscess': 'A tender, fluid-filled pocket that forms in tissue, usually due to infection.',
 'acute': 'Signifies a condition that begins abruptly and is sometimes severe, but the duration is short.',
 'benign': 'Not cancerous.',
 'biopsy': 'A small sample of tissue that is taken for testing.',
 'chronic': 'Signifies a recurring, persistent condition like heart disease.',
 'contusion': 'A bruise.',
 'defibrillator': 'A medical device that uses electric shocks to restore normal heartbeat.',
 'edema': 'Swelling caused by fluid accumulation.',
 'embolism': 'An arterial blockage, often caused by a blood clot.',
 'epidermis': 'The outer layer of the skin.',
 'fracture': 'Broken bone or cartilage.',
 'gland': 'An organ or tissue that produces and secretes fluids that serve a specific function.',
 'hypertension': 'High blood pressure.',
 'inpatient': 'A patient who requires hospitalization.',
 'intravenous': 'Indicates medication or fluid that\'s delivered by vein.',
 'malignant': 'Indicates the presence of cancerous cells.',
 'outpatient': 'A patient who receives care without being admitted to a hospital.',
 'prognosis': 'The predicated outcome of disease progression and treatment.',
 'relapse': 'Return of disease or symptoms after a patient has recovered.',
 'sutures': 'Stitches, which are used to join tissues together as they heal.',
 'transplant': 'The removal of an organ or tissue from one body that is implanted into another.',
 'vaccine': 'A substance that stimulates antibody production to provide immunity against disease.',
 'zoonotic disease': 'A disease that is transmissible from animals to humans.',
 'an': 'Lack of or without.',
 'ation': 'Indicates a process.',
 'dys': 'Abnormal, difficult, or painful.',
 'ectomy': 'Surgical removal of something.',
 'ismus': 'Indicates a spasm or contraction.',
 'itis': 'Signifies inflammation.',
 'lysis': 'Decomposition, destruction, or breaking down.',
 'macro': 'Large in size.',
 'melan': 'Black or dark in color.',
 'micro': 'Small in size.',
 'ology': 'The study of a particular concentration.',
 'osis': 'Indicates something that is abnormal.',
 'otomy': 'To cut into.',
 'pathy': 'Disease or disease process.',
 'plasty': 'Surgical repair.',
 'poly': 'Many.',
 'pseudo': 'False or deceptive, usually in regard to appearance.',
 'retro': 'Behind or backward.',
 'cardio': 'Related to the heart.',
 'dermato': 'Pertaining to the skin.',
 'encephal': 'Related to the brain.',
 'gastro': 'Related to the stomach.',
 'hemato': 'Pertaining to blood.',
 'myo': 'Related to muscle.',
 'osteo': 'Related to bone.',
 'pulmono': 'Refers to the lungs.',
 'rhino': 'Related to the nose.',
 'sclerosis': 'Hard or hardening.',
 'stasis': 'Slowing or stopping the flow of a bodily fluid.',
 'thermo': 'Indicates heat.',
 'abdomen': 'The tummy area from the lower ribs to the pelvis.',
 'abdominal': 'Of the abdomen.',
 'abortion': 'Ending a pregnancy using either medicines (medical abortion) or an operation (surgical abortion).',
 'adenomyosis': 'Endometriosis in the muscle wall of the uterus.',
 'adhesions': 'Scars that connects two or more body structures together.',
 'amniocentesis': 'A way of testing the fluid surrounding a baby in the womb by taking a small sample with a needle put into the womb through the abdomen.',
 'amniotic fluid': 'The watery liquid surrounding and protecting the growing fetus in the uterus.',
 'amniotic sac': 'The pregnancy sac containing the baby and the amniotic fluid. It is sometimes also called "the membranes".',
 'anaemia':	'A condition when the level of haemoglobin, the protein in blood which carries oxygen round the body, is lower than normal.',
 'anaesthesia': 'A medical way of relieving pain.',
 'anaesthetist': 'A doctor trained to administer anaesthetics.',
 'anal sphincter': 'The muscle around the anus that is squeezed to prevent passing wind or opening the bowels involuntarily.',
 'anaphylaxis':	'Anaphylaxis is a severe and potentially life-threatening allergic reaction that needs immediate treatment.',
 'antiphospholipid syndrome' :'A condition caused by your immune system mistakenly attacking healthy cells in your body.',
 'antenatal': 'Before birth.',
 'anthracyclines':	'Antibiotic drugs used in cancer chemotherapy.',
 'antibiotics':	'Medicines to fight an infection caused by bacteria.',
 'antibody': 'Blood protein that helps fight attacks on the immune system.',
 'anticoagulant': 'medication	Medicines to reduce clotting in the blood vessels.',
 'anti-D': 'See RhD antigen.',
 'antigen':	'A substance in the blood that helps trigger the immune system to develop antibodies. See blood group.',
 'bacteria': 'Tiny organisms that may cause certain infections.',
 'virus': 'A micro-organism which invades living cells in order to grow or reproduce.',
 'aneurysm' : 'A bulge in the wall of an artery that weakens the artery and can lead to rupture.',
 'aortic dissection': 'A tear in the inner layer of the aorta.',
 'bradycardia': 'A slowing of the heart ratetypically less than 60 beats per minute for adults.',
 'cyanosis': 'Condition resulting bluish skin, stems from lack of oxygen in the blood.',
 'diagnosis': 'Identification of a condition, disease or disorder by evaluation of symptoms, tests and other factors.',
 'thrombosis': 'A blood clot within a blood vessel that affects normal blood flow.',
 'embolus': 'A blood clot, air bubble or other obstruction blocking blood flow in the affected blood vessel.',
 'atrial fibrillation': 'An uncoordinated, quivering movement of the heart muscle resulting in an irregular pulse and poor blood flow.',
 'hypotension': 'Abnormally low blood pressure.',
 'ischemia': 'Characterized by a lack of blood flow to an organ or part of the body. Often refers to the heart-cardiac ischemia.',
 'cancer': 'Collection of related diseases where some of the body’s cells multiply out of control spreading into surrounding tissues and interfering with normal body function.',
 'normal sinus rhythm': 'A normal heartbeat pattern, usually is between 60 and 80 beats per minute in an adult.',
 'tumor': 'A swelling or mass, often used in relation to cancer.',
 'tension pneumothorax': 'A collapsed lung that occurs when air leaks into the space between the lungs and the chest wall.',
 'pericardial effusion': 'Blood or fluid leaking into the pericardium, the sac surrounding the heart.',
 'myocardial infarction': 'When an arterial blockage or slow blood flow deprives the heart of blood. Known more commonly as a heart attack.',
 'angina': 'A disease in which narrowing of the arteries supplying the heart results in reduced blood flow and chest pain. Usually a symptom of coronary artery disease.',
 'cerebrovascular accident': 'Commonly called a stroke. Occurs when the brain is deprived of blood and oxygen by either a blockage or the rupture of a blood vessel.',
 'sepsis': 'A serious condition caused the body’s response to severe infection. Occurs when the body’s infection-fighting response gets out of balance and can lead to severe isses like organ failure.',
'5-alpha reductase': 'A chemical that changes the sex hormone testosterone into a substance called dihydrotestosterone. This hormone can cause the prostate gland to grow abnormally.',
'abdominal muscles': 'A flat sheet of muscles on the front of the abdomen, between the ribcage and the pelvis.',
'abdominoplasty': 'A procedure to remove excess abdominal skin and tighten the underlying stomach muscles. Also known as a tummy tuck.',
'abduction': 'Movement of a body part, such as an arm or leg, away from the center of the body.',
'ablation': 'A form of treatment that uses electrical energy, heat, cold, alcohol, or other modalities to destroy a small section of damaged tissue.',
'arteriosclerosis': 'A term encompassing a variety of conditions in which artery walls thicken and become less flexible. Sometimes called hardening of the arteries. Arteriosclerosis occurs when cholesterol-rich plaque forms on the inner lining of arteries (atherosclerosis), when artery walls become calcified, or when high blood pressure thickens the muscular wall of arteries.',
'artery': 'A blood vessel that carries blood away from the heart and to various parts of the body.',
'aspiration': 'Breathing in a foreign object. Also, the process of suctioning fluid, tissue, or other substances from the body.',
'aspirin': 'A drug that relieves pain, fever, and swelling, and inhibits the formation of blood clots.',
'atheroma': 'An abnormal build-up of fatty plaque inside an artery.',
'atherosclerosis': 'The buildup of fatty deposits (plaque) in the walls of arteries, causing narrowing and reduced blood flow; the disease responsible for most heart attacks and many strokes.',
'ATP': 'Abbreviation for adenosine triphosphate, an energy-storing molecule that is found in all human cells.',
'auditory nerve': 'A nerve in the inner ear that transmits information about sound to the brain.',
'autonomic nervous system': 'The part of the nervous system that controls involuntary actions, such as blood pressure or breathing. It also plays an important role in the fight or flight response to danger.',
'autopsy': 'Surgically opening and examining a body after death to see if any diseases are present and to determine the cause of death.',
'axillary': 'The armpit.',
'axis': 'The second vertebra of the neck (from the skull); also called the C-2 vertebra.',
'axon': 'The long, slender extension of a nerve cell that conducts electrical impulses away from the nerve\'s cell body and on to nearby nerves.',                                                                                                                                                        
'axon terminal': 'The end of an axon.'

}
NoR=''''''
RoW=''''''
Words=''''''

tips_num=len(tip_list)



Key_terms=list(MT_dict.keys())
k=int(len(Key_terms))


Pre_Suf=Key_terms[24:42]
Root_word=Key_terms[:24]+Key_terms[42:k]
Pre_Suf.sort()
Root_word.sort()
Key_terms.sort()

for i in range(len(Pre_Suf)):
    NoR=NoR+str(Pre_Suf[i])
    NoR=NoR+'''
'''
for i in range(len(Root_word)):
    RoW=RoW+str(Root_word[i])
    RoW=RoW+'''
'''
for i in range(len(Key_terms)):
    Words=Words+str(Key_terms[i])
    Words=Words+'''
'''
def greet(input_text):
    message=str(input_text).lower()
    if message in greet_list:
        return "Hi this is a medical term information bot"
    elif message in help_list:
        return """
        With this bot you can know the Medical terms for as biological purposes.
        """
    elif message in info_list:
        return "HI my name is MIBOT, and I am a Medical Term Information Bot. Nice to meet you :)"
    elif message in thank_list:
        return "I am happy to help"
    elif message in Key_terms:
        return MT_dict[message]
    else:
        return 'I didn\'t understand what you said'
