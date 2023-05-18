from datetime import datetime

from repo_students import Link,repository

link = Link("https://github.com/Spartan03168/Flask-BMI-calculator","jkv549",datetime.utcnow())
link_2 = Link("https://github.com/Spartan03168/Flask-BMI-calculator","jjbhvyt9849",datetime.utcnow())

repository.create(link)
repository.create(link_2)
print(repository.get())
print(repository.get("jkv549"))


