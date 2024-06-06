from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

# Aprendizado por Transferência -> tópico de ML

# List of performance descriptions
performance_descriptions = [
    "The candidate demonstrated exceptional coding skills, quickly solving complex problems and optimizing existing algorithms to improve performance.",
    "Throughout the project, the candidate consistently communicated effectively with team members, providing clear and concise updates and facilitating productive meetings."
]

# Define candidate labels for classification
candidate_labels = [
    "excellent performance", 
    "good performance", 
    "average performance", 
    "poor performance"
    ]

# Analyze each performance description
for description in performance_descriptions:
    result = classifier(description, candidate_labels)
    label = result['labels'][0]
    score = result['scores'][0]

    # CT 1 DISPONIBILIDADE 2 SS 2 ============ 8.7 = nota_usuario

    # Convert the classification label to a score (0 to 1)
    if label == "excellent performance":
        final_score = score
    elif label == "good performance":
        final_score = score * 0.75
    elif label == "average performance":
        final_score = score * 0.5
    else:
        final_score = score * 0.25

    print(f"\nPerformance Description: {description}")
    print(f"Classification Label: {label}")
    print(f"Classification Score: {score}")
    print(f"Final Score: {final_score}\n")
