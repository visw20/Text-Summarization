# from transformers import BartForConditionalGeneration, BartTokenizer

# # Load pre-trained model and tokenizer
# model_name ='facebook/bart-large-cnn'
# model = BartForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

# while True:
#   # Get user input
#   text = input("Enter text to be summarized (or 'q' to quit): ")

#   # Check for quit command
#   if text.lower() == 'q':
#     break

#   # Summarize text
#   inputs = tokenizer(text, max_length=1024, return_tensors='pt', truncation=True)
#   summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
#   summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#   # Print summary
#   print(summary)

#   # Ask to continue
#   continue_summarizing = input("Summarize another text (y/n)? ")
#   if continue_summarizing.lower() != 'y':
#     break

# print("Summary generation stopped.")




# from transformers import BartForConditionalGeneration, BartTokenizer

# # Load pre-trained model and tokenizer
# model_name = 'facebook/bart-large-cnn'
# model = BartForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

# while True:
#     # Get user input
#     text = input("Enter text to be summarized (or 'q' to quit): ")

#     # Check for quit command
#     if text.lower() == 'q':
#         break

#     # Print input text with label
#     print("\nInput Text:\n" + text)

#     # Summarize text
#     inputs = tokenizer(text, max_length=1024, return_tensors='pt', truncation=True)
#     summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=500, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     # Print summary with label
#     print("\nSummary:\n" + summary)

#     # Ask to continue
#     continue_summarizing = input("\nSummarize another text (y/n)? ")
#     if continue_summarizing.lower() != 'y':
#         break

# print("Summary generation stopped.")









# import tkinter as tk
# from tkinter import scrolledtext
# from transformers import BartForConditionalGeneration, BartTokenizer

# # Load pre-trained model and tokenizer
# model_name = 'facebook/bart-large-cnn'
# model = BartForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

# # Function to summarize the text from the input box
# def summarize_text():
#     # Get text from input box
#     text = input_text.get("1.0", tk.END).strip()

#     if text:
#         # Summarize text
#         inputs = tokenizer(text, max_length=1024, return_tensors='pt', truncation=True)
#         summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
#         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#         # Display the summary in the output box
#         output_text.config(state=tk.NORMAL)  # Enable editing in the output box
#         output_text.delete("1.0", tk.END)  # Clear previous content
#         output_text.insert(tk.END, summary)  # Insert the summary
#         output_text.config(state=tk.DISABLED)  # Disable editing after inserting

# # Function to clear both input and output boxes
# def clear_text():
#     input_text.delete("1.0", tk.END)
#     output_text.config(state=tk.NORMAL)
#     output_text.delete("1.0", tk.END)
#     output_text.config(state=tk.DISABLED)

# # Create the main window
# window = tk.Tk()
# window.title("Text Summarization using BART")
# window.geometry("800x600")

# # Label for the input text
# input_label = tk.Label(window, text="Enter text to summarize:")
# input_label.pack(pady=10)

# # Input text box (scrolled text area)
# input_text = scrolledtext.ScrolledText(window, height=10, width=80, wrap=tk.WORD)
# input_text.pack(pady=10)

# # Summarize button
# summarize_button = tk.Button(window, text="Summarize", command=summarize_text)
# summarize_button.pack(pady=10)

# # Label for the output summary
# output_label = tk.Label(window, text="Summary:")
# output_label.pack(pady=10)

# # Output text box (scrolled text area, disabled for editing)
# output_text = scrolledtext.ScrolledText(window, height=10, width=80, wrap=tk.WORD)
# output_text.config(state=tk.DISABLED)
# output_text.pack(pady=10)

# # Clear button to reset input and output
# clear_button = tk.Button(window, text="Clear", command=clear_text)
# clear_button.pack(pady=10)

# # Start the Tkinter event loop
# window.mainloop()





#using flask

# from flask import Flask, render_template, request
# from transformers import BartForConditionalGeneration, BartTokenizer

# # Initialize the Flask app
# app = Flask(__name__)

# # Load the pre-trained model and tokenizer
# model_name = 'facebook/bart-large-cnn'
# model = BartForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

# # Route for the home page where the form is displayed
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     summary = ""
#     if request.method == 'POST':
#         # Get user input from form
#         text = request.form['input_text']
        
#         # Process and summarize the input text
#         inputs = tokenizer(text, max_length=1024, return_tensors='pt', truncation=True)
#         summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
#         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     # Render the HTML template and pass the summary result
#     return render_template('index.html', summary=summary)

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=False, use_reloader=False)



# from transformers import BartForConditionalGeneration, BartTokenizer

# def summarize_text(text, max_length=1000, min_length=900, length_penalty=2.0, num_beams=4):
#     # Load the BART tokenizer and model
#     model_name = "facebook/bart-large-cnn"
#     tokenizer = BartTokenizer.from_pretrained(model_name)
#     model = BartForConditionalGeneration.from_pretrained(model_name)
    
#     # Encode the input text
#     inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    
#     # Generate summary
#     summary_ids = model.generate(
#         inputs, 
#         max_length=max_length, 
#         min_length=min_length, 
#         length_penalty=length_penalty, 
#         num_beams=num_beams, 
#         early_stopping=True
#     )
    
#     # Decode and return the summary
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# # Example usage
# if __name__ == "__main__":
#     text = """
#     Mahendra Singh Dhoni, often called MS Dhoni or "Captain Cool," is one of the most iconic cricketers India has ever produced. Known for his calm demeanor, brilliant leadership, and extraordinary finishing abilities, Dhoni’s journey from a small-town boy in Ranchi to becoming one of the most celebrated cricketers in the world is nothing short of inspiring. His story transcends cricket, embodying resilience, humility, and the belief that dreams, no matter how big, can be achieved with determination and hard work.

# Early Life and Background
# Mahendra Singh Dhoni was born on July 7, 1981, in Ranchi, then part of Bihar and now in Jharkhand. His father, Pan Singh, worked for MECON, a public-sector enterprise, while his mother, Devaki Devi, was a homemaker. Dhoni's early years were far removed from the glamorous cricket stadiums where he would later achieve greatness. Instead, his playgrounds were the dusty fields of Ranchi, where he honed his skills playing gully cricket.

# Interestingly, Dhoni initially aspired to become a football goalkeeper. His skills under the bar were so impressive that his school coach suggested he try wicketkeeping. This decision changed the course of Indian cricket forever. Dhoni began playing for local clubs and soon caught the eye of selectors with his unorthodox style and raw talent.

# Domestic Cricket and Struggles
# Dhoni’s journey to the national team was not easy. He began his domestic cricket career with the Bihar cricket team in the Ranji Trophy during the 1999–2000 season. Despite his consistent performances, his efforts went largely unnoticed due to the lack of visibility for players from smaller states.

# In 2003, Dhoni was selected for the India A team, where he showcased his big-hitting ability during a tour to Kenya. His performances in the tri-series against Kenya and Pakistan caught the attention of then-BCCI President Sourav Ganguly and selectors like Dilip Vengsarkar.

# Debut and Rise to Stardom
# Dhoni made his ODI debut against Bangladesh in December 2004. However, it was an unremarkable start as he was run out for a duck. But Dhoni’s career-defining moment came in April 2005 against Pakistan in Visakhapatnam, where he scored a blistering 148 off 123 balls. This innings not only cemented his place in the team but also established him as a future star.

# In 2007, Dhoni was handed the captaincy of the Indian T20 team for the inaugural ICC T20 World Cup. Under his leadership, India clinched the title, defeating Pakistan in a thrilling final. This victory marked the beginning of Dhoni's illustrious captaincy career.

# Captaincy Era
# Transforming Indian Cricket
# Dhoni’s appointment as the captain of the ODI and Test teams after the T20 World Cup win heralded a new era in Indian cricket. His calmness under pressure and unconventional decision-making became his trademarks. Dhoni led by example, instilling confidence in his teammates and backing young talent.

# One of his early successes as captain came in 2008 when India won the Commonwealth Bank Series in Australia. The series win was a testament to his tactical acumen and ability to outthink opponents.

# ICC Cricket World Cup 2011
# The pinnacle of Dhoni’s career came on April 2, 2011, when India won the ICC Cricket World Cup after 28 years. Dhoni’s unbeaten 91 in the final against Sri Lanka, capped with a towering six to seal the victory, is etched in the memory of every Indian cricket fan. His calm and calculated approach during the chase demonstrated why he was the ideal leader for such a momentous occasion.

# Champions Trophy 2013
# Dhoni further solidified his legacy by leading India to victory in the 2013 ICC Champions Trophy in England. With this win, Dhoni became the only captain in history to win all three ICC trophies—T20 World Cup, ODI World Cup, and Champions Trophy.

# Playing Style
# Dhoni's batting style was a blend of power, innovation, and adaptability. He was known for his ability to finish matches, often taking games deep and keeping cool under pressure. His signature helicopter shot, a result of his strong wrists and unconventional technique, became famous worldwide.

# As a wicketkeeper, Dhoni was among the best in the world. His lightning-fast stumpings and sharp reflexes behind the stumps set him apart. He also revolutionized wicketkeeping with his unique style of effecting run-outs and stumpings.

# Indian Premier League (IPL) Legacy
# Dhoni's association with the Chennai Super Kings (CSK) in the IPL added another glorious chapter to his career. Under his captaincy, CSK became one of the most successful franchises, winning multiple IPL titles (2010, 2011, 2018, 2021, and 2023). His bond with the CSK fans earned him the nickname "Thala" (leader) in Tamil Nadu, showcasing his ability to connect with people beyond cricket.

# Challenges and Criticism
# Despite his successes, Dhoni faced his share of challenges and criticism. His decision to back certain players despite their inconsistent performances and his defensive strategies in Test matches occasionally drew flak. However, Dhoni always stood by his choices, emphasizing the importance of trust and belief in his teammates.

# Dhoni retired from Test cricket in December 2014, citing the need to manage his workload. He later stepped down as captain of the ODI and T20I teams in 2017, passing the baton to Virat Kohli. However, he continued to play as a player, contributing with his experience and mentorship.

# Retirement and Legacy
# On August 15, 2020, Dhoni announced his retirement from international cricket through an Instagram post, marking the end of an era. Despite his retirement, Dhoni's influence on Indian cricket remains unparalleled. He inspired a generation of cricketers from small towns, breaking the notion that only players from metropolitan cities could succeed on the international stage.

# Beyond Cricket
# Dhoni’s interests extend beyond cricket. He is a co-owner of various sports teams, including the Chennaiyin FC football team in the Indian Super League and the Ranchi Rays hockey team. He is also an avid motorbike enthusiast and owns a vast collection of superbikes.

# Known for his humility, Dhoni continues to be a role model for millions. His grounded nature, even after achieving immense success, sets him apart from many sports personalities.

# Conclusion
# MS Dhoni’s journey is a testament to what can be achieved with hard work, self-belief, and perseverance. He not only transformed Indian cricket but also left a legacy that will inspire generations to come. As a cricketer, leader, and human being, Dhoni will always be remembered as one of the greatest icons in the history of the sport.
#     """
    
#     summarized_text = summarize_text(text)
#     #print("Original Text:\n", text)
#     print("\nSummarized Text:\n", summarized_text)









#glove text summarization


# import numpy as np
# import nltk
# from gensim.models import KeyedVectors
# from nltk.tokenize import sent_tokenize, word_tokenize
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.cluster import KMeans

# # Ensure nltk data is downloaded
# nltk.download("punkt")

# import os
# os.environ["OMP_NUM_THREADS"] = "1" 

# # Load pre-trained GloVe embeddings
# def load_glove_model(file_path):
#     embeddings = {}
#     with open(file_path, 'r', encoding="utf-8") as f:
#         for line in f:
#             parts = line.strip().split()
#             word = parts[0]
#             try:
#                 vector = np.array(parts[1:], dtype=np.float32)
#                 embeddings[word] = vector
#             except ValueError:
#                 # Skip lines with errors
#                 print(f"Skipping line: {line}")
#     return embeddings


# # Compute sentence embeddings using average of word embeddings
# def sentence_embedding(sentence, embeddings):
#     words = word_tokenize(sentence)
#     word_vectors = [embeddings[word] for word in words if word in embeddings]
#     if word_vectors:
#         return np.mean(word_vectors, axis=0)
#     else:
#         return np.zeros(300)  # Assuming embedding size is 300

# # Summarize text by selecting representative sentences
# def summarize_text(text, embeddings, num_sentences=3):
#     sentences = sent_tokenize(text)
#     sentence_vectors = [sentence_embedding(sent, embeddings) for sent in sentences]
    
#     # Perform clustering
#     sentence_vectors = np.array(sentence_vectors)
#     kmeans = KMeans(n_clusters=num_sentences, random_state=42)
#     kmeans.fit(sentence_vectors)
#     cluster_centers = kmeans.cluster_centers_
    
#     # Find representative sentences
#     summary = []
#     for center in cluster_centers:
#         similarities = cosine_similarity([center], sentence_vectors)
#         top_indices = np.argsort(similarities[0])[-3:]  # Select top 3 sentences
#         for idx in top_indices:
#             summary.append(sentences[idx])

#     return " ".join(summary)

# # Main script
# if __name__ == "__main__":
#     # Load GloVe embeddings
#     glove_file_path = "C:\All project\models\glove.42B.300d\glove.42B.300d.txt"  # Change to your GloVe file path
#     glove_embeddings = load_glove_model(glove_file_path)
    
#     # Example text
#     text = """
# Shri Narendra Modi was sworn-in as India’s Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 Parliamentary elections. This victory marked the third consecutive term for Shri Modi, further solidifying his leadership.

# The 2024 elections saw a remarkable voter turnout, with a significant portion of the electorate showing continued confidence in Shri Modi’s leadership and vision for the country. His campaign focused on a blend of economic development, national security, and social welfare programs, which resonated widely with the populace.

# Shri Modi’s third term is expected to build on the foundations laid during his previous tenures, with a renewed emphasis on technological innovation, infrastructure development, and international diplomacy, further positioning India as a global powerhouse. The unprecedented third term underscores Shri Modi’s enduring appeal and the trust placed in him by millions of Indians to lead the nation towards greater prosperity and stability.

# The first ever Prime Minister to be born after Independence, Shri Modi has previously served as the Prime Minister of India from 2014 to 2019, and from 2019 to 2024. He also has the distinction of being the longest serving Chief Minister of Gujarat with his term spanning from October 2001 to May 2014.

# In the 2014 and 2019 Parliamentary elections, Shri Modi led the Bharatiya Janata Party to record wins, securing absolute majority on both occasions. The last time that a political party secured such an absolute majority was in the elections of 1984.

# Inspired by the motto of ‘SabkaSaath, Sabka Vikas, Sabka Vishwas’, Shri Modi has ushered in a paradigm shift in governance that has led to inclusive, development-oriented and corruption-free governance. The Prime Minister has worked with speed and scale to realise the aim of Antyodaya, or ensuring last-mile delivery of schemes and services.

# Leading international agencies have noted that under the leadership of PM Narendra Modi, India has been eliminating poverty at record pace. According to the findings from NITI Aayog’s latest report ‘Multidimensional Poverty in India since 2005-06’, almost 25 crore people escaped multidimensional poverty in last nine years. The credit for this remarkable achievement goes to significant initiatives of the government to address all dimensions of poverty.

# Today, India is home to the world’s largest healthcare programme, Ayushman Bharat. Covering over 50 crore Indians, Ayushman Bharat provides top quality and affordable healthcare to the poor and neo-middle class.

# The Lancet, considered among the most prestigious health journals in the world has lauded Ayushman Bharat, stating that this scheme attends to the larger discontent about the health sector in India. The journal also noted PM Modi’s efforts to prioritise universal health coverage.

# Understanding that financial exclusion was a bane for the poor, the Prime Minister launched the Pradhan Mantri Jan Dhan Yojana, that aimed at opening bank accounts for every Indian. Now, over 51 crore Jan Dhan accounts have been opened. These accounts have not only banked the unbanked but also opened the doors for other avenues of empowerment.

# Going a step ahead of Jan Dhan, Shri Modi emphasised on Jan Suraksha, by giving insurance and pension cover to the most vulnerable sections of society. The JAM trinity (Jan Dhan- Aadhaar- Mobile) has led to elimination of middle men and ensured transparency and speed, powered by technology.

# The Pradhan Mantri Ujjwala Yojana, launched in 2016 provides free cooking gas connections to the poor. It has proven to be a major game-changer in providing smoke-free kitchens to over 10 crore beneficiaries, most of whom are women.

# 18,000 villages that were without electricity even after 70 long years of Independence have been electrified.

# Shri Modi believes that no Indian should be homeless and to realise this vision, over 4.2 crore houses were sanctionedunder the PM Awas Yojana between 2014 and 2024. In June 2024, after assuming office for the third term, one of the first decisions of the Cabinet was to assist 3 crore additional rural and urban households for the construction of houses, underscoring Shri Narendra Modi’s commitment to addressing the nation’s housing needs and ensuring dignity and a quality life for every citizen.

# Agriculture is a sector that is very close to Shri Narendra Modi. During the interim budget of 2019, the Government announced a monetary incentive for farmers called the PM Kisan Samman Nidhi. In almost three weeks, on 24th February 2019, the scheme was launched and instalments have been paid regularly since then. During the first Cabinet Meeting of PM Modi’s second term, it was decided to extend the PM Kisan benefits to all farmers, removing the 5 acre limit that was present earlier. As of June 2024, Shri Modi released the 17thinstalment of the PM-KISAN scheme at Varanasi in which more than 9.2 crore farmers received the benefits amounting to over Rs.20,000 crore.

# Shri Modi has also focused path-breaking initiatives for agriculture ranging from Soil Health Cards, E-NAM for better markets and a renewed focus on irrigation. On 30th May 2019, PM Modi fulfilled a major promise by creating a new Jal Shakti Ministry to cater to all aspects relating to water resources.

# On 2nd October 2014, Mahatma Gandhi’s Birth Anniversary, the PM launched ‘Swachh Bharat Mission’ a mass movement for cleanliness across the nation. The scale and impact of the movement is historic. Today, sanitation coverage has risen from 38% in 2014 to 100% in 2019. All states and Union Territories have been declared open defecation free (ODF). Substantive measures been taken for a clean Ganga.

# The World Health Organisation has appreciated the Swachh Bharat Mission and has opined that it would save three lakh lives.

# Shri Modi believes that transportation is an important means towards transformation. That is why, the Government of India has been working to create next-generation infrastructure be it in terms of more highways, railways, i-ways and waterways. The UDAN (UdeDesh Ka Aam Nagrik) Scheme has made aviation sector more people-friendly and boosted connectivity.

# PM Modi launched the ‘Make in India’ initiative to turn India into an international manufacturing powerhouse. This effort has led to transformative results. India has made significant strides in ‘Ease of Doing Business’, improving its ranking from 142 in 2014 to 63 in 2019. The Government of India rolled out the GST during a historic session of Parliament in 2017, which has realised the dream of ‘One Nation, One Tax.’

# During his tenure, special attention has been paid to India’s rich history and culture. India is home to the world’s largest statue, the State of Unity, a fitting tribute to Sardar Patel. This Statue was built through a special mass movement where tools of farmers and soil from all states and Union Territories of India were used, signifying the spirit of ‘Ek Bharat, Shreshtha Bharat.’

# PM Modi is deeply passionate about environmental causes. He has time and again called for closing of ranks to create a clean and green planet. As Chief Minister of Gujarat, Shri Modi created a separate Climate Change Department to create innovative solutions to climate change. This spirit was seen in the 2015 COP21 Summit in Paris where PM Modi played a key role in the high-level deliberations.

# Going a step ahead of climate change, PM Modi has talked about climate justice. In 2018, Heads of State and Government from several nations came to India for the launch of the International Solar Alliance, an innovative effort to harness solar energy for a better planet.

# Recognising his efforts towards environmental conservation, PM Modi was honoured with the United Nations ‘Champions of the Earth Award.’

# Fully sensitive to the fact that climate change has made our planet prone to natural disasters, Shri Modi has brought a new approach to disaster management, harnessing the power of technology and the strength of human resources. As Chief Minister, he transformed Gujarat that had just been ravaged by a devastating earthquake on 26th January 2001. Likewise, he introduced new systems to combat floods and droughts in Gujarat that were internationally lauded.

# Through administrative reforms, Shri Modi has always given priority to justice for citizens. In Gujarat, he spearheaded the start of evening courts to ensure people’s issues are resolved. At the Centre, he began PRAGATI ((Pro-Active Governance And Timely Implementation) to expedite pending projects that were delaying growth.

# Shri Modi’s foreign policy initiatives have realised the true potential and role of world’s largest democracy. He began his first term in office in presence of all Heads of States of SAARC Nations and invited BIMSTEC leaders at the start of the second. His address to the General Assembly of United Nations was appreciated across the world. Shri Modi became the first Indian Prime Minister to embark on a bilateral visit to Nepal after a long period of 17 years, to Australia after 28 years, to Fiji after 31 years and UAE as well as Seychelles after 34 years. Since taking over, Shri Modi attended UN, BRICS, SAARC and G-20 Summits, where India’s interventions and views on a variety of global economic and political issues were widely appreciated.

# PM Modi has been conferred various honours including the highest civilian honour of Saudi Arabia Sash of King Abdulaziz. Shri Modi has been also been conferred the top awards of Russia (The Order of the Holy Apostle Andrew the First), Palestine (Grand Collar of the State of Palestine), Afghanistan (Amir Amanullah Khan Award), UAE (Order of Zayed Award), Maldives (Rule of Nishan Izzuddeen), Bahrain (King Hamad Order of the Renaissance), Bhutan (Order of the Druk Gyalpo), Papua New Guinea (Grand Companion of the Order of Logohu), Fiji (Companion of the Order of Fiji), Egypt (Order of Nile), France (Grand Cross of the Legion of Honour), and Greece (The Grand Cross of the Order of Honour). In 2018, PM received the prestigious Seoul Peace Prize for his contribution to peace and development.He has also received the Global Goalkeeper’ Award by Bill and Melinda Gates Foundation, and Global Energy and Environment Leadership Award by Cambridge Energy Research Associates.

# Narendra Modi’s clarion call for marking a day as ‘International Day of Yoga’ received an overwhelming response at the UN. In a first, a total of 177 Nations across the world came together and passed the resolution to declare 21st June as the ‘International Day of Yoga at the UN.’

# Shri Modi was born on 17 September, 1950, in a small town in Gujarat. His family belonged to the ‘other backward class’ which is among the marginalised sections of society. He grew up in a poor but loving family ‘without a spare rupee’. The initial hardships of life not only taught the value of hard work but also exposed him to the avoidable sufferings of the common people. This inspired him from a very young age to immerse himself in service of people and the nation. In his initial years, he worked with the Rashtriya Swayamsevak Sangh (RSS), a nationalist organisation devoted to nation building and later devoted himself in politics working with the Bharatiya Janata Party organization at National and State level. Shri Modi completed his MA in political science from Gujarat University.

# Narendra Modi is a ‘People’s Leader’, dedicated to solving their problems and improving their well-being. Nothing is more satisfying to him than being amongst the people, sharing their joys and alleviating their sorrows. His powerful ‘personal connect’ with the people on ground is complemented by a strong online presence. He is known as India’s most techno-savvy leader, using the web to reach people and bring about change in their lives. He is very active on social media platforms including YouTube, Facebook, Twitter, Instagram, Sound Cloud, Linkedin, and other forums.

# Beyond politics, Narendra Modi enjoys writing. He has authored several books, including poetry. He begins his day with Yoga, which strengthens his body and mind and instills the power of calmness in an otherwise fast-paced routine.
#     """
    
#     # Generate summary
#     summary = summarize_text(text, glove_embeddings, num_sentences=3)
#     print("Summary:")
#     print(summary)




#glove 2nd

import numpy as np
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from nltk.tokenize import sent_tokenize, word_tokenize
import os

# Ensure nltk data is downloaded
nltk.download("punkt")

# Set environment to limit thread usage for reproducibility
os.environ["OMP_NUM_THREADS"] = "1"

# Load pre-trained GloVe embeddings
def load_glove_model(file_path):
    embeddings = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            word = parts[0]
            try:
                vector = np.array(parts[1:], dtype=np.float32)
                embeddings[word] = vector
            except ValueError:
                print(f"Skipping line: {line}")
    return embeddings

# Compute sentence embeddings using average of word embeddings
def sentence_embedding(sentence, embeddings):
    VECTOR_SIZE = len(next(iter(embeddings.values())))
    words = word_tokenize(sentence.lower())
    word_vectors = [embeddings[word] for word in words if word in embeddings]
    return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(VECTOR_SIZE)

# Summarize text by selecting representative sentences
def summarize_text(text, embeddings, num_sentences=20):
    sentences = sent_tokenize(text)
    sentence_vectors = [sentence_embedding(sent, embeddings) for sent in sentences]

    # Perform clustering
    kmeans = KMeans(n_clusters=num_sentences, random_state=42)
    kmeans.fit(sentence_vectors)
    cluster_centers = kmeans.cluster_centers_

    # Find representative sentences
    summary = []
    for center in cluster_centers:
        similarities = cosine_similarity([center], sentence_vectors)
        top_idx = np.argmax(similarities)
        summary.append(sentences[top_idx])

    return " ".join(summary)

# Main script
if __name__ == "__main__":
    # Load GloVe embeddings
    glove_file_path = "C:\\All project\\models\\glove.42B.300d\\glove.42B.300d.txt"  # Change to your GloVe file path
    glove_embeddings = load_glove_model(glove_file_path)
    
    # Example text
    text = """Shri Narendra Modi was sworn-in as India’s Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 Parliamentary elections. This victory marked the third consecutive term for Shri Modi, further solidifying his leadership.

    The 2024 elections saw a remarkable voter turnout, with a significant portion of the electorate showing continued confidence in Shri Modi’s leadership and vision for the country. His campaign focused on a blend of economic development, national security, and social welfare programs, which resonated widely with the populace.

    Shri Modi’s third term is expected to build on the foundations laid during his previous tenures, with a renewed emphasis on technological innovation, infrastructure development, and international diplomacy, further positioning India as a global powerhouse. The unprecedented third term underscores Shri Modi’s enduring appeal and the trust placed in him by millions of Indians to lead the nation towards greater prosperity and stability.

    The first ever Prime Minister to be born after Independence, Shri Modi has previously served as the Prime Minister of India from 2014 to 2019, and from 2019 to 2024. He also has the distinction of being the longest serving Chief Minister of Gujarat with his term spanning from October 2001 to May 2014.

    In the 2014 and 2019 Parliamentary elections, Shri Modi led the Bharatiya Janata Party to record wins, securing absolute majority on both occasions. The last time that a political party secured such an absolute majority was in the elections of 1984.

    Inspired by the motto of ‘SabkaSaath, Sabka Vikas, Sabka Vishwas’, Shri Modi has ushered in a paradigm shift in governance that has led to inclusive, development-oriented and corruption-free governance. The Prime Minister has worked with speed and scale to realise the aim of Antyodaya, or ensuring last-mile delivery of schemes and services.

    Leading international agencies have noted that under the leadership of PM Narendra Modi, India has been eliminating poverty at record pace. According to the findings from NITI Aayog’s latest report ‘Multidimensional Poverty in India since 2005-06’, almost 25 crore people escaped multidimensional poverty in last nine years. The credit for this remarkable achievement goes to significant initiatives of the government to address all dimensions of poverty.

    Today, India is home to the world’s largest healthcare programme, Ayushman Bharat. Covering over 50 crore Indians, Ayushman Bharat provides top quality and affordable healthcare to the poor and neo-middle class.

    The Lancet, considered among the most prestigious health journals in the world has lauded Ayushman Bharat, stating that this scheme attends to the larger discontent about the health sector in India. The journal also noted PM Modi’s efforts to prioritise universal health coverage.

    Understanding that financial exclusion was a bane for the poor, the Prime Minister launched the Pradhan Mantri Jan Dhan Yojana, that aimed at opening bank accounts for every Indian. Now, over 51 crore Jan Dhan accounts have been opened. These accounts have not only banked the unbanked but also opened the doors for other avenues of empowerment.

    Going a step ahead of Jan Dhan, Shri Modi emphasised on Jan Suraksha, by giving insurance and pension cover to the most vulnerable sections of society. The JAM trinity (Jan Dhan- Aadhaar- Mobile) has led to elimination of middle men and ensured transparency and speed, powered by technology.

    The Pradhan Mantri Ujjwala Yojana, launched in 2016 provides free cooking gas connections to the poor. It has proven to be a major game-changer in providing smoke-free kitchens to over 10 crore beneficiaries, most of whom are women.

    18,000 villages that were without electricity even after 70 long years of Independence have been electrified.

    Shri Modi believes that no Indian should be homeless and to realise this vision, over 4.2 crore houses were sanctionedunder the PM Awas Yojana between 2014 and 2024. In June 2024, after assuming office for the third term, one of the first decisions of the Cabinet was to assist 3 crore additional rural and urban households for the construction of houses, underscoring Shri Narendra Modi’s commitment to addressing the nation’s housing needs and ensuring dignity and a quality life for every citizen.

    Agriculture is a sector that is very close to Shri Narendra Modi. During the interim budget of 2019, the Government announced a monetary incentive for farmers called the PM Kisan Samman Nidhi. In almost three weeks, on 24th February 2019, the scheme was launched and instalments have been paid regularly since then. During the first Cabinet Meeting of PM Modi’s second term, it was decided to extend the PM Kisan benefits to all farmers, removing the 5 acre limit that was present earlier. As of June 2024, Shri Modi released the 17thinstalment of the PM-KISAN scheme at Varanasi in which more than 9.2 crore farmers received the benefits amounting to over Rs.20,000 crore.

    Shri Modi has also focused path-breaking initiatives for agriculture ranging from Soil Health Cards, E-NAM for better markets and a renewed focus on irrigation. On 30th May 2019, PM Modi fulfilled a major promise by creating a new Jal Shakti Ministry to cater to all aspects relating to water resources.

    On 2nd October 2014, Mahatma Gandhi’s Birth Anniversary, the PM launched ‘Swachh Bharat Mission’ a mass movement for cleanliness across the nation. The scale and impact of the movement is historic. Today, sanitation coverage has risen from 38% in 2014 to 100% in 2019. All states and Union Territories have been declared open defecation free (ODF). Substantive measures been taken for a clean Ganga.

    The World Health Organisation has appreciated the Swachh Bharat Mission and has opined that it would save three lakh lives.

    Shri Modi believes that transportation is an important means towards transformation. That is why, the Government of India has been working to create next-generation infrastructure be it in terms of more highways, railways, i-ways and waterways. The UDAN (UdeDesh Ka Aam Nagrik) Scheme has made aviation sector more people-friendly and boosted connectivity.

    PM Modi launched the ‘Make in India’ initiative to turn India into an international manufacturing powerhouse. This effort has led to transformative results. India has made significant strides in ‘Ease of Doing Business’, improving its ranking from 142 in 2014 to 63 in 2019. The Government of India rolled out the GST during a historic session of Parliament in 2017, which has realised the dream of ‘One Nation, One Tax.’

    During his tenure, special attention has been paid to India’s rich history and culture. India is home to the world’s largest statue, the State of Unity, a fitting tribute to Sardar Patel. This Statue was built through a special mass movement where tools of farmers and soil from all states and Union Territories of India were used, signifying the spirit of ‘Ek Bharat, Shreshtha Bharat.’

    PM Modi is deeply passionate about environmental causes. He has time and again called for closing of ranks to create a clean and green planet. As Chief Minister of Gujarat, Shri Modi created a separate Climate Change Department to create innovative solutions to climate change. This spirit was seen in the 2015 COP21 Summit in Paris where PM Modi played a key role in the high-level deliberations.

    Going a step ahead of climate change, PM Modi has talked about climate justice. In 2018, Heads of State and Government from several nations came to India for the launch of the International Solar Alliance, an innovative effort to harness solar energy for a better planet.

    Recognising his efforts towards environmental conservation, PM Modi was honoured with the United Nations ‘Champions of the Earth Award.’

    Fully sensitive to the fact that climate change has made our planet prone to natural disasters, Shri Modi has brought a new approach to disaster management, harnessing the power of technology and the strength of human resources. As Chief Minister, he transformed Gujarat that had just been ravaged by a devastating earthquake on 26th January 2001. Likewise, he introduced new systems to combat floods and droughts in Gujarat that were internationally lauded.

    Through administrative reforms, Shri Modi has always given priority to justice for citizens. In Gujarat, he spearheaded the start of evening courts to ensure people’s issues are resolved. At the Centre, he began PRAGATI ((Pro-Active Governance And Timely Implementation) to expedite pending projects that were delaying growth.

    Shri Modi’s foreign policy initiatives have realised the true potential and role of world’s largest democracy. He began his first term in office in presence of all Heads of States of SAARC Nations and invited BIMSTEC leaders at the start of the second. His address to the General Assembly of United Nations was appreciated across the world. Shri Modi became the first Indian Prime Minister to embark on a bilateral visit to Nepal after a long period of 17 years, to Australia after 28 years, to Fiji after 31 years and UAE as well as Seychelles after 34 years. Since taking over, Shri Modi attended UN, BRICS, SAARC and G-20 Summits, where India’s interventions and views on a variety of global economic and political issues were widely appreciated.

    PM Modi has been conferred various honours including the highest civilian honour of Saudi Arabia Sash of King Abdulaziz. Shri Modi has been also been conferred the top awards of Russia (The Order of the Holy Apostle Andrew the First), Palestine (Grand Collar of the State of Palestine), Afghanistan (Amir Amanullah Khan Award), UAE (Order of Zayed Award), Maldives (Rule of Nishan Izzuddeen), Bahrain (King Hamad Order of the Renaissance), Bhutan (Order of the Druk Gyalpo), Papua New Guinea (Grand Companion of the Order of Logohu), Fiji (Companion of the Order of Fiji), Egypt (Order of Nile), France (Grand Cross of the Legion of Honour), and Greece (The Grand Cross of the Order of Honour). In 2018, PM received the prestigious Seoul Peace Prize for his contribution to peace and development.He has also received the Global Goalkeeper’ Award by Bill and Melinda Gates Foundation, and Global Energy and Environment Leadership Award by Cambridge Energy Research Associates.

    Narendra Modi’s clarion call for marking a day as ‘International Day of Yoga’ received an overwhelming response at the UN. In a first, a total of 177 Nations across the world came together and passed the resolution to declare 21st June as the ‘International Day of Yoga at the UN.’

    Shri Modi was born on 17 September, 1950, in a small town in Gujarat. His family belonged to the ‘other backward class’ which is among the marginalised sections of society. He grew up in a poor but loving family ‘without a spare rupee’. The initial hardships of life not only taught the value of hard work but also exposed him to the avoidable sufferings of the common people. This inspired him from a very young age to immerse himself in service of people and the nation. In his initial years, he worked with the Rashtriya Swayamsevak Sangh (RSS), a nationalist organisation devoted to nation building and later devoted himself in politics working with the Bharatiya Janata Party organization at National and State level. Shri Modi completed his MA in political science from Gujarat University.

    Narendra Modi is a ‘People’s Leader’, dedicated to solving their problems and improving their well-being. Nothing is more satisfying to him than being amongst the people, sharing their joys and alleviating their sorrows. His powerful ‘personal connect’ with the people on ground is complemented by a strong online presence. He is known as India’s most techno-savvy leader, using the web to reach people and bring about change in their lives. He is very active on social media platforms including YouTube, Facebook, Twitter, Instagram, Sound Cloud, Linkedin, and other forums.

    Beyond politics, Narendra Modi enjoys writing. He has authored several books, including poetry. He begins his day with Yoga, which strengthens his body and mind and instills the power of calmness in an otherwise fast-paced routine.
        """  # Replace with your input text
    
    # Generate summary
    summary = summarize_text(text, glove_embeddings, num_sentences=20)
    print("Summary:")
    print(summary)





#gove using chunk..... want to check

# import numpy as np
# import nltk
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.cluster import KMeans
# from nltk.tokenize import sent_tokenize, word_tokenize
# import os

# # Ensure nltk data is downloaded
# nltk.download("punkt")

# # Set environment to limit thread usage for reproducibility
# os.environ["OMP_NUM_THREADS"] = "1"

# # Load pre-trained GloVe embeddings
# def load_glove_model(file_path):
#     embeddings = {}
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             parts = line.strip().split()
#             word = parts[0]
#             try:
#                 vector = np.array(parts[1:], dtype=np.float32)
#                 embeddings[word] = vector
#             except ValueError:
#                 print(f"Skipping line: {line}")
#     return embeddings

# # Compute sentence embeddings using average of word embeddings
# def sentence_embedding(sentence, embeddings):
#     VECTOR_SIZE = len(next(iter(embeddings.values())))
#     words = word_tokenize(sentence.lower())
#     word_vectors = [embeddings[word] for word in words if word in embeddings]
#     return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(VECTOR_SIZE)

# # Summarize text by selecting representative sentences
# def summarize_text(text, embeddings, num_sentences=3):
#     sentences = sent_tokenize(text)
#     sentence_vectors = [sentence_embedding(sent, embeddings) for sent in sentences]

#     # Perform clustering
#     kmeans = KMeans(n_clusters=num_sentences, random_state=42)
#     kmeans.fit(sentence_vectors)
#     cluster_centers = kmeans.cluster_centers_

#     # Find representative sentences
#     summary = []
#     for center in cluster_centers:
#         similarities = cosine_similarity([center], sentence_vectors)
#         top_idx = np.argmax(similarities)
#         summary.append(sentences[top_idx])

#     return " ".join(summary)

# # Process large text in chunks
# def summarize_large_text(text, embeddings, num_sentences=3, chunk_size=5000):
#     # Split text into chunks of approximately `chunk_size` words
#     words = text.split()
#     chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

#     # Summarize each chunk and combine summaries
#     chunk_summaries = []
#     for i, chunk in enumerate(chunks):
#         print(f"Processing chunk {i+1}/{len(chunks)}...")
#         chunk_summary = summarize_text(chunk, embeddings, num_sentences)
#         chunk_summaries.append(chunk_summary)

#     # Combine summaries from chunks into a final summary
#     combined_summary = " ".join(chunk_summaries)
#     final_summary = summarize_text(combined_summary, embeddings, num_sentences)
#     return final_summary

# # Main script
# if __name__ == "__main__":
#     # Load GloVe embeddings
#     glove_file_path = "C:\\All project\\models\\glove.42B.300d\\glove.42B.300d.txt"  # Change to your GloVe file path
#     glove_embeddings = load_glove_model(glove_file_path)
    
#     # Example large text
#     text = """<YOUR_LARGE_TEXT_HERE>"""  # Replace with your 15,000-word text
    
#     # Generate summary
#     summary = summarize_large_text(text, glove_embeddings, num_sentences=5, chunk_size=5000)
#     print("Summary:")
#     print(summary)







#word2vec text summarization



# import numpy as np
# import nltk
# from gensim.models import KeyedVectors
# from nltk.tokenize import sent_tokenize, word_tokenize
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.cluster import KMeans

# # Ensure nltk data is downloaded
# nltk.download("punkt")

# # Load pre-trained Word2Vec model
# def load_word2vec_model(file_path):
#     return KeyedVectors.load_word2vec_format(file_path, binary=True)  # Use binary=False for plain text format

# # Compute sentence embeddings using average of word embeddings
# def sentence_embedding(sentence, model):
#     words = word_tokenize(sentence)
#     word_vectors = [model[word] for word in words if word in model.key_to_index]
#     if word_vectors:
#         return np.mean(word_vectors, axis=0)
#     else:
#         return np.zeros(model.vector_size)

# # Summarize text by selecting representative sentences
# def summarize_text(text, model, num_sentences=7):
#     sentences = sent_tokenize(text)
#     sentence_vectors = [sentence_embedding(sent, model) for sent in sentences]
    
#     # Perform clustering
#     sentence_vectors = np.array(sentence_vectors)
#     kmeans = KMeans(n_clusters=num_sentences, random_state=42)
#     kmeans.fit(sentence_vectors)
#     cluster_centers = kmeans.cluster_centers_
    
#     # Find representative sentences
#     summary = []
#     for center in cluster_centers:
#         similarities = cosine_similarity([center], sentence_vectors)
#         top_indices = np.argsort(similarities[0])[-3:]  # Select the most similar sentence per cluster
#         for idx in top_indices:
#             summary.append(sentences[idx])

#     return " ".join(summary)

# # Main script
# if __name__ == "__main__":
#     # Load Word2Vec model
#     word2vec_file_path = "C:\\Users\\Viswajith\\Downloads\\archive (2)\\GoogleNews-vectors-negative300.bin"  # Change to your Word2Vec file path
#     word2vec_model = load_word2vec_model(word2vec_file_path)
    
#     # Example text
#     text = """
# Overview of MS Dhoni as one of India's greatest cricketers.
# His legacy and influence both on and off the field.
# Early Life and Background

# Birth and family background in Ranchi, Jharkhand.
# Early interest in sports and transition from football to cricket.
# Initial struggles and breakthrough in domestic cricket.
# Rise in International Cricket

# Debut in 2004 against Bangladesh.
# His aggressive playing style and record-breaking performances.
# The significance of his innings, including the famous 148 against Pakistan.
# Captaincy and Leadership

# Becoming India's captain in 2007 for the T20 World Cup.
# Leading India to victory in the inaugural T20 World Cup (2007).
# His leadership style: calm under pressure, strategic, and unconventional.
# The historic 2007 ICC T20 World Cup win and its impact on Indian cricket.
# MS Dhoni's Contribution to Indian Cricket

# Leading India to victory in the 2011 ICC Cricket World Cup.
# Captaining the team to the 2013 ICC Champions Trophy win.
# Transforming the Indian team into a world-class unit with a focus on fitness, attitude, and approach.
# His role in mentoring young players and fostering a competitive environment.
# Captaincy in IPL and CSK

# Leading Chennai Super Kings (CSK) in the IPL.
# Success of CSK under Dhoni’s leadership, with multiple IPL titles.
# Building CSK as one of the most successful and beloved teams in the IPL.
# Dhoni’s relationship with CSK fans and his influence on the franchise.
# Style of Play and Unique Traits

# His wicketkeeping skills and unique batting style.
# The evolution of his finishing role in limited-overs cricket.
# Understanding Dhoni’s on-field personality: calculated, fearless, and aggressive when needed.
# Key performances, including his match-winning knocks in World Cup finals and IPL.
# Memorable Moments in Dhoni’s Career

# The iconic 2011 World Cup-winning six.
# Leading India to the 2013 Champions Trophy victory.
# Last-minute finishes and games won from seemingly impossible situations.
# The memorable helicopter shot, which became his signature.
# Challenges and Setbacks

# Handling criticism, especially after losses.
# Balancing the pressure of captaincy and performance.
# The 2014 IPL final and the fallout of losing.
# His controversial decisions and some of his critics.
# Retirement and Legacy

# Retirement from Test cricket in 2014.
# The impact of his retirement from limited-overs cricket in 2020.
# Dhoni’s legacy as a captain and player, including his longevity in international cricket.
# How he paved the way for future generations of cricketers, especially in leadership roles.
# Contributions outside of cricket, including business ventures and philanthropy.
# Dhoni's Influence on Indian Society

# His role as an inspiration for millions of Indians.
# The Dhoni brand and his influence on youth culture in India.
# His calm demeanor, self-discipline, and work ethic becoming models for millions.
# Conclusion

# Final thoughts on Dhoni’s career, his contribution to cricket, and his standing in the pantheon of cricketing legends.
# Dhoni’s retirement from international cricket and the void left in Indian cricket.
# Sample Excerpt (Shortened Version)
# Early Life and Background

# Mahendra Singh Dhoni, commonly known as MS Dhoni, was born on July 7, 1981, in Ranchi, Jharkhand. Growing up in a middle-class family, Dhoni was initially more inclined towards football and badminton. His passion for cricket ignited during his school years, where he started as a goalkeeper for his school's football team. The transition to cricket was a gradual one, but his raw talent was soon recognized by coaches. Dhoni's journey in cricket began at the state level, where he played for Bihar in domestic cricket before Jharkhand’s formation.

# He had an unconventional rise, playing for the India A team and performing consistently well. His explosive batting and wicketkeeping skills caught the attention of the selectors. His big break came in 2004 when he made his debut for India against Bangladesh, where he was dismissed cheaply. Despite this early setback, Dhoni’s confidence and determination helped him rise quickly in Indian cricket.

# Captaincy and Leadership

# In 2007, MS Dhoni was handed the leadership of the Indian team for the inaugural ICC T20 World Cup. Under his captaincy, India became the first-ever T20 World Cup champions, defeating Pakistan in a nail-biting final. Dhoni's calm demeanor under pressure, his trust in young players, and his tactical decisions set him apart as a leader.

# Dhoni’s leadership in One Day Internationals (ODIs) and T20Is saw India rise to number one in the ICC rankings and eventually led the team to victory in the 2011 ICC Cricket World Cup. One of the most iconic moments in Indian cricket came when Dhoni hit the match-winning six in the final, sealing India’s first World Cup win in 28 years.

# The IPL and CSK

# In the Indian Premier League (IPL), Dhoni's impact was even more significant. He led Chennai Super Kings (CSK) to several IPL titles, cementing his reputation as one of the greatest captains in the T20 format. His leadership helped turn CSK into a franchise with a loyal fanbase, and his calmness on the field was mirrored by the team's disciplined approach.

# Conclusion

# MS Dhoni's contribution to Indian cricket cannot be overstated. He was not just a player but a visionary leader, a mentor, and a symbol of perseverance. His legacy as a captain, batsman, and wicketkeeper will inspire generations to come. Dhoni’s story is one of grit, determination, and unmatched leadership. He may have retired from international cricket, but his influence continues to resonate in the world of cricket.
#     """

#     # Generate summary
#     summary = summarize_text(text, word2vec_model, num_sentences=7)
#     print("Summary:")
#     print(summary)









# from transformers import LEDTokenizer, LEDForConditionalGeneration

# def clean_text(text):
#     """
#     Cleans the input text by removing special characters and extra whitespaces.
#     """
#     import re
#     text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespaces with a single space
#     text = re.sub(r'[^a-zA-Z0-9\s,.]', '', text)  # Remove non-alphanumeric characters except punctuation
#     return text.strip()

# def summarize_text_longformer(
#     text, 
#     max_length=500, 
#     min_length=400, 
#     length_penalty=1.0, 
#     num_beams=4,
#     repetition_penalty=2.0
# ):
#     """
#     Summarizes the input text using the allenai/led-large-16384 model.
#     """
#     model_name = "allenai/led-large-16384"
    
#     # Load the tokenizer and model
#     tokenizer = LEDTokenizer.from_pretrained(model_name)
#     model = LEDForConditionalGeneration.from_pretrained(model_name)
    
#     # Clean and preprocess input text
#     text = clean_text(text)
    
#     # Tokenize and encode the input text
#     inputs = tokenizer(text, return_tensors="pt", max_length=16384, truncation=True, padding=True)
#     print(f"Number of tokens: {inputs['input_ids'].size(1)}")  # Debug token count
    
#     # Generate the summary
#     try:
#         summary_ids = model.generate(
#             inputs['input_ids'],
#             attention_mask=inputs['attention_mask'],
#             max_length=max_length,
#             min_length=min_length,
#             length_penalty=length_penalty,
#             num_beams=num_beams,
#             repetition_penalty=repetition_penalty,
#             early_stopping=True
#         )
#         summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#         return summary
#     except Exception as e:
#         print(f"Error during generation: {e}")
#         return None


# # Example usage
# if __name__ == "__main__":
#     text = """
# Shri Narendra Modi was sworn-in as India’s Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 Parliamentary elections. This victory marked the third consecutive term for Shri Modi, further solidifying his leadership.

# The 2024 elections saw a remarkable voter turnout, with a significant portion of the electorate showing continued confidence in Shri Modi’s leadership and vision for the country. His campaign focused on a blend of economic development, national security, and social welfare programs, which resonated widely with the populace.

# Shri Modi’s third term is expected to build on the foundations laid during his previous tenures, with a renewed emphasis on technological innovation, infrastructure development, and international diplomacy, further positioning India as a global powerhouse. The unprecedented third term underscores Shri Modi’s enduring appeal and the trust placed in him by millions of Indians to lead the nation towards greater prosperity and stability.

# The first ever Prime Minister to be born after Independence, Shri Modi has previously served as the Prime Minister of India from 2014 to 2019, and from 2019 to 2024. He also has the distinction of being the longest serving Chief Minister of Gujarat with his term spanning from October 2001 to May 2014.

# In the 2014 and 2019 Parliamentary elections, Shri Modi led the Bharatiya Janata Party to record wins, securing absolute majority on both occasions. The last time that a political party secured such an absolute majority was in the elections of 1984.

# Inspired by the motto of ‘SabkaSaath, Sabka Vikas, Sabka Vishwas’, Shri Modi has ushered in a paradigm shift in governance that has led to inclusive, development-oriented and corruption-free governance. The Prime Minister has worked with speed and scale to realise the aim of Antyodaya, or ensuring last-mile delivery of schemes and services.

# Leading international agencies have noted that under the leadership of PM Narendra Modi, India has been eliminating poverty at record pace. According to the findings from NITI Aayog’s latest report ‘Multidimensional Poverty in India since 2005-06’, almost 25 crore people escaped multidimensional poverty in last nine years. The credit for this remarkable achievement goes to significant initiatives of the government to address all dimensions of poverty.

# Today, India is home to the world’s largest healthcare programme, Ayushman Bharat. Covering over 50 crore Indians, Ayushman Bharat provides top quality and affordable healthcare to the poor and neo-middle class.

# The Lancet, considered among the most prestigious health journals in the world has lauded Ayushman Bharat, stating that this scheme attends to the larger discontent about the health sector in India. The journal also noted PM Modi’s efforts to prioritise universal health coverage.

# Understanding that financial exclusion was a bane for the poor, the Prime Minister launched the Pradhan Mantri Jan Dhan Yojana, that aimed at opening bank accounts for every Indian. Now, over 51 crore Jan Dhan accounts have been opened. These accounts have not only banked the unbanked but also opened the doors for other avenues of empowerment.

# Going a step ahead of Jan Dhan, Shri Modi emphasised on Jan Suraksha, by giving insurance and pension cover to the most vulnerable sections of society. The JAM trinity (Jan Dhan- Aadhaar- Mobile) has led to elimination of middle men and ensured transparency and speed, powered by technology.

# The Pradhan Mantri Ujjwala Yojana, launched in 2016 provides free cooking gas connections to the poor. It has proven to be a major game-changer in providing smoke-free kitchens to over 10 crore beneficiaries, most of whom are women.

# 18,000 villages that were without electricity even after 70 long years of Independence have been electrified.

# Shri Modi believes that no Indian should be homeless and to realise this vision, over 4.2 crore houses were sanctionedunder the PM Awas Yojana between 2014 and 2024. In June 2024, after assuming office for the third term, one of the first decisions of the Cabinet was to assist 3 crore additional rural and urban households for the construction of houses, underscoring Shri Narendra Modi’s commitment to addressing the nation’s housing needs and ensuring dignity and a quality life for every citizen.

# Agriculture is a sector that is very close to Shri Narendra Modi. During the interim budget of 2019, the Government announced a monetary incentive for farmers called the PM Kisan Samman Nidhi. In almost three weeks, on 24th February 2019, the scheme was launched and instalments have been paid regularly since then. During the first Cabinet Meeting of PM Modi’s second term, it was decided to extend the PM Kisan benefits to all farmers, removing the 5 acre limit that was present earlier. As of June 2024, Shri Modi released the 17thinstalment of the PM-KISAN scheme at Varanasi in which more than 9.2 crore farmers received the benefits amounting to over Rs.20,000 crore.

# Shri Modi has also focused path-breaking initiatives for agriculture ranging from Soil Health Cards, E-NAM for better markets and a renewed focus on irrigation. On 30th May 2019, PM Modi fulfilled a major promise by creating a new Jal Shakti Ministry to cater to all aspects relating to water resources.

# On 2nd October 2014, Mahatma Gandhi’s Birth Anniversary, the PM launched ‘Swachh Bharat Mission’ a mass movement for cleanliness across the nation. The scale and impact of the movement is historic. Today, sanitation coverage has risen from 38% in 2014 to 100% in 2019. All states and Union Territories have been declared open defecation free (ODF). Substantive measures been taken for a clean Ganga.

# The World Health Organisation has appreciated the Swachh Bharat Mission and has opined that it would save three lakh lives.

# Shri Modi believes that transportation is an important means towards transformation. That is why, the Government of India has been working to create next-generation infrastructure be it in terms of more highways, railways, i-ways and waterways. The UDAN (UdeDesh Ka Aam Nagrik) Scheme has made aviation sector more people-friendly and boosted connectivity.

# PM Modi launched the ‘Make in India’ initiative to turn India into an international manufacturing powerhouse. This effort has led to transformative results. India has made significant strides in ‘Ease of Doing Business’, improving its ranking from 142 in 2014 to 63 in 2019. The Government of India rolled out the GST during a historic session of Parliament in 2017, which has realised the dream of ‘One Nation, One Tax.’

# During his tenure, special attention has been paid to India’s rich history and culture. India is home to the world’s largest statue, the State of Unity, a fitting tribute to Sardar Patel. This Statue was built through a special mass movement where tools of farmers and soil from all states and Union Territories of India were used, signifying the spirit of ‘Ek Bharat, Shreshtha Bharat.’

# PM Modi is deeply passionate about environmental causes. He has time and again called for closing of ranks to create a clean and green planet. As Chief Minister of Gujarat, Shri Modi created a separate Climate Change Department to create innovative solutions to climate change. This spirit was seen in the 2015 COP21 Summit in Paris where PM Modi played a key role in the high-level deliberations.

# Going a step ahead of climate change, PM Modi has talked about climate justice. In 2018, Heads of State and Government from several nations came to India for the launch of the International Solar Alliance, an innovative effort to harness solar energy for a better planet.

# Recognising his efforts towards environmental conservation, PM Modi was honoured with the United Nations ‘Champions of the Earth Award.’

# Fully sensitive to the fact that climate change has made our planet prone to natural disasters, Shri Modi has brought a new approach to disaster management, harnessing the power of technology and the strength of human resources. As Chief Minister, he transformed Gujarat that had just been ravaged by a devastating earthquake on 26th January 2001. Likewise, he introduced new systems to combat floods and droughts in Gujarat that were internationally lauded.

# Through administrative reforms, Shri Modi has always given priority to justice for citizens. In Gujarat, he spearheaded the start of evening courts to ensure people’s issues are resolved. At the Centre, he began PRAGATI ((Pro-Active Governance And Timely Implementation) to expedite pending projects that were delaying growth.

# Shri Modi’s foreign policy initiatives have realised the true potential and role of world’s largest democracy. He began his first term in office in presence of all Heads of States of SAARC Nations and invited BIMSTEC leaders at the start of the second. His address to the General Assembly of United Nations was appreciated across the world. Shri Modi became the first Indian Prime Minister to embark on a bilateral visit to Nepal after a long period of 17 years, to Australia after 28 years, to Fiji after 31 years and UAE as well as Seychelles after 34 years. Since taking over, Shri Modi attended UN, BRICS, SAARC and G-20 Summits, where India’s interventions and views on a variety of global economic and political issues were widely appreciated.

# PM Modi has been conferred various honours including the highest civilian honour of Saudi Arabia Sash of King Abdulaziz. Shri Modi has been also been conferred the top awards of Russia (The Order of the Holy Apostle Andrew the First), Palestine (Grand Collar of the State of Palestine), Afghanistan (Amir Amanullah Khan Award), UAE (Order of Zayed Award), Maldives (Rule of Nishan Izzuddeen), Bahrain (King Hamad Order of the Renaissance), Bhutan (Order of the Druk Gyalpo), Papua New Guinea (Grand Companion of the Order of Logohu), Fiji (Companion of the Order of Fiji), Egypt (Order of Nile), France (Grand Cross of the Legion of Honour), and Greece (The Grand Cross of the Order of Honour). In 2018, PM received the prestigious Seoul Peace Prize for his contribution to peace and development.He has also received the Global Goalkeeper’ Award by Bill and Melinda Gates Foundation, and Global Energy and Environment Leadership Award by Cambridge Energy Research Associates.

# Narendra Modi’s clarion call for marking a day as ‘International Day of Yoga’ received an overwhelming response at the UN. In a first, a total of 177 Nations across the world came together and passed the resolution to declare 21st June as the ‘International Day of Yoga at the UN.’

# Shri Modi was born on 17 September, 1950, in a small town in Gujarat. His family belonged to the ‘other backward class’ which is among the marginalised sections of society. He grew up in a poor but loving family ‘without a spare rupee’. The initial hardships of life not only taught the value of hard work but also exposed him to the avoidable sufferings of the common people. This inspired him from a very young age to immerse himself in service of people and the nation. In his initial years, he worked with the Rashtriya Swayamsevak Sangh (RSS), a nationalist organisation devoted to nation building and later devoted himself in politics working with the Bharatiya Janata Party organization at National and State level. Shri Modi completed his MA in political science from Gujarat University.

# Narendra Modi is a ‘People’s Leader’, dedicated to solving their problems and improving their well-being. Nothing is more satisfying to him than being amongst the people, sharing their joys and alleviating their sorrows. His powerful ‘personal connect’ with the people on ground is complemented by a strong online presence. He is known as India’s most techno-savvy leader, using the web to reach people and bring about change in their lives. He is very active on social media platforms including YouTube, Facebook, Twitter, Instagram, Sound Cloud, Linkedin, and other forums.

# Beyond politics, Narendra Modi enjoys writing. He has authored several books, including poetry. He begins his day with Yoga, which strengthens his body and mind and instills the power of calmness in an otherwise fast-paced routine.
#     """
    
#     summarized_text = summarize_text_longformer(text, max_length=500, min_length=400, num_beams=4)
#     print("\nSummarized Text:\n", summarized_text)


