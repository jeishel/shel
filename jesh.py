from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Programming is the best",page_icon=":hala:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',  unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/ii.png")
img_github = Image.open("images/nn.jpg")

 

with st.container():
    st.subheader('Hi, I am Jeishel Rivas')
    st.title('Find out how interesting Computer Engineering is through my blog')
    st.write('Hey there, fellow tech enthusiast! Ready to dive into the wild world of Computer Engineering with me? Buckle up because I am about to spill the beans on the highs and lows of being a Computer Engineer in the making')
    st.write('Welcome to my corner of the internet, where we are about to unravel the rollercoaster ride of Pros and Cons that come with the badge of being a Computer Engineering student. Lets get this byte-sized adventure started! 💻✨')
    st.write('[Message me in gmail >](jrivas2@ssct.edu.ph)')

with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("Computer Programming: First-Year Perspective")
        st.write("##")
        st.write(
            """
        The first Impression
        -As I stepped into the university halls, a blend of excitement and nerves surged through me. 
        The world of computer engineering beckoned, promising both challenges and boundless opportunities.
        From day one, I was introduced to the foundational concepts binary, algorithms, and the wonders of programming languages. 
        It was like learning a secret language that unlocks the possibilities of technology
            """
        )
        
    st.write("[For more information >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("to know")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.write(
        """
        -Let's talk about those courses! Oh, the thrill and sometimes the slight terror of facing programming assignments.
          Debugging became my daily workout routine, and trust me, the satisfaction of fixing the bug after hours of contemplation is unmatched.
        """     
        )
    st.write("Ah, the eternal struggle of balancing academics, social life, and personal time.")
    st.write('It is a fine tuned juggling act, But I learned that organization and time management are my trusty sidekicks in this endeavor.')
    st.write('-The journey of a computer engineering freshman is a whirlwind a mix of curiosity, challenges, and unending discoveries. ')
    st.write('Every line of code written is a step forward in understanding the complex yet captivating world of technology.')
    st.write('-So, future freshmen or tech enthusiasts, join me in this exhilarating expedition as we unravel the mysteries of computer engineering, one line of code at a time')

with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_github)

with text_column:
    st.subheader("PROS AND CONS")
    st.write("Computer programming offers numerous benefits and a few challenges as well. Here's a breakdown:")
    st.write("PROS:")
    st.write("1.Lucrative Career Opportunities: Programming skills are in high demand across industries, offering excellent job prospects and high salaries.")
    st.write("2.Problem-Solving Skills: Programming teaches you to break down complex problems into smaller, manageable parts, enhancing your logical thinking and problem-solving abilities.")
    st.write("3.Creativity: It's a creative field where you can build something from scratch, allowing for innovative solutions and unique creations.")
    st.write("4.Flexibility: You can work remotely, freelance, or in an office, providing flexibility in work environments.")
    st.write("5.Continuous Learning: Technology is constantly evolving, ensuring that there's always something new to learn, keeping the field dynamic and exciting.")
    st.write("6.Global Community: Programming connects you with a vast global community of developers, fostering collaboration and shared knowledge.")
    
    st.write("CONS:")
    st.write("1.Steep Learning Curve: Initially, learning to code can be challenging and might require patience and perseverance to grasp programming concepts.")  
    st.write("2.Sedentary Work: Programming often involves long hours of sitting, which can impact physical health if not balanced with exercise and breaks.")
    st.write("3.Frustration with Bugs: Debugging code can be frustrating and time-consuming, especially when dealing with complex errors")
    st.write("4.Rapid Technological Changes: Keeping up with the latest languages, frameworks, and tools can be overwhelming and require continuous learning.")
    st.write("5.Isolation: Depending on work settings, programmers might spend long hours working alone, which can lead to a sense of isolation.")
    st.write("6.Complexity: As projects grow larger, managing code complexity becomes more challenging, requiring good organizational skills.")
    
with st.container():
    st.write("---")
    st.header('For Comments:')
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/rivasjeishel@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message  here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
