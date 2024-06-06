from transformers import pipeline
import numpy as np

# Load the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# List of performance descriptions
performance_descriptions = [
    "The candidate demonstrated exceptional coding skills, quickly solving complex problems and optimizing existing algorithms to improve performance.",

    "Throughout the project, the candidate consistently communicated effectively with team members, providing clear and concise updates and facilitating productive meetings.",

    "As the project lead, the candidate showed strong leadership qualities, motivating the team, delegating tasks efficiently, and ensuring that milestones were met on time.",

    "The candidate displayed remarkable adaptability, swiftly adjusting to unexpected changes in project scope and incorporating new requirements without disrupting the workflow.",

    "Demonstrating a high level of creativity, the candidate proposed innovative solutions that significantly enhanced the project’s overall functionality and user experience.",

    "When faced with a critical issue, the candidate applied analytical thinking to identify the root cause and implement a successful resolution under tight deadlines.",

    "The candidate's attention to detail was evident in the meticulous documentation and thorough testing processes, ensuring the final deliverable was of high quality.",
    "Taking initiative, the candidate independently researched new technologies and integrated them into the project, resulting in improved efficiency and performance.",
    "The candidate maintained a professional demeanor during client interactions, effectively understanding their needs and providing satisfactory solutions that exceeded expectations.",
    "Exemplary time management skills were demonstrated as the candidate balanced multiple tasks simultaneously, meeting all deadlines without compromising the quality of work.",
    "The candidate struggled to meet deadlines and often required additional guidance to complete tasks, which affected the overall project timeline and quality.",
    "The candidate effectively managed conflicts within the team, mediating disputes and fostering a collaborative environment to ensure smooth project progression.",
    "Showing a strong commitment to personal development, the candidate actively sought feedback and consistently applied it to improve their skills and performance.",
    "The candidate frequently made errors in their code, which required extensive debugging and review from senior team members, slowing down the project progress.",
    "The candidate had difficulty communicating their ideas clearly and often missed important updates from the team, leading to misunderstandings and delays.",
    
    "The candidate showed little initiative in taking on additional responsibilities or suggesting improvements, often waiting for direction from others.",

    "When faced with changes in project requirements, the candidate struggled to adapt, resulting in missed deadlines and increased stress for the team.",

    "The candidate often missed deadlines and had to rush through tasks at the last minute, resulting in subpar quality of work.",

    "The candidate frequently displayed a negative attitude towards feedback and collaboration, creating a challenging work environment for others."
]

# Custom scoring function to add variability
def custom_score(label, score):
    if label == 'POSITIVE':
        return np.clip(score * 1.5, 0, 1)
    else:
        return np.clip(score * 1.5, -1, 0)

# Analyze each performance description
for description in performance_descriptions:
    result = sentiment_analysis(description)[0]
    label = result['label']
    score = result['score']

    # Convert the sentiment label to a custom weight (positive or negative)
    weight = custom_score(label, score)

    print(f"Performance Description: {description}")
    print(f"Sentiment Label: {label}")
    print(f"Score: {score}")
    print(f"Weight: {weight}\n")
