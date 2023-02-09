import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("YOLO V5 Object Detection App")
st.caption('This web application demostrate Object Detection')

# Content
st.markdown("""
### This App detects objects from Images
- Automatically detects 20 objects from image
- [Click here for App](/YOLO_for_image/)  

Below give are the object the our model will detect
1. Person
2. Car
3. Chair
4. Bottle
5. Sofa
6. Bicyle
7. Horse
8. Boat
9. Motor Bike
10. Cat
11. Tv Monitor
12. Cow
13. Sheep
14. Aeroplane
15. Train
16. Dining Table
17. Bus
18. Potted Plant
19. Bird
20. Dog 
           
            """)