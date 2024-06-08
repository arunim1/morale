import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import random

st.title("Morale Evaluation")
reminder_lines = ['* To have high morale is to believe that you are able to do the things you want to do; to have low morale is to believe the opposite.', '* Either state is stable, and your brain will act to reinforce it, so that reality matches its expectation.', '* Everything - everything - either increases or decreases morale.']
st.write("\n".join(reminder_lines))

# Create a form
with st.form(key='morale_form'):
    morale_level = st.radio("My morale is", ("Low", "High"))
    submit_button = st.form_submit_button(label='next')

# Display the output based on the submitted form
if submit_button:
    if morale_level == "Low":
        morale_boosters = ['#1. Publishing a blog post', '#2. Dancing', '#3. Looking at posters of warfare, heroes, or aggressive slogans in bold font', '#4. Drinking coffee', '#5. Saying “i want”', '#6. Doing things that increase morale', '#7. Going to bed and getting out of bed at a time you previously decided', '#8. feeling 1/10 upon waking up but getting out of bed because you have a train to catch in 20 minutes and by the time you make it a minute before departure you forgot you were sleepy at all', '#9. feeling ahead (of enemies or schedule).', '#10. going outside', '#11. Watching this video https://www.youtube.com/watch?v=X8-qnUyJSlc', '#12. remembering that even ceos took vacations', '#13. remembering that i could’ve spent literally all day watching youtube (did like 5 days of this in 2023) and i would have 0 new tasks & made 0 progress, except some old tasks now expired. so just doing nothing decreases number of tasks. so doing things literally can’t increase number of tasks.', '#14. Deliberately working for a small number of hours - like 4 - if you’re doing something hard', '#15. watching basically any christopher nolan movie, or master and commander', '#16. Watching https://www.youtube.com/watch?v=a3lcGnMhvsA', '#17. Watching https://www.youtube.com/watch?v=th5A6ZQ28pE', '#18. Watching https://www.youtube.com/watch?v=rbnlp8q3Rsk', '#19. Watching https://www.youtube.com/watch?v=5-sfG8BV8wU', '#20. stopping a thief', '#21. Meditating and asking myself what should I be doing? why?', '#22. Going out of your way to show how you care for someone', '#23. liking the guy staring at yourself in the mirror', '#24. exhausting yourself by running', '#25. traveling to your favorite city', '#26. generating like / laugh reactions in any kind of chat or twitter', '#27. reading this paul graham essay (http://paulgraham.com/greatwork.html)', '#28. remembering that paul graham is one of the greatest writers of all time because he literally just decided to be one day', '#29. writing down things that are floating in your head and causing you to worry and making them explicit', '#30. task list size decreasing', '#31. making concrete progress towards a specific goal', '#32. scheduling the day fully the day before & following the schedule', '#33. Watching https://youtu.be/k9zTr2MAFRg', '#34. meeting people', '#35. learning', '#36. answering questions', '#37. thinking of interesting questions', '#38. making a decision', '#39. Being fit', '#40. flying', '#41. sitting straight up', '#42. being specific', '#43. helping people', '#44. creating art', '#45. Remembering you are in america', '#46. being unapologetic about being yourself', '#47. deciding what you want to do the next day in the evening', '#48. someone you respect giving you an assignment', '#49. doing everything above with friends', '#50. becoming more like your role models', '#51. deciding the top 3 things you want to do in 10 years', '#52. doing things that make you happy', '#53. laughing at your own jokes', '#54. Getting sunlight', '#55. being intentional', '#56. talking to someone intentional', '#57. following inspiration', '#58. Making a gc with 3 friends in which everyone does 1 courageous thing a day for 9 days']

        # Remove any empty lines from the list of morale boosters
        morale_boosters = [line for line in morale_boosters if line.strip()]

        # Randomly select 5 ways to boost morale
        random_boosters = random.sample(morale_boosters, 5)

        # Display the reminder lines and the randomly selected morale boosters
        st.write("That sucks, do at least one of these and re-evaluate. Try:\n")
        st.write("\n\n".join(random_boosters))
    else:
        st.write("Go and take actions!")

# Add a footer with the link
footer_html = '''
<style>
    footer {
        text-align: center;
        padding: 20px;
        background-color: transparent;
        color: white;
        font-size: 14px;
    }

    footer a {
        color: #6c757d;
        text-decoration: none;
    }
    footer a:hover {
        color: #f8f9fa;
        text-decoration: underline;
    }
</style>
<footer>
    list modified <a href="https://docs.google.com/document/d/1_9RudMX0Pq9iArqunJnQITtQTjbFplhjHt0WZ4cFqOg/edit?usp=sharing" target="_blank">here</a> and compiled from Alexey Guzey's post: <a href="https://guzey.com/morale/" target="_blank">https://guzey.com/morale/</a>
</footer>
'''

st.markdown(footer_html, unsafe_allow_html=True)