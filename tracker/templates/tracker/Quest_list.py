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

from tracker.models import Quest
from datetime import datetime, timedelta

today = datetime.today()

quest_data = [
    # Day 1
    ("Solve 1 LeetCode problem (Easy)", 0),
    ("Watch a Python concept tutorial (15 mins)", 0),
    ("Initialize a GitHub repo and commit something", 0),
    ("Watch 'What is DevOps?' overview", 0),

    # Day 2
    ("Solve 1 LeetCode problem (Medium)", 1),
    ("Learn Python class and __init__ usage", 1),
    ("Practice Git branching locally", 1),
    ("Explore AI Prompting with ChatGPT", 1),

    # Day 3
    ("Solve 1 LeetCode problem using Sliding Window", 2),
    ("Read about CI/CD pipeline basics", 2),
    ("Practice Python OOP exercise", 2),
    ("Watch GPT real-world use-case video", 2),

    # Day 4
    ("Solve 1 SQL or DB-based LeetCode problem", 3),
    ("Learn Python error handling with try/except", 3),
    ("Resolve a Git merge conflict", 3),
    ("Use OpenAI Playground for a basic test", 3),

    # Day 5
    ("Solve 1 Graph or Tree LeetCode problem", 4),
    ("Build a small Python automation script", 4),
    ("Create PR and merge it", 4),
    ("Explore LangChain 101 or HuggingFace basics", 4),

    # Day 6
    ("Practice Python File I/O", 5),
    ("Explore Docker fundamentals", 5),
    ("Solve a DSA topic of your choice", 5),
    ("Read an AI paper summary", 5),

    # Day 7
    ("Reflect and write down weekly learnings", 6),
    ("Solve a recap LeetCode problem", 6),
    ("Watch advanced Git tips video", 6),
    ("Do guided meditation or reward walk", 6),
]

for title, offset in quest_data:
    Quest.objects.create(
        title=title,
        date=today + timedelta(days=offset),
        is_completed=False
    )

