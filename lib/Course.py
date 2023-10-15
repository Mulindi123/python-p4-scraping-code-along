class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output=""
        output += f'Title: {self.title}\n Schedule: {self.schedule}\nDescription: {self.description}\n'
        output +='-----------------------------'
        return output   
    

#programming = Course("Programming Robots for Outer Space,", "FullTime", "Learn python programming in 15 weeks")
