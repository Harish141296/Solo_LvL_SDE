from tracker.models import Quest
from datetime import datetime, timedelta

base_topics = [
    "Solve 1 LeetCode problem on", "Watch a 15-min tutorial on", "Read and summarize article about",
    "Practice implementing", "Debug a broken function in", "Write notes on", "Review GitHub repo related to",
    "Practice type-speed coding on", "Sketch a diagram for", "Build a mini-project using"
]

sub_topics = [
    "Arrays", "Linked Lists", "Stacks", "Queues", "Binary Trees", "Graphs", "Hash Tables", "Recursion",
    "Dynamic Programming", "Sorting Algorithms", "Searching Algorithms", "System Design", "APIs", "Databases",
    "SQL Joins", "Indexing", "Django Views", "Flask Routing", "Linux Commands", "CI/CD", "Docker", "Kubernetes",
    "AWS EC2", "Git Workflows", "OAuth2", "Logging", "Monitoring", "Multithreading", "Async in Python",
    "Design Patterns", "OOP", "REST API", "GraphQL", "Unit Testing", "Pytest", "Postman", "HTTP Protocol",
    "TCP/IP", "OS Concepts", "Virtual Memory", "Caching", "Load Balancers", "Message Queues", "Data Lakes",
    "Pandas", "Numpy", "Matplotlib", "Scikit-learn", "Prompt Engineering", "LangChain", "LLMs", "Tokenization",
    "Data Cleaning", "Version Control", "Refactoring", "Code Review"
]

from random import shuffle, seed
seed(42)
sub_topics = sub_topics * 20
shuffle(sub_topics)
today = datetime.today()

quests = []
for i in range(1000):
    title = f"{base_topics[i % len(base_topics)]} {sub_topics[i]}"
    quests.append(Quest(title=title, date=today + timedelta(days=i % 60)))

Quest.objects.bulk_create(quests)
