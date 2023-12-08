import requests
import streamlit as st

st.set_page_config(page_title="Jeishel_Blog", page_icon=":heart:", layout="wide")


with st.container():
    st.subheader("Hi, I'm Jeishel Rivas :wave:")
    st.title("Find out how interesting Computer Engineering is through my blog")
    st.write("Hey there, fellow tech enthusiast! Ready to dive into the wild world of Computer Engineering with me? Buckle up because I'm about to spill the beans on the highs and lows of being a Computer Engineer in the making. Welcome to my corner of the internet, where we're about to unravel the rollercoaster ride of Pros and Cons that come with the badge of being a Computer Engineering student. Let's get this byte-sized adventure started! 💻✨")
    st.write("[Message me in gmail >] jrivas2@ssct.edu.ph")


with st.container():
     st.title("Computer Programming: First-Year Perspective") 


with st.container():     
     image_file_path = "Untitled_design-removebg-preview.PNG"
     st.image(image_file_path, caption="Rivas, Jeishel C.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("The first Impression")
        st.write("##")
        st.write(
            """
            -As I stepped into the university halls, a blend of excitement and nerves surged through me. The world of computer engineering beckoned, promising both challenges and boundless opportunities. From day one, I was introduced to the foundational concepts—binary, algorithms, and the wonders of programming languages. It was like learning a secret language that unlocks the possibilities of technology.\n
            -Let's talk about those courses! Oh, the thrill and sometimes the slight terror of facing programming assignments. Debugging became my daily workout routine, and trust me, the satisfaction of fixing the bug after hours of contemplation is unmatched.\n
            -Ah, the eternal struggle of balancing academics, social life, and personal time. It's a fine-tuned juggling act. But I've learned that organization and time management are my trusty sidekicks in this endeavor.\n
            -The journey of a computer engineering freshman is a whirlwind—a mix of curiosity, challenges, and unending discoveries. Every line of code written is a step forward in understanding the complex yet captivating world of technology.\n
            -So, future freshmen or tech enthusiasts, join me in this exhilarating expedition as we unravel the mysteries of computer engineering, one line of code at a time!

            """ 
         )
with st.container():     
     image_file_path = "wowowowow.jpg"
     st.image(image_file_path, caption="Computer Engineer")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("PROS AND CONS")
        st.write("##")
        st.write(
            """
            Computer programming offers numerous benefits and a few challenges as well. Here's a breakdown:\n
            **Pros:**\n
            1.Lucrative Career Opportunities: Programming skills are in high demand across industries, offering excellent job prospects and high salaries.\n
            2.Problem-Solving Skills: Programming teaches you to break down complex problems into smaller, manageable parts, enhancing your logical thinking and problem-solving abilities.\n
            3.Creativity: It's a creative field where you can build something from scratch, allowing for innovative solutions and unique creations.\n
            4.Flexibility: You can work remotely, freelance, or in an office, providing flexibility in work environments.\n
            5.Continuous Learning: Technology is constantly evolving, ensuring that there's always something new to learn, keeping the field dynamic and exciting.\n
            6.Global Community: Programming connects you with a vast global community of developers, fostering collaboration and shared knowledge.\n

            **Cons:**\n
            1.Steep Learning Curve: Initially, learning to code can be challenging and might require patience and perseverance to grasp programming concepts.\n
            2.Sedentary Work: Programming often involves long hours of sitting, which can impact physical health if not balanced with exercise and breaks.\n
            3.Frustration with Bugs: Debugging code can be frustrating and time-consuming, especially when dealing with complex errors.\n
            4.Rapid Technological Changes: Keeping up with the latest languages, frameworks, and tools can be overwhelming and require continuous learning.\n
            5.Isolation: Depending on work settings, programmers might spend long hours working alone, which can lead to a sense of isolation.\n
            6.Complexity: As projects grow larger, managing code complexity becomes more challenging, requiring good organizational skills.

            """ 
         )
        
        with st.container():     
         image_file_path = "yehey.jpg"
         st.image(image_file_path, caption="Computer Engineering Student")
    
        st.write("[Facebook account>](https://www.facebook.com/JEISHELRIVAS101/)")
    
        


    